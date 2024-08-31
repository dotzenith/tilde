"""
A task file to deploy nginx
"""
from pyinfra.operations import files, server

from tilde.vars import USERNAME, HOME

nginx_data = f"{HOME}/container-data/nginx/data"
nginx_letsencrypt = f"{HOME}/container-data/nginx/letsencrypt"

files.directory(
    name="Make nginx container directory",
    path=f"{HOME}/container-data/nginx",
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make nginx data directory",
    path=nginx_data,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make nginx letsencrypt directory",
    path=nginx_letsencrypt,
    present=True,
    user=USERNAME,
)
files.directory(
    name="Make Nginx tilde directory",
    path=f"{HOME}/tilde/nginx",
    present=True,
    user=USERNAME,
)
files.template(
    name="Copy Nginx Docker Compose",
    src="templates/nginx.yml.j2",
    dest=f"{HOME}/tilde/nginx/docker-compose.yml",
    nginx_data = nginx_data,
    nginx_letsencrypt = nginx_letsencrypt
)
server.shell(
    name="Deploy Nginx container",
    commands=[f"cd {HOME}/tilde/nginx && docker compose up -d"],
    _sudo=True,  
)
