# Ansible module: ansible.module_grafana_plugin


Manage Grafana plugins via grafana-cli

## Description

Install and remove Grafana plugins.

## Requirements

TODO

## Arguments

``` json
{
    "grafana_plugin_url": "{'description': ['Custom Grafana plugin URL.', 'Requires grafana 4.6.x or later.']}",
    "grafana_plugins_dir": "{'description': ['Directory where Grafana plugin will be installed.']}",
    "grafana_repo": "{'description': ['Grafana repository. If not set, gafana-cli will use the default value C(https://grafana.net/api/plugins).']}",
    "name": "{'description': ['Name of the plugin.'], 'required': True}",
    "state": "{'description': ['Status of the Grafana plugin.', 'If latest is set, the version parameter will be ignored.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "version": "{'description': ['Version of the plugin to install.', 'Default to latest.']}",
}
```

## Examples


``` yaml

---
- name: Install - update Grafana piechart panel plugin
  grafana_plugin:
    name: grafana-piechart-panel
    version: latest
    state: present

```

## License

TODO

## Author Information
  - ['Thierry Sallé (@tsalle)']
