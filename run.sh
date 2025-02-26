#!/bin/bash

# Base exports
export USERNAME=
export HOST=

# Settings for wg-easy
export WIREGUARD_PASSWORD=
export WIREGUARD_HOST=


# Can be obtained by running `id $user`
export TILDE_UID=
export TILDE_GID=

# Run
cd src/tilde && pyinfra inventory.py deploy.py
