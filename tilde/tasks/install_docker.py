"""
A task file to install Docker

Checks if Docker is installed and if it isn't, installs Docker using a convenience script
"""
from pyinfra import host, logger
from pyinfra.operations import server

from tilde.helpers import USERNAME

# Helper function
def is_docker_installed():
    """
    A helper function to check if Docker is already installed
    """
    command = "docker run hello-world"
    status, stdout, _ = host.run_shell_command(
        command=command,
        sudo=True,
    )
    return status and ("Hello from Docker!" in stdout)


# Install Docker using convenience script
if is_docker_installed():
    logger.info("Docker Already Installed")
else:
    server.shell(
        name="Install docker",
        commands=[
            "curl -fsSL https://get.docker.com -o get-docker.sh",
            "sh get-docker.sh",
            "systemctl enable docker",
        ],
        _sudo=True,
    )

    server.shell(
        name=f"Create docker group and add {USERNAME} to group",
        commands=[
            "getent group somegroupname || groupadd somegroupname",
            f"usermod -aG docker {USERNAME}",
        ],
        _sudo=True,
    )
