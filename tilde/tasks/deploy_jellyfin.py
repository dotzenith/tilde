"""
A task file to deploy Jellyfin

Creates directories for Jellffin data and uses a docker-compose file to spin up the stack
"""

from pyinfra import logger
from pyinfra.operations import server
from pyinfra.operations import files

from tilde.helpers import USERNAME, is_container_running

# Spin up stack
if is_container_running("jellyfin"):
    logger.info("jellyfin container already running")
else:
    # Make directories for jellyfin files
    files.directory(
        name = "Make jellyfin config directory", # type: ignore
        path = "/home/{USERNAME}/data/jellyfin/config",
        present = True,
        user = USERNAME,
    )
    files.directory(
        name = "Make jellyfin movies directory", # type: ignore
        path = "/home/{USERNAME}/data/jellyfin/movies",
        present = True,
        user = USERNAME,
    )
    files.directory(
        name = "Make jellyfin tv directory", # type: ignore
        path = "/home/{USERNAME}/data/jellyfin/tv",
        present = True,
        user = USERNAME,
    )
    files.directory(
        name = "Make jellyfin music directory", # type: ignore
        path = "/home/{USERNAME}/data/jellyfin/music",
        present = True,
        user = USERNAME,
    )
    server.shell(
        name="Deploy Jellyfin container", # type: ignore
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/jellyfin.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True, # type: ignore
    )
