# Ansible module: ansible.module_onyx_lldp_interface


Manage LLDP interfaces configuration on Mellanox ONYX network devices

## Description

This module provides declarative management of LLDP interfaces configuration on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of interfaces LLDP should be configured on.']}",
    "name": "{'description': ['Name of the interface LLDP should be configured on.']}",
    "purge": "{'description': ['Purge interfaces not defined in the aggregate parameter.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['State of the LLDP configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Configure LLDP on specific interfaces
  onyx_lldp_interface:
    name: Eth1/1
    state: present

- name: Disable LLDP on specific interfaces
  onyx_lldp_interface:
    name: Eth1/1
    state: disabled

- name: Enable LLDP on specific interfaces
  onyx_lldp_interface:
    name: Eth1/1
    state: enabled

- name: Delete LLDP on specific interfaces
  onyx_lldp_interface:
    name: Eth1/1
    state: absent

- name: Create aggregate of LLDP interface configurations
  onyx_lldp_interface:
    aggregate:
    - { name: Eth1/1 }
    - { name: Eth1/2 }
    state: present

- name: Delete aggregate of LLDP interface configurations
  onyx_lldp_interface:
    aggregate:
    - { name: Eth1/1 }
    - { name: Eth1/2 }
    state: absent

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
