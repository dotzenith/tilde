"""
A few helper functions for different tasks
"""

import os
import re

from dotenv import dotenv_values
from pyinfra import host

USERNAME = os.environ["SERVER_USER"]

def is_container_running(container_name: str) -> bool:
    """
    Checks if a container is running in a very basic manner

    container_name: str
        The name of the container
    """

    command = "docker ps"
    _, stdout, _ = host.run_shell_command(
        command=command,
        sudo=True,
    )
    return len(re.findall(f"{container_name}", str(stdout))) > 0


def get_docker_env_vars() -> dict[str, str | None]:
    """
    Return a dict of values stored in compose/.env
    """

    return dotenv_values("compose/.env")
