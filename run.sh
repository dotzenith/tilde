#!/bin/bash

# Base exports
export SERVER_USER=
export HOMESERVER=

# Run
cd tilde && pyinfra inventory.py deploy.py
