#!/usr/bin/python3
"""
Script Name: 2-do_deploy_web_static.py
Usage:
    fab -f 2-do_deploy_web_static.py do_deploy:archive_path=<path_to_archive>
Description: This Fabric script deploys a web_static archive to web servers.
    It uploads, uncompresses, and manages symbolic links for the archive.
Author:      Alexander Udeogaranya
Example:
    fab -f 2-do_deploy_web_static.py
    do_deploy:archive_path=versions/web_static_20170315003959.tgz
"""

import os
from fabric.api import env, put, run

env.hosts = ['100.25.19.204', '54.157.159.85']


def do_deploy(archive_path):
    """
    Distribute an archive to a web server, unpack, and manage symbolic links.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True on success, False on failure.
    """
    # Check if the archive exists
    if not os.path.isfile(archive_path):
        return False

    # Extract the archive file name and name without extension
    file_name = os.path.basename(archive_path)
    name = file_name.split('.')[0]

    # Upload the archive to the server
    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False

    # Define remote paths
    releases_dir = "/data/web_static/releases/{}".format(name)

    # Unpack the archive and clean up
    commands = [
        "rm -rf {}/".format(releases_dir),
        "mkdir -p {}/".format(releases_dir),
        "tar -xzf /tmp/{} -C {}/".format(file_name, releases_dir),
        "rm /tmp/{}".format(file_name),
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


if __name__ == "__main__":
    # Run the deployment when this script is executed directly
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("archive_path", help="Path to the archive to deploy")
    args = parser.parse_args()
    
    if do_deploy(args.archive_path):
        print("Deployment successful!")
    else:
        print("Deployment failed.")
