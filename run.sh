#!/bin/bash

# Base exports
export SERVER_USER=
export HOMESERVER=

# Only needed if you're using caddy
export DOMAIN=
export INTERNAL_IP=

# Run
cd tilde && pyinfra inventory.py deploy.py
