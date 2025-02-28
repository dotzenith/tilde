# ❖ Port Forwarding

When accessing our services away from home, we'll be using a Wireguard tunnel to VPN into our home network.
For this to work however, we need to set up Port Forwarding.

For some background, Tilde configures Wireguard to run on the default port `51820`.
Let's assume that your Server's internal IP is `192.168.1.30`.
We need to tell our Router to send any outside traffic on port `51820` to `192.168.1.30:51820`.

Setting up port forwarding is different from one Router to another. Please look up how to do so for your Router.

Here are some links to point you in the right direction:

- [Netgear](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router)
- [TP-Link](https://www.tp-link.com/us/support/faq/1379/)
- [Asus](https://www.asus.com/us/support/faq/1037906/)
- [OpenWRT](https://openwrt.org/docs/guide-user/firewall/fw3_configurations/fw3_nat)
