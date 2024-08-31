"""
A task file to deploy Jellyfin

Creates directories for Jellffin data and uses a docker-compose file to spin up the stack
"""

from pyinfra.operations import files, server
from tilde.vars import HOME, USERNAME

jellyfin_config = f"{HOME}/container-data/jellyfin/config"
jellyfin_movies = f"{HOME}/container-data/jellyfin/movies"
jellyfin_tv = f"{HOME}/container-data/jellyfin/tv"
jellyfin_music = f"{HOME}/container-data/jellyfin/music"

# Make directories for jellyfin files
files.directory(
    name="Make jellyfin container directory",  
    path=f"{HOME}/container-data/jellyfin",
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make jellyfin config directory",  
    path=jellyfin_config,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make jellyfin movies directory",  
    path=jellyfin_movies,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make jellyfin tv directory",  
    path=jellyfin_tv,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make jellyfin music directory",  
    path=jellyfin_music,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make jellyfin tilde directory",
    path=f"{HOME}/tilde/jellyfin",
    present=True,
    user=USERNAME,
)
files.template(
    name="Copy Jellyfin Docker Compose",
    src="templates/jellyfin.yml.j2",
    dest=f"{HOME}/tilde/jellyfin/docker-compose.yml",
    jellyfin_config = jellyfin_config,
    jellyfin_movies = jellyfin_movies,
    jellyfin_tv = jellyfin_tv,
    jellyfin_music = jellyfin_music
)
server.shell(
    name="Deploy Jellyfin container",
    commands=[f"cd {HOME}/tilde/jellyfin", "docker compose up -d"],
    _sudo=True,  
)
