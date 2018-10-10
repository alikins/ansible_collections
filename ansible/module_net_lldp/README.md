# Ansible module: ansible.module_net_lldp


Manage LLDP service configuration on network devices

## Description

This module provides declarative management of LLDP service configuration on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "state": "{'description': ['State of the LLDP service configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Enable LLDP service
  net_lldp:
    state: present

- name: Disable LLDP service
  net_lldp:
    state: lldp

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
