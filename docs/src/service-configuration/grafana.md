# ❖ Grafana

Tilde configures [Grafana](https://grafana.com/) with [Prometheus](https://prometheus.io/) for server monitoring.

In short, Prometheus scrapes a set of data sources and serves that data through Prometheus Query Language. Grafana then takes that data, and displays them to you in a beautiful UI.

The following Prometheus data sources come pre-configured with Tilde:
  - [Node Exporter](https://github.com/prometheus/node_exporter): System Stats 
  - [cadvisor](https://github.com/google/cadvisor): Container Stats

You can then use pre-made [Grafana Dashboards](https://grafana.com/grafana/dashboards/) to visualize that data.
For example, I like using [Node Exporter Full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/) as one of my dashboards.
This relies on Node Exporter being set up for Prometheus.
