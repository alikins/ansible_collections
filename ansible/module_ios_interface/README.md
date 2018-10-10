# Ansible module: ansible.module_ios_interface


Manage Interface on Cisco IOS network devices

## Description

This module provides declarative management of Interfaces on Cisco IOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "duplex": "{'description': ['Interface link status'], 'default': 'auto', 'choices': ['full', 'half', 'auto']}",
    "enabled": "{'description': ['Interface link status.']}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for CDP/LLDP neighbor.', 'The following suboptions are available.'], 'suboptions': {'host': {'description': ['CDP/LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['CDP/LLDP neighbor port to which given interface C(name) is connected.']}}}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['Interface link speed.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  ios_interface:
      name: GigabitEthernet0/2
      description: test-interface
      speed: 100
      duplex: half
      mtu: 512

- name: remove interface
  ios_interface:
    name: Loopback9
    state: absent

- name: make interface up
  ios_interface:
    name: GigabitEthernet0/2
    enabled: True

- name: make interface down
  ios_interface:
    name: GigabitEthernet0/2
    enabled: False

- name: Check intent arguments
  ios_interface:
    name: GigabitEthernet0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  ios_interface:
    name: Gi0/0
    neighbors:
    - port: eth0
      host: netdev

- name: Config + intent
  ios_interface:
    name: GigabitEthernet0/2
    enabled: False
    state: down

- name: Add interface using aggregate
  ios_interface:
    aggregate:
    - { name: GigabitEthernet0/1, mtu: 256, description: test-interface-1 }
    - { name: GigabitEthernet0/2, mtu: 516, description: test-interface-2 }
    duplex: full
    speed: 100
    state: present

- name: Delete interface using aggregate
  ios_interface:
    aggregate:
    - name: Loopback9
    - name: Loopback10
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
