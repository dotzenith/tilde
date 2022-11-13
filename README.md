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
  While it's built for personal use cases in mind, it's general enough to be used by anyone. Expect breaking changes, this is forever a work in progress :)

  <b></b>

  <img src="https://github.com/dotzenith/dotzenith/blob/main/assets/tilde/tilde.png" alt="tilde photo">

---

### ❖ Features

  <b></b>

  - A [Wireguard](https://www.wireguard.com/) tunnel with a user-friendly interface so you can access your services even when you're not home, without exposing them to the internet. 
  - Dynamic DNS using [Cloudflare](https://www.cloudflare.com/) so that the Wireguard doesn't just stop working randomly.
  - A [Portainer](https://www.portainer.io/) instance to provide a nice GUI to manage all of your docker containers and deploy new ones.
  - A [Nextcloud](https://nextcloud.com/) instance set up with PostgreSQL and Alpine for your own personal cloud storage.
  - A [Jellffyin](https://jellyfin.org/) instance for media consumption.
  - A [Caddy](https://caddyserver.com/) web server for automatic TLS and internal domains to access the services

---

### ❖ Requirements

While tilde is meant to be very hands off, there's still a few things you'll need to do manually. It's not incredibly complicated, but the instructions are written under the assumption that you're at least a little bit familiar with unix commandline.

<b></b>

#### ❖ The server itself

- A machine running Debian 11 or above (for future).
- SSH access with a non-root user.
- Sudo privileges for the non-root user.


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

tilde assumes this will be done using Cloudflare and your own domain. You can also use something like [freedns](https://freedns.afraid.org/) but you'll need to modify some code to get that to work. 

Once you have a domain from either Cloudflare itself or transferred over to Cloudflare's DNS servers, you'll need to add a new "A" record. Make sure `Proxy status` is set to to `DNS only`. 

When you have all of that taken care of, you'll just need to fill out the [update script](./tilde/templates/cloudflare-template.sh) 

NOTE: You only need to fill out the following values, the script also has instructions on how to get these values:

- `auth_email`
- `auth_key`
- `zone_identifier`
- `record_name`
- `sitename` (optional)

<b></b>

#### ❖ Automatic TLS with Caddy

If you'd like to set up your services with automatic TLS (i.e. HTTPS) without exposing them to the internet, you'll need to set that up using Cloudflare as well. 

NOTE: If you don't need/want TLS for your internal services, feel free to skip this. You'll just have to comment out the call to the caddy task in [deploy.py](./tilde/deploy.py)

Add the following "A" records to your domain on the Cloudflare dashboard:

- `wireguard`
- `portainer`
- `jellyfin`
- `nextcloud`

Set the `Content` field to the internal IP of your homeserver and make sure `Proxy status` is set to to `DNS only`

Next: Create an API token for the DNS challenge (for more background, see https://github.com/libdns/cloudflare/blob/master/README.md):

1. In the upper right, click the person icon and navigate to `My Profile`, and then select the `API Tokens` tab.
1. Click the `Create Token` button, and then `Use template` on `Edit zone DNS`.
1. Edit the `Token name` field if you prefer a more descriptive name.
1. Under `Permissions`, the `Zone / DNS / Edit` permission should already be populated. Add another permission: `Zone / Zone / Read`.
1. Under `Zone Resources`, set `Include / Specific zone / example.com` (replacing `example.com` with your domain).
1. Under `TTL`, set an End Date for when your token will become inactive. You might want to choose one far in the future.
1. Create the token and copy the token value.

Once you have the API token, fill out the following values in the [.env file](./tilde/compose/.env):

- `CLOUDFLARE_EMAIL=<your-cloudflare-email>`
- `CLOUDFLARE_API_TOKEN=<the-API-token-you-just-generated>`

As a last step, fill out the following values in the [run script](./run.sh) as well:

- `DOMAIN=<your-cloudflare-domain.tld>`
- `INTERNAL_IP=<the-internal-ip-address-of-your-homeserver>`

NOTE: Nextcloud currently runs without TLS because of some weird issues with Caddy, this should be updated in the future

<b></b>

#### ❖ Environment Variables

As the final step of preparation, you'll need to fill out some environment variables in the [run script](./run.sh) and the [.env file](./tilde/compose/.env) for the docker-compose files.

```
# run.sh

export SERVER_USER=<non-root-user>
export HOMESERVER=<homeserver-from-your-ssh-config>
```

```
# .env

POSTGRES_PASSWORD=<password-you-want-for-nextcloud-db>
WG_PASS=<password-you-want-for-wireguard-ui>
WG_HOST=<record_name.your_domain.com>
```
> Without the < >

### ❖ Deploying.

Phew that was a lot!! But we're finally ready to deploy!

tilde only has two main dependencies `pyinfra` and `python-dotenv`. You can either use [Poetry](https://python-poetry.org/) like I do, or just use a venv and install the packages yourself, it's totally up to you!

#### ❖ Using Poetry

```
$ poetry shell    # Open up a virtual env using Poetry
$ poetry install  # Install pyinfra and dotenv 
$ ./run.sh        # Run tilde on your homeserver
```

#### ❖ Using a normal venv
```
$ python3 -m venv tilde_venv          # Create a venv for tilde
$ source tilde_venv/bin/activate      # Activate the venv
$ pip3 install pyinfra python-dotenv  # Install pyinfra and dotenv
$ ./run.sh                            # Run tilde on your homeserver
```

If everything goes as expected, you'll have a shiny new homeserver complete with all the features mentioned earlier!

If you opted to use Caddy. All services are available at `service.your-cloudflare-domain.com`. 

If you opted to not use Caddy. The services are available at `homeserver-internal-ip:service-port`. 
The mapping for the ports is as follows

- `wireguard: 51821`
- `portainer: 9000`
- `nextcloud: 8080`
- `jellyfin: 8096`

### ❖ What's New? 

0.3.0 - Added Caddy for automatic TLS

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>
