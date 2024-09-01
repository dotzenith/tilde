"""
A task file to install Docker

Checks if Docker is installed and if it isn't, installs Docker using a convenience script
"""
from pyinfra import logger
from pyinfra.operations import server, python

from tilde.vars import USERNAME

def is_docker_installed():
    """
    A helper function to check if Docker is already installed
    """
    command = "docker run hello-world"
    result = server.shell(
        commands=[command],
        _sudo=True,
    )
    return result.did_succeed()

def docker_orchestrator():
    if is_docker_installed():
        logger.info("Docker Already Installed")
    else:
        server.shell(
            name="Install docker",
            commands=[
                "curl -fsSL https://get.docker.com -o get-docker.sh",
                "sh get-docker.sh",
                "systemctl enable docker",
                "rm get-docker.sh"
            ],
            _sudo=True,
        )

        server.shell(
            name=f"Create docker group and add {USERNAME} to group",
            commands=[
                "getent group docker || groupadd docker",
                f"usermod -aG docker {USERNAME}",
            ],
            _sudo=True,
        )

python.call(
    name="Execute Docker orchestrator",
    function=docker_orchestrator,
)
