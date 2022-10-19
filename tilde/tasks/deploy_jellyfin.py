"""
A task file to deploy Jellyfin

Creates directories for Jellffin data and uses a docker-compose file to spin up the stack
"""

from pyinfra import logger
from pyinfra.operations import server

from tilde.helpers import USERNAME, get_docker_env_vars, is_container_running

env_vars = get_docker_env_vars()

# Spin up stack
if is_container_running("jellyfin"):
    logger.info("jellyfin container already running")
else:
    # Make directories for jellyfin files
    server.shell(
        name="Make directories for Jellyfin",
        commands=[
            f"if [ ! -d {env_vars['JELLYFIN_CONFIG']} ]; \
                    then mkdir -p {env_vars['JELLYFIN_CONFIG']}; fi",
            f"if [ ! -d {env_vars['JELLYFIN_TV']} ]; \
                    then mkdir -p {env_vars['JELLYFIN_TV']}; fi",
            f"if [ ! -d {env_vars['JELLYFIN_MOVIES']} ]; \
                    then mkdir -p {env_vars['JELLYFIN_MOVIES']}; fi",
            f"if [ ! -d {env_vars['JELLYFIN_MUSIC']} ]; \
                    then mkdir -p {env_vars['JELLYFIN_MUSIC']}; fi",
        ],
    )
    server.shell(
        name="Deploy Jellyfin container",
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/jellyfin.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,
    )
