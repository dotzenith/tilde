"""
A task file to deploy Wireguard

It first runs an update script for Dynamic DNS and then sets up a cron job to run that script every 24 hours

It then uses a docker-compose file to spin up the stack
"""
from pyinfra import host, logger
from pyinfra.operations import server

from tilde.helpers import USERNAME, get_docker_env_vars, is_container_running

env_vars = get_docker_env_vars()

# Helper function
def is_cron_job_initiated(cron_file: str):
    """
    A simple function to check if a cron job already exists

    cron_file: str
        Name of the cron job file
    """
    command = f'[ -f /etc/cron.d/{cron_file} ] && echo "Cron Job Exists"'
    status, stdout, _ = host.run_shell_command(
        command=command,
        sudo=True,
    )
    return status and ("Cron Job Exists" in stdout)


# Update cloudflare dns
server.shell(
    name="Run DDNS script",
    commands=[f"bash /home/{USERNAME}/tilde/templates/cloudflare-template.sh"],
    _sudo=True,
)

# Add cron job
if is_cron_job_initiated("cloudflare_job"):
    logger.info("Cloudflare job already set up")
else:
    server.shell(
        name="Add DDNS script to cron",
        commands=[
            f"echo '0 0 * * * /home/{USERNAME}/tilde/templates/cloudflare-template.sh' > cloudflare_job",
            "mv cloudflare_job /etc/cron.d/",
        ],
        _sudo=True,
    )

# Spin up stack
if is_container_running("wireguard"):
    logger.info("Wireguard container already running")
else:
    server.shell(
        name="Make directory for Wireguard",
        commands=[
            f"if [ ! -d {env_vars['WG_DIR']} ]; then mkdir -p {env_vars['WG_DIR']}; fi"
        ],
    )
    server.shell(
        name="Deploy Wireguard container",
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/wireguard.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,
    )
