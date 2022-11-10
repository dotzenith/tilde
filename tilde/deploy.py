"""
The parent deploy script for pyinfra
"""

from pyinfra import local
from pyinfra.operations import apt

# Prompt for sudo password when starting
_use_sudo_password = True

# Update Apt
apt.update(
    name="Update apt repositories", #type: ignore
    _sudo=True, #type: ignore
)

# Add some crucial packages
apt.packages(
    name="Install crucial packages", #type: ignore
    packages=["sudo", "curl", "git"],
    _sudo=True, #type: ignore
)

# Installing frequently used packages
apt.packages(
    name="Install frequently used packages", #type: ignore
    packages=["vim", "neofetch"],
    _sudo=True, #type: ignore
)


# Set up some directories
local.include("tasks/make_dirs.py")

# Sync Files
local.include("tasks/sync_files.py")

# Install Docker
local.include("tasks/install_docker.py")

# Deploy Portainer
local.include("tasks/deploy_portainer.py")

# Deploy Wireguard
local.include("tasks/deploy_wireguard.py")

# Deploy Nextcloud
local.include("tasks/deploy_nextcloud.py")

# Deploy Jellyfin
local.include("tasks/deploy_jellyfin.py")
