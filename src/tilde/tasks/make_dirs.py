"""
A task to make important directories and set permissions
"""

from pyinfra.operations import files

from tilde.vars import USERNAME

files.directory(
    name="Ensure a directory exists for all of the tilde files",
    path=f"/home/{USERNAME}/tilde",
    user=USERNAME,
    present=True,
)

files.directory(
    name="Ensure a directory exists to store data for various services",
    path=f"/home/{USERNAME}/container-data",
    user=USERNAME,
    present=True,
    _sudo=True,  # type: ignore
)
