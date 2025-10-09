"""
A task file to deploy nextcloud

Uses a docker-compose file to spin up the stack with Nextcloud, Postgres, and Redis
"""

from pyinfra.operations import files, server

from tilde.vars import HOME, USERNAME

zendns_config = f"{HOME}/tilde/zendns/config.json"
zendns_logfile = f"{HOME}/tilde/zendns/zendns.log"

files.directory(
    name="Make ZenDNS tilde directory",
    path=f"{HOME}/tilde/zendns",
    present=True,
    user=USERNAME,
)
files.template(
    name="Copy ZenDNS config",
    src="templates/zendns.json.j2",
    dest=zendns_config,
)
server.shell(
    name="Install ZenDNS",
    commands=[
        "curl --proto '=https' --tlsv1.2 -LsSf https://github.com/dotzenith/zendns/releases/latest/download/zendns-installer.sh | sh"
    ],
)
server.shell(
    name="Run ZenDNS for the first time",
    commands=[
        f"{HOME}/.cargo/bin/zendns --config {zendns_config} --log {zendns_logfile}"
    ],
)
server.crontab(
    name="Add Crontab for Dynamic DNS",
    command=f"{HOME}/.cargo/bin/zendns --config {zendns_config} --log {zendns_logfile}",
    minute="0",
    hour="*/12",
    month="*",
    day_of_week="*",
    day_of_month="*",
    interpolate_variables=True,
    user=USERNAME
)
