"""
A task file to deploy nextcloud

Uses a docker-compose file to spin up the stack with Nextcloud, Postgres, and Redis
"""

from pyinfra import logger
from pyinfra.operations import files

from tilde.helpers import USERNAME, DOMAIN, INTERNAL_DOMAIN, is_container_running


# Spin up stack
if is_container_running("caddy"):
    logger.info("Caddy container already running")
else:

    files.directory(
        name="Make caddy data directory",  # type: ignore
        path="/data/caddy",
        present=True,
        user=USERNAME,
    )

    files.template(
        name="Setup Caddyfile",
        src="templates/caddyfile.j2",
        dest="/data/caddy/Caddyfile",
        user=USERNAME,
    )
