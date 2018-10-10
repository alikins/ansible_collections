# Ansible module: ansible.module_slxos_vlan


Manage VLANs on Extreme Networks SLX-OS network devices

## Description

This module provides declarative management of VLANs on Extreme SLX-OS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "delay": "{'description': ['Delay the play should wait to check for declarative intent params values.'], 'default': 10}",
    "interfaces": "{'description': ['List of interfaces that should be associated to the VLAN.'], 'required': True}",
    "name": "{'description': ['Name of the VLAN.']}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['ID of the VLAN. Range 1-4094.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create vlan
  slxos_vlan:
    vlan_id: 100
    name: test-vlan
    state: present
- name: Add interfaces to VLAN
  slxos_vlan:
    vlan_id: 100
    interfaces:
      - Ethernet 0/1
      - Ethernet 0/2
- name: Delete vlan
  slxos_vlan:
    vlan_id: 100
    state: absent

```

## License

TODO

## Author Information
  - ['Lindsay Hill (@lindsayhill)']
