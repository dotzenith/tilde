#!/bin/bash

# Base exports
export USERNAME=
export HOST=

# Password for PostgreSQL database used by nextcloud 
export POSTGRES_PASSWORD=

# Settings for wg-easy
export WIREGUARD_PASSWORD=
export WIREGUARD_HOST=

# Run
cd src/tilde && pyinfra inventory.py deploy.py
