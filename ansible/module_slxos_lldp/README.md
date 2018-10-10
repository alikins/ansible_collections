# Ansible module: ansible.module_slxos_lldp


Manage LLDP configuration on Extreme Networks SLX-OS network devices

## Description

This module provides declarative management of LLDP service on Extreme SLX-OS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "state": "{'description': ['State of the LLDP configuration. If value is I(present) lldp will be enabled else if it is I(absent) it will be disabled.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Enable LLDP service
  slxos_lldp:
    state: present

- name: Disable LLDP service
  slxos_lldp:
    state: absent

```

## License

TODO

## Author Information
  - ['Matthew Stone (@bigmstone)']
