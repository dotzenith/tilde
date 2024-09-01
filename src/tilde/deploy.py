"""
The parent deploy script for pyinfra
"""

from pyinfra import local
from pyinfra.operations import apt

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
    packages=["curl", "git"],
    _sudo=True,
)

# Installing frequently used packages
apt.packages(
    name="Install frequently used packages",
    packages=["vim", "neofetch"],
    _sudo=True,
)

local.include("tasks/make_dirs.py")
local.include("tasks/install_docker.py")
local.include("tasks/zendns.py")
local.include("tasks/wireguard.py")
local.include("tasks/nextcloud.py")
local.include("tasks/jellyfin.py")
local.include("tasks/nginx.py")
