# Ansible module: ansible.module_slxos_linkagg


Manage link aggregation groups on Extreme Networks SLX-OS network devices

## Description

This module provides declarative management of link aggregation groups on Extreme Networks SLX-OS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of link aggregation definitions.']}",
    "group": "{'description': ['Channel-group number for the port-channel Link aggregation group. Range 1-1024.']}",
    "members": "{'description': ['List of members of the link aggregation group.']}",
    "mode": "{'description': ['Mode of the link aggregation group.'], 'choices': ['active', 'on', 'passive']}",
    "purge": "{'description': ['Purge links not defined in the I(aggregate) parameter.'], 'type': 'bool'}",
    "state": "{'description': ['State of the link aggregation group.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: create link aggregation group
  slxos_linkagg:
    group: 10
    state: present

- name: delete link aggregation group
  slxos_linkagg:
    group: 10
    state: absent

- name: set link aggregation group to members
  slxos_linkagg:
    group: 200
    mode: active
    members:
      - Ethernet 0/1
      - Ethernet 0/2

- name: remove link aggregation group from Ethernet 0/1
  slxos_linkagg:
    group: 200
    mode: active
    members:
      - Ethernet 0/1

- name: Create aggregate of linkagg definitions
  slxos_linkagg:
    aggregate:
      - { group: 3, mode: on, members: [Ethernet 0/1] }
      - { group: 100, mode: passive, members: [Ethernet 0/2] }

```

## License

TODO

## Author Information
  - ['Matthew Stone (@bigmstone)']
