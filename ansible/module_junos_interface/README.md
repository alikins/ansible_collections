# Ansible module: ansible.module_junos_interface


Manage Interface on Juniper JUNOS network devices

## Description

This module provides declarative management of Interfaces on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "duplex": "{'description': ['Interface link status.'], 'default': 'auto', 'choices': ['full', 'half', 'auto']}",
    "enabled": "{'description': ['Configure interface link status.']}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for LLDP neighbor.', 'The following suboptions are available.'], 'suboptions': {'host': {'description': ['LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['LLDP neighbor port to which given interface C(name) is connected.']}}}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['Interface link speed.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) idicates present and operationally up and C(down) indicates present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  junos_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  junos_interface:
    name: ge-0/0/1
    state: absent

- name: make interface down
  junos_interface:
    name: ge-0/0/1
    enabled: False

- name: make interface up
  junos_interface:
    name: ge-0/0/1
    enabled: True

- name: Deactivate interface config
  junos_interface:
    name: ge-0/0/1
    state: present
    active: False

- name: Activate interface config
  net_interface:
    name: ge-0/0/1
    state: present
    active: True

- name: Configure interface speed, mtu, duplex
  junos_interface:
    name: ge-0/0/1
    state: present
    speed: 1g
    mtu: 256
    duplex: full

- name: Create interface using aggregate
  junos_interface:
    aggregate:
      - name: ge-0/0/1
        description: test-interface-1
      - name: ge-0/0/2
        description: test-interface-2
    speed: 1g
    duplex: full
    mtu: 512

- name: Delete interface using aggregate
  junos_interface:
    aggregate:
      - name: ge-0/0/1
      - name: ge-0/0/2
    state: absent

- name: Check intent arguments
  junos_interface:
    name: "{{ name }}"
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbor intent
  junos_interface:
    name: xe-0/1/1
    neighbors:
    - port: Ethernet1/0/1
      host: netdev

- name: Config + intent
  junos_interface:
    name: "{{ name }}"
    enabled: False
    state: down

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
