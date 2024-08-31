"""
A task file to deploy Wireguard

It first runs an update script for Dynamic DNS and then sets up a cron job to run that script every 24 hours

It then uses a docker-compose file to spin up the stack
"""
from pyinfra.operations import files, server
from tilde.vars import USERNAME, HOME, WG_PASS, WG_HOST

wireguard_dir = f"{HOME}/container-data/wireguard"

files.directory(
    name="Make Wireguard container directory",
    path=wireguard_dir,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make Wireguard tilde directory",
    path=f"{HOME}/tilde/wireguard",
    present=True,
    user=USERNAME,
)
files.template(
    name="Copy Wireguard Docker Compose",
    src="templates/wireguard.yml.j2",
    dest=f"{HOME}/tilde/wireguard/docker-compose.yml",
    WG_PASS = WG_PASS,
    WG_HOST = WG_HOST,
    WG_DIR = wireguard_dir
)
server.shell(
    name="Deploy Wireguard container",
    commands=[f"cd {HOME}/tilde/wireguard && docker compose up -d"],
    _sudo=True,  
)
