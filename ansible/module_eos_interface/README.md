# Ansible module: ansible.module_eos_interface


Manage Interface on Arista EOS network devices

## Description

This module provides declarative management of Interfaces on Arista EOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions. Each of the entry in aggregate list should define name of interface C(name) and other options as required.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface upto 240 characters.']}",
    "enabled": "{'description': ['Interface link status. If the value is I(True) the interface state will be enabled, else if value is I(False) interface will be in disable (shutdown) state.'], 'default': True}",
    "mtu": "{'description': ['Set maximum transmission unit size in bytes of transmit packet for the interface given in C(name) option.']}",
    "name": "{'description': ['Name of the Interface to be configured on remote device. The name of interface should be in expanded format and not abbreviated.'], 'required': True}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for LLDP neighbor.', 'The following suboptions are available.'], 'suboptions': {'host': {'description': ['LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['LLDP neighbor port to which given interface C(name) is connected.']}}}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(eapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(eapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['eapi', 'cli'], 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=eapi).  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool', 'default': 'yes'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps) for the interface given in C(name) option.', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['This option configures autoneg and speed/duplex/flowcontrol for the interface given in C(name) option.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps) for the interface given in C(name) option.', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  eos_interface:
      name: ethernet1
      description: test-interface
      speed: 100full
      mtu: 512

- name: remove interface
  eos_interface:
    name: ethernet1
    state: absent

- name: make interface up
  eos_interface:
    name: ethernet1
    enabled: True

- name: make interface down
  eos_interface:
    name: ethernet1
    enabled: False

- name: Check intent arguments
  eos_interface:
    name: ethernet1
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  eos_interface:
    name: ethernet1
    neighbors:
    - port: eth0
      host: netdev

- name: Configure interface in disabled state and check if the operational state is disabled or not
  eos_interface:
    name: ethernet1
    enabled: False
    state: down

- name: Add interface using aggregate
  eos_interface:
    aggregate:
    - { name: ethernet1, mtu: 256, description: test-interface-1 }
    - { name: ethernet2, mtu: 516, description: test-interface-2 }
    speed: 100full
    state: present

- name: Delete interface using aggregate
  eos_interface:
    aggregate:
    - name: loopback9
    - name: loopback10
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
