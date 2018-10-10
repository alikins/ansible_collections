# Ansible module: ansible.module_nso_show


Displays data from Cisco NSO

## Description

This module provides support for displaying data from Cisco NSO.

## Requirements

TODO

## Arguments

``` json
{
    "operational": "{'description': ['Controls whether or not operational data is included in the result.\n'], 'type': 'bool', 'default': False}",
    "password": "{'description': ['NSO password'], 'required': True}",
    "path": "{'description': ['Path to NSO data.'], 'required': True}",
    "timeout": "{'description': ['JSON-RPC request timeout in seconds'], 'default': 300, 'version_added': '2.6'}",
    "url": "{'description': ['NSO JSON-RPC URL, http://localhost:8080/jsonrpc'], 'required': True}",
    "username": "{'description': ['NSO username'], 'required': True}",
}
```

## Examples


``` yaml

- name: Show devices including operational data
  nso_show:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    path: /ncs:devices/device
    operational: true

```

## License

TODO

## Author Information
  - ['Claes Nästén (@cnasten)']
