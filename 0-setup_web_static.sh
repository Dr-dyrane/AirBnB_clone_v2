#!/usr/bin/env bash
# ----------------------------------------------------------------------
# Script Name:  0-setup_web_static.sh
# Usage:        sudo ./0-setup_web_static.sh
# Description:  This Bash script sets up web servers for the deployment
#               of web_static on an Ubuntu system with Nginx. It performs
#               the following tasks:
#               - Installs Nginx if not already installed
#               - Allows Nginx through the firewall
#               - Creates necessary directories for web_static
#               - Generates a fake HTML file for testing
#               - Sets up symbolic links for web_static
#               - Sets ownership to the ubuntu user and group recursively
#               - Updates Nginx configuration to serve web_static content
#               - Restarts Nginx to apply changes
# Author:       Alexander Udeogaranya
# Repository:   (https://github.com/Dr-dyrane/AirBnB_clone_v2)
# Examples:     sudo ./0-setup_web_static.sh
# ----------------------------------------------------------------------

# Update package information and install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Allow Nginx through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file for testing
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Add the alias configuration to the Nginx default server block
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart

# Exit with success status
exit 0