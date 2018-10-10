# Ansible module: ansible.module_net_l2_interface


Manage Layer-2 interface on network devices

## Description

This module provides declarative management of Layer-2 interface on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port.']}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'default': 'access', 'choices': ['access', 'trunk']}",
    "name": "{'description': ['Name of the interface excluding any logical unit number.']}",
    "native_vlan": "{'description': ['Native VLAN to be configured in trunk port.']}",
    "state": "{'description': ['State of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trunk_allowed_vlans": "{'description': ["List of allowed VLAN's in a given trunk port."]}",
    "trunk_vlans": "{'description': ['List of VLANs to be configured in trunk port.']}",
}
```

## Examples


``` yaml

- name: configure Layer-2 interface
  net_l2_interface:
    name: gigabitethernet0/0/1
    mode: access
    access_vlan: 30

- name: remove Layer-2 interface configuration
  net_l2_interface:
    name: gigabitethernet0/0/1
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
