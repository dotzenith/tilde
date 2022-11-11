"""
A task file to deploy Wireguard

It first runs an update script for Dynamic DNS and then sets up a cron job to run that script every 24 hours

It then uses a docker-compose file to spin up the stack
"""
from pyinfra import host, logger
from pyinfra.operations import files, server

from tilde.helpers import USERNAME, is_container_running


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
    name="Run DDNS script",  # type: ignore
    commands=[f"bash /home/{USERNAME}/tilde/templates/cloudflare-template.sh"],
    _sudo=True,  # type: ignore
)

# Add cron job
if is_cron_job_initiated("cloudflare_job"):
    logger.info("Cloudflare job already set up")
else:
    server.shell(
        name="Add DDNS script to cron",  # type: ignore
        commands=[
            f"echo '0 0 * * * /home/{USERNAME}/tilde/templates/cloudflare-template.sh' > cloudflare_job",
            "mv cloudflare_job /etc/cron.d/",
        ],
        _sudo=True,  # type: ignore
    )

# Spin up stack
if is_container_running("wireguard"):
    logger.info("Wireguard container already running")
else:
    files.directory(
        name="Make directory for Wireguard",  # type: ignore
        path=f"/home/{USERNAME}/data/wireguard",
        user=USERNAME,
        present=True,
    )
    server.shell(
        name="Deploy Wireguard container",  # type: ignore
        commands=[
            f"docker compose -f /home/{USERNAME}/tilde/compose/wireguard.yml \
              --env-file /home/{USERNAME}/tilde/compose/.env up -d"
        ],
        _sudo=True,  # type: ignore
    )
