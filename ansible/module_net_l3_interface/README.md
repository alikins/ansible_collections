# Ansible module: ansible.module_net_l3_interface


Manage L3 interfaces on network devices

## Description

This module provides declarative management of L3 interfaces on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of L3 interfaces definitions']}",
    "ipv4": "{'description': ['IPv4 of the L3 interface.']}",
    "ipv6": "{'description': ['IPv6 of the L3 interface.']}",
    "name": "{'description': ['Name of the L3 interface.']}",
    "purge": "{'description': ['Purge L3 interfaces not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the L3 interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Set eth0 IPv4 address
  net_l3_interface:
    name: eth0
    ipv4: 192.168.0.1/24

- name: Remove eth0 IPv4 address
  net_l3_interface:
    name: eth0
    state: absent

- name: Set IP addresses on aggregate
  net_l3_interface:
    aggregate:
      - { name: eth1, ipv4: 192.168.2.10/24 }
      - { name: eth2, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  net_l3_interface:
    aggregate:
      - { name: eth1, ipv4: 192.168.2.10/24 }
      - { name: eth2, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
