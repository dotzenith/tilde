"""
A task file to deploy nextcloud

Uses a docker-compose file to spin up the stack with Nextcloud, Postgres, and Redis
"""

from pyinfra import logger
from pyinfra.operations import server

from tilde.helpers import USERNAME, get_docker_env_vars, is_container_running

env_vars = get_docker_env_vars()

# Spin up stack
if is_container_running("nextcloud"):
    logger.info("Nextcloud container already running")
else:

    server.shell(
        name="Deploy Nextcloud container",
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/nextcloud.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,
    )
