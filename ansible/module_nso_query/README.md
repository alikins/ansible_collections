# Ansible module: ansible.module_nso_query


Query data from Cisco NSO

## Description

This module provides support for querying data from Cisco NSO using XPath.

## Requirements

TODO

## Arguments

``` json
{
    "fields": "{'description': ['List of fields to select from matching nodes.\n'], 'required': True}",
    "password": "{'description': ['NSO password'], 'required': True}",
    "timeout": "{'description': ['JSON-RPC request timeout in seconds'], 'default': 300, 'version_added': '2.6'}",
    "url": "{'description': ['NSO JSON-RPC URL, http://localhost:8080/jsonrpc'], 'required': True}",
    "username": "{'description': ['NSO username'], 'required': True}",
    "xpath": "{'description': ['XPath selection relative to the root.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Select device name and description
  nso_query:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    xpath: /ncs:devices/device
    fields:
    - name
    - description

```

## License

TODO

## Author Information
  - ['Claes Nästén (@cnasten)']
