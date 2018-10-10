# Ansible module: ansible.module_onyx_l2_interface


Manage Layer-2 interface on Mellanox ONYX network devices

## Description

This module provides declarative management of Layer-2 interface on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port.']}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'default': 'access', 'choices': ['access', 'trunk', 'hybrid']}",
    "name": "{'description': ['Name of the interface.']}",
    "state": "{'description': ['State of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trunk_allowed_vlans": "{'description': ['List of allowed VLANs in a given trunk port.']}",
}
```

## Examples


``` yaml

- name: configure Layer-2 interface
  onyx_l2_interface:
    name: Eth1/1
    mode: access
    access_vlan: 30

- name: remove Layer-2 interface configuration
  onyx_l2_interface:
    name: Eth1/1
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
