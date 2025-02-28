# ❖ Nginx Proxy Manager

[Nginx Proxy Manager](https://nginxproxymanager.com/) is a fancy frontend for [Nginx](https://nginx.org/).
I'll be calling it NPM from this point forward, and you can expect to see this abbreviation pop up in self hosting communities as well.
If you own a domain, you can use NPM to set up a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) for your services.
This way, you can access jellyfin at `jellyfin.your-domain.com` instead of `192.168.1.30:8096`.

The first time login credentials for NPM are as follows:
```plaintext
Email:    admin@example.com
Password: changeme
```

You can also use NPM to set up [TLS/SSL](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) for your services. 
This will make your browser stop complaining about an insecure connection and let you access your services over HTTPS.

I won't go over how to do that here, but I will link this incredibly helpful [Wolfgang's Channel Video](https://www.youtube.com/watch?v=qlcVx-k-02E) on the topic.
