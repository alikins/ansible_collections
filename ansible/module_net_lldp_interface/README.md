# Ansible module: ansible.module_net_lldp_interface


Manage LLDP interfaces configuration on network devices

## Description

This module provides declarative management of LLDP interfaces configuration on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of interfaces LLDP should be configured on.']}",
    "name": "{'description': ['Name of the interface LLDP should be configured on.']}",
    "purge": "{'description': ['Purge interfaces not defined in the aggregate parameter.'], 'default': False}",
    "state": "{'description': ['State of the LLDP configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Configure LLDP on specific interfaces
  net_lldp_interface:
    name: eth1
    state: present

- name: Disable LLDP on specific interfaces
  net_lldp_interface:
    name: eth1
    state: disabled

- name: Enable LLDP on specific interfaces
  net_lldp_interface:
    name: eth1
    state: enabled

- name: Delete LLDP on specific interfaces
  net_lldp_interface:
    name: eth1
    state: absent

- name: Create aggregate of LLDP interface configurations
  net_lldp_interface:
    aggregate:
    - { name: eth1 }
    - { name: eth2 }
    state: present

- name: Delete aggregate of LLDP interface configurations
  net_lldp_interface:
    aggregate:
    - { name: eth1 }
    - { name: eth2 }
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
