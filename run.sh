#!/bin/bash

# Exports
export SERVER_USER=
export HOMESERVER=
export DOMAIN=
export INTERNAL_DOMAIN=

# Run
cd tilde && pyinfra inventory.py deploy.py
