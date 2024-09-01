#!/bin/bash

# Base exports
export USERNAME=
export HOST=

# Settings for wg-easy
export WIREGUARD_PASSWORD=
export WIREGUARD_HOST=

# Run
cd src/tilde && pyinfra inventory.py deploy.py
