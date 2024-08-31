"""
A task file to deploy Portainer

Does not use a docker-compose file, instead just uses a long command to spin up Portainer
"""
from pyinfra import logger
from pyinfra.operations import server

from tilde.helpers import is_container_running

# Spin up container
if is_container_running("portainer"):
    logger.info("Portainer Already running")
else:
    server.shell(
        name="Deploy Portainer",  # type: ignore
        commands=[
            "docker volume create portainer_data",
            "docker run -d -p 8000:8000 -p 9443:9443 -p 9000:9000 --name portainer \
            --restart=always \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v portainer_data:/data \
            portainer/portainer-ce:2.9.3",
        ],
        _sudo=True,  # type: ignore
    )
