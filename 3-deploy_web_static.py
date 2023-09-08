#!/usr/bin/python3
"""
Script Name: 3-deploy_web_static.py
Usage:       fab -f 3-deploy_web_static.py deploy
Description: This Fabric script creates and deploys a web_static archive
             to web servers.
    It packages the web_static directory, distributes it to the servers,
             and updates the symbolic link.
Author:      Alexander Udeogaranya
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run

# Define the list of host servers
env.hosts = ['100.25.19.204', '54.157.159.85']


def do_pack():
    """
    Create a tar gzipped archive of the web_static directory.

    Returns:
        str: The path to the created archive on success, None on failure.
    """
    # Get the current time
    dt = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    target_dir = "versions"

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create the archive using tar
    archive_path = os.path.join(target_dir, file_name)
    cmd = "tar -czvf {} web_static".format(archive_path)
    if local(cmd).failed:
        return None

    return archive_path


def do_deploy(archive_path):
    """
    Distribute an archive to a web server and update the symbolic link.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True on success, False on failure.
    """
    if not os.path.exists(archive_path):
        return False

    # Extract the file name and name without extension
    file_name = os.path.basename(archive_path)
    name = file_name.split('.')[0]

    # Define paths on the remote server
    tmp_archive = "/tmp/{}".format(file_name)
    releases_dir = "/data/web_static/releases/{}".format(name)

    # Upload the archive to the remote server
    if put(archive_path, tmp_archive).failed:
        return False

    # Commands to execute on the remote server
    commands = [
        "rm -rf {}/".format(releases_dir),
        "mkdir -p {}/".format(releases_dir),
        "tar -xzf {} -C {}/".format(tmp_archive, releases_dir),
        "rm {}".format(tmp_archive),
        "mv {}/web_static/* {}/".format(releases_dir, releases_dir),
        "rm -rf {}/web_static".format(releases_dir),
        "rm -rf /data/web_static/current",
        "ln -s {} /data/web_static/current".format(releases_dir)
    ]

    # Execute commands on the remote server
    for cmd in commands:
        if run(cmd).failed:
            return False

    return True


def deploy():
    """
    Create and distribute an archive to a web server and
    update the symbolic link.

    Returns:
        bool: True on successful deployment, False on failure.
    """
    # Create the archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Deploy the archive
    return do_deploy(archive_path)


if __name__ == "__main__":
    # Run the deployment when this script is executed directly
    deploy()
