# Ansible module: ansible.module_onyx_interface


Manage Interfaces on Mellanox ONYX network devices

## Description

This module provides declarative management of Interfaces on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "duplex": "{'description': ['Interface link status'], 'default': 'auto', 'choices': ['full', 'half', 'auto']}",
    "enabled": "{'description': ['Interface link status.'], 'type': 'bool'}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "purge": "{'description': ['Purge Interfaces not defined in the aggregate parameter. This applies only for logical interface.'], 'default': False, 'type': 'bool'}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['Interface link speed.'], 'choices': ['1G', '10G', '25G', '40G', '50G', '56G', '100G']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  onyx_interface:
      name: Eth1/2
      description: test-interface
      speed: 100 GB
      mtu: 512

- name: make interface up
  onyx_interface:
    name: Eth1/2
    enabled: True

- name: make interface down
  onyx_interface:
    name: Eth1/2
    enabled: False

- name: Check intent arguments
  onyx_interface:
    name: Eth1/2
    state: up

- name: Config + intent
  onyx_interface:
    name: Eth1/2
    enabled: False
    state: down

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
