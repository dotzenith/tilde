"""
Variables to use around the deployment
"""

import os

from pyinfra_cli.exceptions import sys

USERNAME = os.environ["USERNAME"]
HOST = os.environ["HOST"]
UID = os.environ["TILDE_UID"]
GID = os.environ["TILDE_GID"]
TZ = os.environ["TZ"]
HOME = f"/home/{USERNAME}"

for var in [USERNAME, HOST, UID, GID, TZ]:
    if len(var) < 1:
        print("One or more environment variables not set")
        sys.exit(1)
