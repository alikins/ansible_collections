# Ansible module: ansible.module_infinity


manage Infinity IPAM using Rest API

## Description

Manage Infinity IPAM using REST API

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Action to perform'], 'required': True, 'choices': ['reserve_next_available_ip', 'release_ip', 'delete_network', 'add_network', 'reserve_network', 'release_network', 'get_network_id']}",
    "ip_address": "{'description': ['IP Address for a reservation or a release'], 'default': ''}",
    "network_address": "{'description': ['Network address with CIDR format (e.g., 192.168.310.0)'], 'required': False, 'default': ''}",
    "network_family": "{'description': ['Network family defined by Infinity, e.g. IPv4, IPv6 and Dual stack'], 'choices': [4, 6, 'dual'], 'default': '4'}",
    "network_id": "{'description': ['Network ID'], 'default': ''}",
    "network_location": "{'description': ['the parent network id for a given network'], 'default': -1}",
    "network_name": "{'description': ['The name of a network'], 'default': ''}",
    "network_size": "{'description': ['Network bitmask (e.g. 255.255.255.220) or CIDR format (e.g., /26)'], 'default': ''}",
    "network_type": "{'description': ['Network type defined by Infinity'], 'choices': ['lan', 'shared_lan', 'supernet'], 'default': 'lan'}",
    "password": "{'description': ['Infinity password'], 'required': True}",
    "server_ip": "{'description': ['Infinity server_ip with IP address'], 'required': True}",
    "username": "{'description': ['Username to access Infinity', 'The user must have Rest API privileges'], 'required': True}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  connection: local
  strategy: debug
  tasks:
    - name: Reserve network into Infinity IPAM
      infinity:
        server_ip: "80.75.107.12"
        username: "username"
        password: "password"
        action: "reserve_network"
        network_name: "reserve_new_ansible_network"
        network_family: "4"
        network_type: 'lan'
        network_id: "1201"
        network_size: "/28"
      register: infinity


```

## License

TODO

## Author Information
  - ['Meirong Liu']
