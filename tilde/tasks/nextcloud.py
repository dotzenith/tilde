"""
A task file to deploy nextcloud

Uses a docker-compose file to spin up the stack with Nextcloud, Postgres, and Redis
"""

from pyinfra import logger
from pyinfra.operations import server

from tilde.helpers import USERNAME, is_container_running

# Spin up stack
if is_container_running("nextcloud"):
    logger.info("Nextcloud container already running")
else:

    server.shell(
        name="Deploy Nextcloud container",  # type: ignore
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/nextcloud.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,  # type: ignore
    )
