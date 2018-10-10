# Ansible module: ansible.module_onyx_mlag_vip


Configures MLAG VIP on Mellanox ONYX network devices

## Description

This module provides declarative management of MLAG virtual IPs on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "delay": "{'description': ['Delay interval, in seconds, waiting for the changes on mlag VIP to take effect.'], 'default': 12}",
    "group_name": "{'description': ['MLAG group name. Required if I(state=present).']}",
    "ipaddress": "{'description': ['Virtual IP address of the MLAG. Required if I(state=present).']}",
    "mac_address": "{'description': ['MLAG system MAC address. Required if I(state=present).']}",
    "state": "{'description': ['MLAG VIP state.'], 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure mlag-vip
  onyx_mlag_vip:
    ipaddress: 50.3.3.1/24
    group_name: ansible-test-group
    mac_address: 00:11:12:23:34:45

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
