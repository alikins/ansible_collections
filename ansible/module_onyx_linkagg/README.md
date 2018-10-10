# Ansible module: ansible.module_onyx_linkagg


Manage link aggregation groups on Mellanox ONYX network devices

## Description

This module provides declarative management of link aggregation groups on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of link aggregation definitions.']}",
    "members": "{'description': ['List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces.'], 'required': True}",
    "mode": "{'description': ['Mode of the link aggregation group. A value of C(on) will enable LACP. C(active) configures the link to actively information about the state of the link, or it can be configured in C(passive) mode ie. send link state information only when received them from another link.'], 'default': True, 'choices': ['on', 'active', 'passive']}",
    "name": "{'description': ['Name of the link aggregation group.'], 'required': True}",
    "purge": "{'description': ['Purge link aggregation groups not defined in the I(aggregate) parameter.'], 'default': False, 'type': 'bool'}",
    "state": "{'description': ['State of the link aggregation group.'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
}
```

## Examples


``` yaml

- name: configure link aggregation group
  onyx_linkagg:
    name: Po1
    members:
      - Eth1/1
      - Eth1/2

- name: remove configuration
  onyx_linkagg:
    name: Po1
    state: absent

- name: Create aggregate of linkagg definitions
  onyx_linkagg:
    aggregate:
        - { name: Po1, members: [Eth1/1] }
        - { name: Po2, members: [Eth1/2] }

- name: Remove aggregate of linkagg definitions
  onyx_linkagg:
    aggregate:
      - name: Po1
      - name: Po2
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
