"""
The parent deploy script for pyinfra
"""

from pyinfra import local
from pyinfra.operations import apt, server

from tilde.helpers import USERNAME

# Prompt for sudo password when starting
_use_sudo_password = True

# Update Apt
apt.update(
    name="Update apt repositories",
    _sudo=True,
)

# Add some crucial packages
apt.packages(
    name="Install crucial packages",
    packages=["sudo", "curl", "git"],
    _sudo=True,
)

# Installing frequently used packages
apt.packages(
    name="Install frequently used packages",
    packages=["vim", "neofetch"],
    _sudo=True,
)

# Make tilde dir
server.shell(
    name="Make tilde dir",
    commands=[
        f"if [ ! -d /home/{USERNAME}/tilde ]; \
                then mkdir /home/{USERNAME}/tilde; fi",
    ],
)

# Install Docker
local.include("tasks/install_docker.py")

# Deploy Portainer
local.include("tasks/deploy_portainer.py")

# Sync Files
local.include("tasks/sync_files.py")

# Deploy Wireguard
local.include("tasks/deploy_wireguard.py")

# Deploy Nextcloud
local.include("tasks/deploy_nextcloud.py")

# Deploy Jellyfin
local.include("tasks/deploy_jellyfin.py")
