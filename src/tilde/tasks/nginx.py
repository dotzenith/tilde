"""
A task file to deploy caddy
"""
from os import environ

from pyinfra import logger
from pyinfra.operations import files, server

from tilde.helpers import USERNAME, is_container_running

# Spin up stack
if is_container_running("nginx-proxy-manager"):
    logger.info("NPM container already running")
else:

    files.directory(
        name="Make nginx directory",  # type: ignore
        path="/data/nginx",
        present=True,
        user=USERNAME,
    )

    files.directory(
        name="Make nginx data directory",  # type: ignore
        path="/data/nginx/data",
        present=True,
        user=USERNAME,
    )

    files.directory(
        name="Make nginx letsencrypt directory",  # type: ignore
        path="/data/nginx/letsencrypt",
        present=True,
        user=USERNAME,
    )

    server.shell(
        name="Deploy Nginx Proxy Manager container",  # type: ignore
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/nginx.yml up -d"
        ],
        _sudo=True,  # type: ignore
    )
