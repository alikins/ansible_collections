# Ansible module: ansible.module_slxos_l3_interface


Manage L3 interfaces on Extreme Networks SLX-OS network devices

## Description

This module provides declarative management of L3 interfaces on slxos network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of L3 interfaces definitions. Each of the entry in aggregate list should define name of interface C(name) and a optional C(ipv4) or C(ipv6) address.']}",
    "ipv4": "{'description': ['IPv4 address to be set for the L3 interface mentioned in I(name) option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24']}",
    "ipv6": "{'description': ['IPv6 address to be set for the L3 interface mentioned in I(name) option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64']}",
    "name": "{'description': ['Name of the L3 interface to be configured eg. Ethernet 0/2']}",
    "state": "{'description': ['State of the L3 interface configuration. It indicates if the configuration should be present or absent on remote device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Remove Ethernet 0/3 IPv4 and IPv6 address
  slxos_l3_interface:
    name: Ethernet 0/3
    state: absent

- name: Set Ethernet 0/3 IPv4 address
  slxos_l3_interface:
    name: Ethernet 0/3
    ipv4: 192.168.0.1/24

- name: Set Ethernet 0/3 IPv6 address
  slxos_l3_interface:
    name: Ethernet 0/3
    ipv6: "fd5d:12c9:2201:1::1/64"

- name: Set IP addresses on aggregate
  slxos_l3_interface:
    aggregate:
      - { name: Ethernet 0/3, ipv4: 192.168.2.10/24 }
      - { name: Ethernet 0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  slxos_l3_interface:
    aggregate:
      - { name: Ethernet 0/3, ipv4: 192.168.2.10/24 }
      - { name: Ethernet 0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent

```

## License

TODO

## Author Information
  - ['Matthew Stone (@bigmstone)']
