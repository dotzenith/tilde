<h1 align="center"> ━━━  ❖  ━━━ </h1>

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

## ❖ Information

<b></b>

Tilde aims to be starting point for anyone getting started in their self-hosting journey. 
It uses [Pyinfra](https://pyinfra.com/) to configure a new server and deploy commonly used applications
using [Docker](https://www.docker.com/). Please note that Tilde only targets and supports
[Debian](https://www.debian.org/).

<b></b>

<img src="https://github.com/dotzenith/dotzenith/blob/main/assets/tilde/tilde.png" alt="tilde photo">

---

## ❖ Features

<b></b>

- A [Wireguard](https://www.wireguard.com/) tunnel with a user-friendly interface so you can access your services even when you're not home, without exposing them to the internet.
- Dynamic DNS using [DuckDNS](https://www.duckdns.org/) so that wireguard can always connect you to your services
- A [Nextcloud](https://nextcloud.com/) instance for your own cloud storage
- A [Jellyfin](https://jellyfin.org/) instance for media consumption
- [Grafana](https://grafana.com/) with [Prometheus](https://prometheus.io/) for server monitoring
  - Comes with [Node Exporter](https://github.com/prometheus/node_exporter) (System Stats) and [cadvisor](https://github.com/google/cadvisor) (Container Stats) pre-configured. Add any dashboard compatible with them.
- A [Nginx Proxy Manager](https://nginxproxymanager.com/) Instance for reverse proxy and TLS (Configured by the user)

---

## ❖ User Guide

### [tilde.dotzenith.xyz](https://tilde.dotzenith.xyz/)
