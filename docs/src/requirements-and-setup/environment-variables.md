# ❖ Environment Variables

As the final pre-requisite before we deploy, you'll also need to fill out some environment variables in the [run script](https://github.com/dotzenith/tilde/blob/main/run.sh).

```
# run.sh

export USERNAME=<username>
export HOST=<server-from-your-ssh-config>

export WIREGUARD_PASSWORD=<password-you-want-for-wireguard-ui>
export WIREGUARD_HOST=<your-subdomain.duckdns.org>

# Can be obtained by running `id $user`
export TILDE_UID=<uid-here>
export TILDE_GID=<gid-here>

export TZ=America/New_York
```
> [!NOTE]
> See [TZ Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zoneshttps://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to set your TimeZone properly.
>
> Also don't forget to get rid of the \<\>
