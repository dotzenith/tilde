"""
A task file to deploy caddy
"""
from os import environ

from pyinfra import logger
from pyinfra.operations import files, server

from tilde.helpers import USERNAME, is_container_running

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
        DOMAIN=environ["DOMAIN"],
        INTERNAL_IP=environ["INTERNAL_IP"],
    )

    server.shell(
        name="Build caddy cloudflare image",  # type: ignore
        commands=[
            f"docker build -t caddycloudflare:latest /home/{USERNAME}/tilde/compose/caddy/"
        ],
        _sudo=True,  # type: ignore
    )

    server.shell(
        name="Deploy caddy container",  # type: ignore
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/caddy/caddy.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,  # type: ignore
    )
