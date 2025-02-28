# ❖ Deployment

After all that work, we are finally ready to deploy!!

Tilde only has one dependency: [pyinfra](https://pyinfra.com/). You can either use [uv](https://docs.astral.sh/uv/) like I do,
or just use a venv and install [pyinfra](https://pyinfra.com/) yourself, it's totally up to you!

## ❖ Using uv

```bash
uv sync                         # Create a virutal environment and install pyinfra
source .venv/bin/activate       # Activate the virutal environment
./run.sh                        # Run tilde on your homeserver
```

## ❖ Using a venv

```bash
python3 -m venv tilde_venv          # Create a venv for tilde
source tilde_venv/bin/activate      # Activate the venv
pip3 install pyinfra                # Install pyinfra and dotenv
./run.sh                            # Run tilde on your homeserver
```

If everything goes as expected, you'll have a shiny new home server complete with all the features mentioned earlier!

The services are available at `homeserver-internal-ip:service-port`

The mapping for the ports is as follows:
```
Nginx Proxy Manager:       81
Wireguard:                 51821
Grafana:                   3000
Jellyfin:                  8096
Nextcloud:                 8080
```
