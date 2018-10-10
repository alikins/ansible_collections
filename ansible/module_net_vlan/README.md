# Ansible module: ansible.module_net_vlan


Manage VLANs on network devices

## Description

This module provides declarative management of VLANs on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "interfaces": "{'description': ['List of interfaces the VLAN should be configured on.']}",
    "name": "{'description': ['Name of the VLAN.']}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'active', 'suspend']}",
    "vlan_id": "{'description': ['ID of the VLAN.']}",
}
```

## Examples


``` yaml

- name: configure VLAN ID and name
  net_vlan:
    vlan_id: 20
    name: test-vlan

- name: remove configuration
  net_vlan:
    state: absent

- name: configure VLAN state
  net_vlan:
    vlan_id:
    state: suspend


```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
