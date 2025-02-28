# ❖ Server Configuration and SSH

## ❖ Operating System

The target server should be running Debian 12 or above.
The [Install Images](https://www.debian.org/distrib/) provided by Debian include a Graphical Installer,
and a TUI installer as well. Feel free to use whichever one you are more comfortable with.

## ❖ SSH

If you don't have ssh keys set up, please take a look at the 
[Github Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
on the topic.

Your ssh config should should look something like this:
```
# ~/.ssh/config

host <homeserver>
  HostName <internal-ip-of-server> 
  user <non-root-user>

host *
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```
> [!NOTE]  
> Replace the values wrapped in \<\> with the appropriate values for your server

The password authentication can be skipped by adding your public key to your server. You can do so manually
by placing it in the `~/.ssh/authorized_keys` file on your server. Or you can use the following command to do it
for you:

```bash
ssh-copy-id <homeserver>
```

## ❖ Sudo User

For the sake of security and to generally make our lives easier, we will not be logging into the server as `root`.
The Debian Installer should have guided you to create another user. But just in case it didn't, if you're already
logged in as root, you can create a new user by running the following command:

```
adduser <username>
```

Once we have another user, we need to give that user `sudo` privileges. On Debian, `sudo` is not installed by
default. We will run the following commands to install `sudo` and give our user the proper permissions.

```bash
apt install sudo                  # Install sudo
usermod -aG sudo <username>       # Add sudo permissions for our user
```

## ❖ Laptop Configuration (Optional)

If you are using an old laptop as your server, we want to make sure that the laptop does not go to sleep
when the lid is closed. We can do so by following the steps below.

Open `/etc/systemd/logind.conf` in your preferred text editor
```bash
sudo vim /etc/systemd/logind.conf
```

Uncomment and set the `HandleLidSwitch` option to ignore
```
HandleLidSwitch=ignore
```

Restart the systemd daemon:
```bash
sudo systemctl restart systemd-logind
```
> [!WARNING] 
> This will log you out

Taken from
[ask Ubuntu](https://askubuntu.com/questions/15520/how-can-i-tell-ubuntu-to-do-nothing-when-i-close-my-laptop-lid)
