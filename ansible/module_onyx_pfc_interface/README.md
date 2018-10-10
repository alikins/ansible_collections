# Ansible module: ansible.module_onyx_pfc_interface


Manage priority flow control on ONYX network devices

## Description

This module provides declarative management of priority flow control (PFC) on interfaces of Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of interfaces PFC should be configured on.']}",
    "name": "{'description': ['Name of the interface PFC should be configured on.']}",
    "purge": "{'description': ['Purge interfaces not defined in the aggregate parameter.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['State of the PFC configuration.'], 'default': 'enabled', 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: configure PFC
  onyx_pfc_interface:
    name: Eth1/1
    state: enabled

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
