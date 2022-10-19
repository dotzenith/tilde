"""
A task to sync the templates and docker-compose files
"""

from pyinfra.operations import files

from tilde.helpers import USERNAME

# Sync templates
files.sync(
    name="Sync templates",
    user=USERNAME,
    src="templates",
    dest=f"/home/{USERNAME}/tilde/templates/",
)

# Sync compose files
files.sync(
    name="Sync compose files",
    user=USERNAME,
    src="compose",
    dest=f"/home/{USERNAME}/tilde/compose/",
)
