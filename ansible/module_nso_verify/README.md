# Ansible module: ansible.module_nso_verify


Verifies Cisco NSO configuration

## Description

This module provides support for verifying Cisco NSO configuration is in compliance with specified values.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ['NSO data in format as C(| display json) converted to YAML. List entries can be annotated with a C(__state) entry. Set to in-sync/deep-in-sync for services to verify service is in sync with the network. Set to absent in list entries to ensure they are deleted if they exist in NSO.\n'], 'required': True}",
    "password": "{'description': ['NSO password'], 'required': True}",
    "timeout": "{'description': ['JSON-RPC request timeout in seconds'], 'default': 300, 'version_added': '2.6'}",
    "url": "{'description': ['NSO JSON-RPC URL, http://localhost:8080/jsonrpc'], 'required': True}",
    "username": "{'description': ['NSO username'], 'required': True}",
}
```

## Examples


``` yaml

- name: Verify interface is up
  nso_config:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    data:
      ncs:devices:
        device:
        - name: ce0
          live-status:
            interfaces:
              interface:
                - name: GigabitEthernet0/12
                - state: Up

```

## License

TODO

## Author Information
  - ['Claes Nästén (@cnasten)']
