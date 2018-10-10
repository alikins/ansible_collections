# Ansible module: ansible.module_slxos_l2_interface


Manage Layer-2 interface on Extreme Networks SLX-OS devices

## Description

This module provides declarative management of Layer-2 interface on Extreme slxos devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port. If C(mode=access), used as the access VLAN ID.']}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'default': 'access', 'choices': ['access', 'trunk']}",
    "name": "{'description': ['Full name of the interface excluding any logical unit number, i.e. Ethernet 0/1.'], 'required': True, 'aliases': ['interface']}",
    "native_vlan": "{'description': ['Native VLAN to be configured in trunk port. If C(mode=trunk), used as the trunk native VLAN ID.']}",
    "state": "{'description': ['Manage the state of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'unconfigured']}",
    "trunk_allowed_vlans": "{'description': ['List of allowed VLANs in a given trunk port. If C(mode=trunk), these are the only VLANs that will be configured on the trunk, i.e. "2-10,15".']}",
    "trunk_vlans": "{'description': ['List of VLANs to be configured in trunk port. If C(mode=trunk), used as the VLAN range to ADD or REMOVE from the trunk.']}",
}
```

## Examples


``` yaml

- name: Ensure Ethernet 0/5 is in its default l2 interface state
  slxos_l2_interface:
    name: Ethernet 0/5
    state: unconfigured

- name: Ensure Ethernet 0/5 is configured for access vlan 20
  slxos_l2_interface:
    name: Ethernet 0/5
    mode: access
    access_vlan: 20

- name: Ensure Ethernet 0/5 only has vlans 5-10 as trunk vlans
  slxos_l2_interface:
    name: Ethernet 0/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 5-10

- name: Ensure Ethernet 0/5 is a trunk port and ensure 2-50 are being tagged (doesn't mean others aren't also being tagged)
  slxos_l2_interface:
    name: Ethernet 0/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 2-50

- name: Ensure these VLANs are not being tagged on the trunk
  slxos_l2_interface:
    name: Ethernet 0/5
    mode: trunk
    trunk_vlans: 51-4094
    state: absent

```

## License

TODO

## Author Information
  - ['Matthew Stone (@bigmstone)']
