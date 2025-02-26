"""
A task file to deploy nextcloud

Uses a docker-compose file to spin up the stack with Nextcloud, Postgres, and Redis
"""

from pyinfra.operations import server, files

from tilde.vars import USERNAME, HOME, UID, GID, TZ

files.directory(
    name="Make nextcloud tilde directory",
    path=f"{HOME}/tilde/nextcloud",
    present=True,
    user=USERNAME,
)
files.template(
    name="Copy Nextcloud Docker Compose",
    src="templates/nextcloud.yml.j2",
    dest=f"{HOME}/tilde/nextcloud/docker-compose.yml",
    UID = UID,
    GID = GID,
    TZ = TZ
)
server.shell(
    name="Deploy Nextcloud container",
    commands=[f"cd {HOME}/tilde/nextcloud && docker compose up -d"],
    _sudo=True,  
)
