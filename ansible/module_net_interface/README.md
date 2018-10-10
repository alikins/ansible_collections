# Ansible module: ansible.module_net_interface


Manage Interface on network devices

## Description

This module provides declarative management of Interfaces on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "duplex": "{'description': ['Interface link status'], 'default': 'auto', 'choices': ['full', 'half', 'auto']}",
    "enabled": "{'description': ['Configure interface link status.']}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "purge": "{'description': ['Purge Interfaces not defined in the aggregate parameter. This applies only for logical interface.'], 'default': False}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['Interface link speed.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) indicates present and operationally up and C(down) indicates present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  net_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  net_interface:
    name: ge-0/0/1
    state: absent

- name: make interface up
  net_interface:
    name: ge-0/0/1
    description: test-interface
    enabled: True

- name: make interface down
  net_interface:
    name: ge-0/0/1
    description: test-interface
    enabled: False

- name: Create interface using aggregate
  net_interface:
    aggregate:
      - { name: ge-0/0/1, description: test-interface-1 }
      - { name: ge-0/0/2, description: test-interface-2 }
    speed: 1g
    duplex: full
    mtu: 512

- name: Delete interface using aggregate
  junos_interface:
    aggregate:
      - { name: ge-0/0/1 }
      - { name: ge-0/0/2 }
    state: absent

- name: Check intent arguments
  net_interface:
    name: fxp0
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Config + intent
  net_interface:
    name: fxp0
    enabled: False
    state: down

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
