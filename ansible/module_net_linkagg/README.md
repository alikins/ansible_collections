# Ansible module: ansible.module_net_linkagg


Manage link aggregation groups on network devices

## Description

This module provides declarative management of link aggregation groups on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of link aggregation definitions.']}",
    "members": "{'description': ['List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces.'], 'required': True}",
    "min_links": "{'description': ['Minimum members that should be up before bringing up the link aggregation group.']}",
    "mode": "{'description': ['Mode of the link aggregation group. A value of C(on) will enable LACP. C(active) configures the link to actively information about the state of the link, or it can be configured in C(passive) mode ie. send link state information only when received them from another link.'], 'default': True, 'choices': ['on', 'active', 'passive']}",
    "name": "{'description': ['Name of the link aggregation group.'], 'required': True}",
    "purge": "{'description': ['Purge link aggregation groups not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the link aggregation group.'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
}
```

## Examples


``` yaml

- name: configure link aggregation group
  net_linkagg:
    name: bond0
    members:
      - eth0
      - eth1

- name: remove configuration
  net_linkagg:
    name: bond0
    state: absent

- name: Create aggregate of linkagg definitions
  net_linkagg:
    aggregate:
        - { name: bond0, members: [eth1] }
        - { name: bond1, members: [eth2] }

- name: Remove aggregate of linkagg definitions
  net_linkagg:
    aggregate:
      - name: bond0
      - name: bond1
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
