<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/dotzenith/tilde?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/dotzenith/tilde?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/dotzenith/tilde?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://img.shields.io/github/commit-activity/y/dotzenith/tilde?color=96CDFB&labelColor=302D41&style=for-the-badge&label=COMMITS"/>
   <br>
</div>

<p/>

---

### ❖ Information 

  <b></b>

  tilde is an effort to automagically deploy a homeserver with a few useful services using [pyinfra](https://pyinfra.com/).
  While it's built for personal use cases in mind, it's general enough to be used by anyone. Expect breaking changes :)

  <b></b>

  <img src="https://github.com/dotzenith/dotzenith/blob/main/assets/tilde/tilde.png" alt="tilde photo">

---

### ❖ Features

  <b></b>

  - A [Wireguard](https://www.wireguard.com/) tunnel with a user-friendly interface so you can access your services even when you're not home, without exposing them to the internet.
  - Dynamic DNS using [DuckDNS](https://www.duckdns.org/) so that wireguard can always connect you to your services
  - A [Nextcloud](https://nextcloud.com/) instance for your own cloud storage
  - A [Jellyfin](https://jellyfin.org/) instance for media consumption
  - [Grafana](https://grafana.com/) with [Prometheus](https://prometheus.io/) for server monitoring
    - Comes with [Node Exporter](https://github.com/prometheus/node_exporter) (System Stats) and [cadvisor](https://github.com/google/cadvisor) (Container Stats) pre-configured. Add any dashboard compatible with them.
  - A [Nginx Proxy Manager](https://nginxproxymanager.com/) Instance for reverse proxy and TLS (Configured by the user)

---

### ❖ Requirements

While tilde is meant to be very hands off, there's still a few things you'll need to do manually. It's not incredibly complicated, but the instructions are written under the assumption that you're at least a little bit familiar with unix commandline.

<b></b>

#### ❖ The server itself

- A machine running Debian 12 or above (for future)
- SSH access with a non-root user
- Sudo privileges for the non-root user


If you don't have ssh keys set up, please take a look at the [Github Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) on the topic.


Your ssh config should should look something like this if you're on MacOS:

```
# .ssh/config

host <homeserver>
  HostName <internal-ip-of-server> 
  user <non-root-user>

host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
> Replace \<homeserver\>, \<internal-ip-of-server\>, and \<non-root-user\> with the appropriate values (without the < >)

NOTE: This is for your personal machine, NOT for the server. 

If you're on a different OS, the Github guide has instructions for windows and linux as well, I trust that you'll be able to follow them :)

<b></b>

#### ❖ Port forwarding

In order for the Wireguard tunnel to work, you'll need to set up port forwarding on your home router. The instructions can vary from router to router so there are no specific instructions on how to do so.

Once you've figured out how to do so, forward port `51820` to port `51820` of your homeserver.

<b></b>

#### ❖ Dynamic DNS

With a residential internet connection, your public IP is liable to change at any given moment. This is why you'll need to set up Dynamic DNS to make sure the Wireguard tunnel can still connect you to your home network even if your public IP changes.

tilde uses [ZenDNS](https://github.com/dotzenith/ZenDNS) to periodically update the DNS records. While this guide assumes that [DuckDNS](https://www.duckdns.org/) will be used,
[ZenDNS](https://github.com/dotzenith/ZenDNS) also works with [Cloudflare](www.cloudflare.com) and [Namecheap](https://www.namecheap.com/). Please read the docs for [ZenDNS](https://github.com/dotzenith/ZenDNS) to configure what works best for you.

Assuming you're using [DuckDNS](https://www.duckdns.org/):

- Sign up for an account
- Pick a new subdomain on the website and click `add domain`
- Copy the `token` from the website as well

Fill out the information in [src/tilde/templates/zendns.yaml.j2](./src/tilde/templates/zendns.yaml.j2). It should look something like:
```yaml
duckdns:
  - token: "your-token"
    domain: "your-subdomain.duckdns.org"
```

Again, look at the docs for [ZenDNS](https://github.com/dotzenith/ZenDNS) and replace the contents of [src/tilde/templates/zendns.yaml.j2](./src/tilde/templates/zendns.yaml.j2) with configuration
for your chosen provider.

<b></b>

#### ❖ Environment Variables

As the final step of preparation, you'll need to fill out some environment variables in the [run script](./run.sh).

```
# run.sh
export USERNAME=<non-root-user>
export HOST=<homeserver-from-your-ssh-config>

export WIREGUARD_PASSWORD=<password-you-want-for-wireguard-ui>
export WIREGUARD_HOST=<your-subdomain.duckdns.org>

# Can be obtained by running `id $user`
export TILDE_UID=<uid-here>
export TILDE_GID=<gid-here>

# Timezone see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
export TZ=America/New_York
```
> Without the < >

### ❖ Deploying.

Phew that was a lot!! But we're finally ready to deploy!

tilde only has one dependency: `pyinfra`. You can either use [uv](https://docs.astral.sh/uv/) like I do, or just use a venv and install `pyinfra` yourself, it's totally up to you!

#### ❖ Using uv

```
uv sync                         # Create a virutal environment and install pyinfra
source .venv/bin/activate       # Activate the virutal environment
./run.sh                        # Run tilde on your homeserver
```

#### ❖ Using a normal venv
```
python3 -m venv tilde_venv          # Create a venv for tilde
source tilde_venv/bin/activate      # Activate the venv
pip3 install pyinfra                # Install pyinfra and dotenv
./run.sh                            # Run tilde on your homeserver
```

If everything goes as expected, you'll have a shiny new homeserver complete with all the features mentioned earlier!

The services are available at `homeserver-internal-ip:service-port`

The mapping for the ports is as follows:

- `nginx:       81`
- `nextcloud:   8080`
- `jellyfin:    8096`
- `wireguard:   51821`
- `grafana:     3000`

Feel free to use Nginx Proxy Manager to set up internal domains for these services

### ❖ What's New? 

0.6.0 - Added Grafana and Prometheus

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>
