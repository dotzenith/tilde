#!/bin/bash

# Exports
export SERVER_USER=
export HOMESERVER=

# Fix Docker Volume Path
sed -i "" "s/username/$SERVER_USER/g" ./tilde/compose/.env

# Run
cd tilde && pyinfra inventory.py deploy.py
