# ❖ Dynamic DNS

## ❖ Overview

Unless you pay for a static IP, your ISP is free to change your public IP whenever they want.
This is usually not a problem, but it is for us.
We need to make sure that Wireguard can find our home's public IP at all times.

This is where [Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/) will come to our rescue.

Tilde uses [ZenDNS](https://github.com/dotzenith/ZenDNS) to periodically update the DNS records. While this guide assumes that [DuckDNS](https://www.duckdns.org/) will be used,
ZenDNS also works with [Cloudflare](www.cloudflare.com) and [Namecheap](https://www.namecheap.com/). 
Please read the docs for ZenDNS to configure what works best for you.

It's worth mentioning that I am the author of ZenDNS as well. I wrote it because updating DNS entries through API calls is actually pretty easy.
Other tools always seemed more complicated than they had to be. With that said, that's just my experience. If ZenDNS doesn't work well for you
please feel free to switch to a Dynamic DNS client like [inadyn](https://github.com/troglobit/inadyn) or [ddclient](https://ddclient.net/).
You can even write your own!

## ❖ Example

Assuming you're using [DuckDNS](https://www.duckdns.org/):

- Sign up for an account
- Pick a new subdomain on the website and click `add domain`
- Copy the `token` from the website as well

Fill out [src/tilde/templates/zendns.json.j2](https://github.com/dotzenith/tilde/blob/main/src/tilde/templates/zendns.json.j2). It should look something like:
```json
{
    "providers": [
        {
            "type": "duckdns",
            "token": "your-token",
            "domain": "your-hostname.duckdns.org"
        }
    ]
}
```

If you're not using DuckDNS, look at the docs for [ZenDNS](https://github.com/dotzenith/ZenDNS) and replace the contents of
[src/tilde/templates/zendns.json.j2](https://github.com/dotzenith/tilde/blob/main/src/tilde/templates/zendns.json.j2)
with configuration for your chosen provider.
