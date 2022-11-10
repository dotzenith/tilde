"""
A task to sync the templates and docker-compose files
"""

from pyinfra.operations import files

from tilde.helpers import USERNAME

files.directory(
    name = "Ensure a directory exists for all of the tilde files", #type: ignore
    path = f"/home/{USERNAME}/tilde",
    user = USERNAME,
    present = True,
)

files.directory(
    name = "Ensure a directory exists to store data for various services", #type: ignore
    path = f"/home/{USERNAME}/data",
    user = USERNAME,
    present = True,
)
