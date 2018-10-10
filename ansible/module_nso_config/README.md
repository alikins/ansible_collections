# Ansible module: ansible.module_nso_config


Manage Cisco NSO configuration and service synchronization

## Description

This module provides support for managing configuration in Cisco NSO and can also ensure services are in sync.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ['NSO data in format as | display json converted to YAML. List entries can be annotated with a __state entry. Set to in-sync/deep-in-sync for services to verify service is in sync with the network. Set to absent in list entries to ensure they are deleted if they exist in NSO.\n'], 'required': True}",
    "password": "{'description': ['NSO password'], 'required': True}",
    "timeout": "{'description': ['JSON-RPC request timeout in seconds'], 'default': 300, 'version_added': '2.6'}",
    "url": "{'description': ['NSO JSON-RPC URL, http://localhost:8080/jsonrpc'], 'required': True}",
    "username": "{'description': ['NSO username'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create L3VPN
  nso_config:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    data:
      l3vpn:vpn:
        l3vpn:
        - name: company
          route-distinguisher: 999
          endpoint:
          - id: branch-office1
            ce-device: ce6
            ce-interface: GigabitEthernet0/12
            ip-network: 10.10.1.0/24
            bandwidth: 12000000
            as-number: 65101
          - id: branch-office2
            ce-device: ce1
            ce-interface: GigabitEthernet0/11
            ip-network: 10.7.7.0/24
            bandwidth: 6000000
            as-number: 65102
          - id: branch-office3
            __state: absent
        __state: in-sync

```

## License

TODO

## Author Information
  - ['Claes Nästén (@cnasten)']
