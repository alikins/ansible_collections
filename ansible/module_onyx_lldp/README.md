# Ansible module: ansible.module_onyx_lldp


Manage LLDP configuration on Mellanox ONYX network devices

## Description

This module provides declarative management of LLDP service configuration on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "state": "{'description': ['State of the LLDP protocol configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Enable LLDP protocol
  onyx_lldp:
    state: present

- name: Disable LLDP protocol
  onyx_lldp:
    state: lldp

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
