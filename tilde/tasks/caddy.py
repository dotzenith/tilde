"""
A task file to deploy caddy
"""

from pyinfra import logger
from pyinfra.operations import files

from tilde.helpers import USERNAME, DOMAIN, INTERNAL_DOMAIN, is_container_running


# Spin up stack
if is_container_running("caddy"):
    logger.info("Caddy container already running")
else:

    username = USERNAME
    domain = DOMAIN
    internal_domain = INTERNAL_DOMAIN

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
        DOMAIN=DOMAIN,
        INTERNAL_DOMAIN=INTERNAL_DOMAIN,
    )
