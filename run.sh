#!/bin/bash

# Base exports
export USERNAME=
export HOST=

# Can be obtained by running `id $user`
export TILDE_UID=
export TILDE_GID=

# Timezone see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
export TZ=America/New_York

# Run
cd src/tilde && pyinfra inventory.py deploy.py
