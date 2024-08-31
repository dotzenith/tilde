"""
A list of servers for pyinfra to act on.

Currently only has one element since tilde is meant for a single homeserver, but can easily be expanded to multiple.
"""

import os

my_hosts = [os.environ["HOMESERVER"]]
