"""
A task to make important directories and set permissions
"""

from pyinfra.operations import files, server

from tilde.helpers import USERNAME

files.directory(
    name="Ensure a directory exists for all of the tilde files",  # type: ignore
    path=f"/home/{USERNAME}/tilde",
    user=USERNAME,
    present=True,
)

files.directory(
    name="Ensure a directory exists to store data for various services",  # type: ignore
    path="/data",
    user=USERNAME,
    present=True,
    _sudo=True,  # type: ignore
)

server.shell(
    name="Ensure permissions for /data",  # type: ignore
    commands=[
        f"chown -R {USERNAME}:{USERNAME} /data",
        "chmod -R a=,a+rX,u+w,g+w /data",
    ],
    _sudo=True,  # type: ignore
)
