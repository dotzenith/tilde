"""
A task file to deploy Grafana With Prometheus

Uses a docker-compose file to spin up the stack with Grafana, Prometheus, Node_Exporter, and Cadvisor
"""

from pyinfra.operations import server, files
from io import StringIO

from tilde.vars import USERNAME, HOME

files.directory(
    name="Make Grafana/Prometheus compose directory",
    path=f"{HOME}/tilde/promgraf",
    present=True,
    user=USERNAME,
)

files.template(
    name="Copy Grafana/Prometheus compose file",
    src="templates/promgraf.yml.j2",
    dest=f"{HOME}/tilde/promgraf/docker-compose.yml",
    prometheus_config = f"{HOME}/container-data/prometheus/prometheus.yml",
    grafana_datasources = f"{HOME}/container-data/grafana/datasources",
)

files.directory(
    name="Make Prometheus config directory",
    path=f"{HOME}/container-data/prometheus",
    present=True,
    user=USERNAME,
)
# Prometheus config
prometheus_config = """
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    static_configs:
      - targets: ['node_exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8081']
"""

files.put(
    name="Add Prometheus config file",
    src=StringIO(prometheus_config),
    dest=f'{HOME}/container-data/prometheus/prometheus.yml',
    user=USERNAME,
    create_remote_dir=True
)

files.directory(
    name="Make Grafana provisioning/datasources directory",
    path=f"{HOME}/container-data/grafana/datasources",
    present=True,
    user=USERNAME,
)

# Grafana file for prometheus datasource configuration
prometheus_datasource = """
datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    isDefault: true
    editable: false
"""

files.put(
    name="Add Prometheus as Grafana datasource",
    src=StringIO(prometheus_datasource),
    dest=f'{HOME}/container-data/grafana/datasources/prometheus.yml',
    user=USERNAME,
    create_remote_dir=True
)

server.shell(
    name="Deploy Grafana/Prometheus stack",
    commands=[f"cd {HOME}/tilde/promgraf && docker compose up -d"],
    _sudo=True,  
)
