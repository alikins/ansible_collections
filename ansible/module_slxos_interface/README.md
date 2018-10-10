# Ansible module: ansible.module_slxos_interface


Manage Interfaces on Extreme SLX-OS network devices

## Description

This module provides declarative management of Interfaces on Extreme SLX-OS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "enabled": "{'description': ['Interface link status.'], 'default': True, 'type': 'bool'}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for LLDP neighbor.', 'The following suboptions are available.'], 'suboptions': {'host': {'description': ['LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['LLDP neighbor port to which given interface C(name) is connected.']}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).']}",
    "speed": "{'description': ['Interface link speed.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).']}",
}
```

## Examples


``` yaml

- name: configure interface
  slxos_interface:
      name: Ethernet 0/2
      description: test-interface
      speed: 1000
      mtu: 9216

- name: remove interface
  slxos_interface:
    name: Loopback 9
    state: absent

- name: make interface up
  slxos_interface:
    name: Ethernet 0/2
    enabled: True

- name: make interface down
  slxos_interface:
    name: Ethernet 0/2
    enabled: False

- name: Check intent arguments
  slxos_interface:
    name: Ethernet 0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  slxos_interface:
    name: Ethernet 0/41
    neighbors:
    - port: Ethernet 0/41
      host: SLX

- name: Config + intent
  slxos_interface:
    name: Ethernet 0/2
    enabled: False
    state: down

- name: Add interface using aggregate
  slxos_interface:
    aggregate:
    - { name: Ethernet 0/1, mtu: 1548, description: test-interface-1 }
    - { name: Ethernet 0/2, mtu: 1548, description: test-interface-2 }
    speed: 10000
    state: present

- name: Delete interface using aggregate
  slxos_interface:
    aggregate:
    - name: Loopback 9
    - name: Loopback 10
    state: absent

```

## License

TODO

## Author Information
  - ['Lindsay Hill (@LindsayHill)']
