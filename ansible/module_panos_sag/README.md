# Ansible module: ansible.module_panos_sag


Create a static address group

## Description

Create a static address group object in the firewall used for policy rules.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "description": "{'description': ['The purpose / objective of the static Address Group']}",
    "devicegroup": "{'description': ['- The name of the Panorama device group. The group must exist on Panorama. If device group is not defined it is assumed that we are contacting a firewall.\n']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "operation": "{'description': ['The operation to perform Supported values are I(add)/I(list)/I(delete).'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "sag_name": "{'description': ['name of the dynamic address group'], 'required': True}",
    "static_match_filter": "{'description': ['Static filter user by the address group'], 'required': True}",
    "tags": "{'description': ['Tags to be associated with the address group']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: sag
  panos_sag:
    ip_address: "192.168.1.1"
    password: "admin"
    sag_name: "sag-1"
    static_value: ['test-addresses', ]
    description: "A description for the static address group"
    tags: ["tags to be associated with the group", ]

```

## License

TODO

## Author Information
  - ['Vinay Venkataraghavan @vinayvenkat']
