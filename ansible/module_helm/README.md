# Ansible module: ansible.module_helm


Manages Kubernetes packages with the Helm package manager

## Description

Install, upgrade, delete and list packages with the Helm package manager.

## Requirements

TODO

## Arguments

``` json
{
    "chart": "{'description': ['A map describing the chart to install. See examples for available options.\n'], 'default': {}}",
    "disable_hooks": "{'description': ['Whether to disable hooks during the uninstall process.'], 'type': 'bool', 'default': False}",
    "host": "{'description': ["Tiller's server host."], 'default': 'localhost'}",
    "name": "{'description': ['Release name to manage.']}",
    "namespace": "{'description': ['Kubernetes namespace where the chart should be installed.'], 'default': 'default'}",
    "port": "{'description': ["Tiller's server port."], 'default': 44134}",
    "state": "{'description': ['Whether to install C(present), remove C(absent), or purge C(purged) a package.'], 'choices': ['absent', 'purged', 'present'], 'default': 'present'}",
    "values": "{'description': ['A map of value options for the chart.'], 'default': {}}",
}
```

## Examples


``` yaml

- name: Install helm chart
  helm:
    host: localhost
    chart:
      name: memcached
      version: 0.4.0
      source:
        type: repo
        location: https://kubernetes-charts.storage.googleapis.com
    state: present
    name: my-memcached
    namespace: default

- name: Uninstall helm chart
  helm:
    host: localhost
    state: absent
    name: my-memcached

```

## License

TODO

## Author Information
  - ['Flavio Percoco (flaper87)']
