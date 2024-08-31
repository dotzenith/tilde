"""
Variables to use around the deployment
"""

import os

USERNAME = os.environ["USERNAME"]
HOST = os.environ["HOST"]
PG_PASS = os.environ["POSTGRES_PASSWORD"]
WG_PASS = os.environ["WIREGUARD_PASSWORD"]
WG_HOST = ["WIREGUARD_HOST"]
HOME = f"/home/{USERNAME}"
