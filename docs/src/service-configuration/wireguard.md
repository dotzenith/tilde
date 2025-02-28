# ❖ Wireguard

Tilde uses [wg-easy](https://github.com/wg-easy/wg-easy) to make [Wireguard](https://www.wireguard.com/) VPN access easy.
The password for the UI will be the one set in the [run script](https://github.com/dotzenith/tilde/blob/main/run.sh).
You can add profiles for all of your devices, and access your services from anywhere.

Do note that IP collisions can happen when using Wireguard. This is when your current network's private address space is the same as your home network.

For example, devices in your home network are assigned IP address `192.168.1.0` to `192.168.1.255` and the same is true of the network you are currently connected to.
If you're at a friend's house, you can ask them to change their private address space to be `192.168.2.0` to `192.168.2.255` or something along those lines.
You can also change yours to accomplish the same thing.

This is an oversimplification of how private address spaces are assigned, but illustrates a common problem that I've run into multiple times.
