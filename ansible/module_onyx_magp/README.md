# Ansible module: ansible.module_onyx_magp


Manage MAGP protocol on Mellanox ONYX network devices

## Description

This module provides declarative management of MAGP protocol on vlan interface of Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "interface": "{'description': ['VLAN Interface name.'], 'required': True}",
    "magp_id": "{'description': ['MAGP instance number 1-255'], 'required': True}",
    "router_ip": "{'description': ['MAGP router IP address.']}",
    "router_mac": "{'description': ['MAGP router MAC address.']}",
    "state": "{'description': ['MAGP state.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: run add vlan interface with magp
  onyx_magp:
    magp_id: 103
    router_ip: 192.168.8.2
    router_mac: AA:1B:2C:3D:4E:5F
    interface: Vlan 1002

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
