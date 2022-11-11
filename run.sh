#!/bin/bash

# Exports
export SERVER_USER=
export HOMESERVER=

# Run
cd tilde && pyinfra inventory.py deploy.py
