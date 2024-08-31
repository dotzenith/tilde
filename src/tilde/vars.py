"""
Variables to use around the deployment
"""

import os

USERNAME = os.environ["USERNAME"]
HOST = os.environ["HOST"]
WG_PASS = os.environ["WIREGUARD_PASSWORD"]
WG_HOST = os.environ["WIREGUARD_HOST"]
HOME = f"/home/{USERNAME}"
