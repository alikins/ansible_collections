# Ansible module: ansible.module_onyx_vlan


Manage VLANs on Mellanox ONYX network devices

## Description

This module provides declarative management of VLANs on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "name": "{'description': ['Name of the VLAN.']}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['ID of the VLAN.']}",
}
```

## Examples


``` yaml

- name: configure VLAN ID and name
  onyx_vlan:
    vlan_id: 20
    name: test-vlan

- name: remove configuration
  onyx_vlan:
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd) Alex Tabachnik (@atabachnik)']
