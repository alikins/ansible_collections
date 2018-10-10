# Ansible module: ansible.module_onyx_mlag_ipl


Manage IPL (inter-peer link) on Mellanox ONYX network devices

## Description

This module provides declarative management of IPL (inter-peer link) management on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the interface (port-channel) IPL should be configured on.'], 'required': True}",
    "peer_address": "{'description': ['IPL peer IP address.']}",
    "state": "{'description': ['IPL state.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_interface": "{'description': ['Name of the IPL vlan interface.']}",
}
```

## Examples


``` yaml

- name: run configure ipl
  onyx_mlag_ipl:
    name: Po1
    vlan_interface: Vlan 322
    state: present
    peer_address: 192.168.7.1

- name: run remove ipl
  onyx_mlag_ipl:
    name: Po1
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
