# Ansible module: ansible.module_onyx_l3_interface


Manage L3 interfaces on Mellanox ONYX network devices

## Description

This module provides declarative management of L3 interfaces on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of L3 interfaces definitions']}",
    "ipv4": "{'description': ['IPv4 of the L3 interface.']}",
    "ipv6": "{'description': ['IPv6 of the L3 interface (not supported for now).']}",
    "name": "{'description': ['Name of the L3 interface.']}",
    "purge": "{'description': ['Purge L3 interfaces not defined in the I(aggregate) parameter.'], 'default': False, 'type': 'bool'}",
    "state": "{'description': ['State of the L3 interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Set Eth1/1 IPv4 address
  onyx_l3_interface:
    name: Eth1/1
    ipv4: 192.168.0.1/24

- name: Remove Eth1/1 IPv4 address
  onyx_l3_interface:
    name: Eth1/1
    state: absent

- name: Set IP addresses on aggregate
  onyx_l3_interface:
    aggregate:
      - { name: Eth1/1, ipv4: 192.168.2.10/24 }
      - { name: Eth1/2, ipv4: 192.168.3.10/24 }

- name: Remove IP addresses on aggregate
  onyx_l3_interface:
    aggregate:
      - { name: Eth1/1, ipv4: 192.168.2.10/24 }
      - { name: Eth1/2, ipv4: 192.168.3.10/24 }
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
