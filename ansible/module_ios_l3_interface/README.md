# Ansible module: ansible.module_ios_l3_interface


Manage Layer-3 interfaces on Cisco IOS network devices

## Description

This module provides declarative management of Layer-3 interfaces on IOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Layer-3 interfaces definitions. Each of the entry in aggregate list should define name of interface C(name) and a optional C(ipv4) or C(ipv6) address.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "ipv4": "{'description': ['IPv4 address to be set for the Layer-3 interface mentioned in I(name) option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24']}",
    "ipv6": "{'description': ['IPv6 address to be set for the Layer-3 interface mentioned in I(name) option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64']}",
    "name": "{'description': ['Name of the Layer-3 interface to be configured eg. GigabitEthernet0/2']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "state": "{'description': ['State of the Layer-3 interface configuration. It indicates if the configuration should be present or absent on remote device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Remove GigabitEthernet0/3 IPv4 and IPv6 address
  ios_l3_interface:
    name: GigabitEthernet0/3
    state: absent

- name: Set GigabitEthernet0/3 IPv4 address
  ios_l3_interface:
    name: GigabitEthernet0/3
    ipv4: 192.168.0.1/24

- name: Set GigabitEthernet0/3 IPv6 address
  ios_l3_interface:
    name: GigabitEthernet0/3
    ipv6: "fd5d:12c9:2201:1::1/64"

- name: Set GigabitEthernet0/3 in dhcp
  ios_l3_interface:
    name: GigabitEthernet0/3
    ipv4: dhcp
    ipv6: dhcp

- name: Set interface Vlan1 (SVI) IPv4 address
  ios_l3_interface:
    name: Vlan1
    ipv4: 192.168.0.5/24

- name: Set IP addresses on aggregate
  ios_l3_interface:
    aggregate:
      - { name: GigabitEthernet0/3, ipv4: 192.168.2.10/24 }
      - { name: GigabitEthernet0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  ios_l3_interface:
    aggregate:
      - { name: GigabitEthernet0/3, ipv4: 192.168.2.10/24 }
      - { name: GigabitEthernet0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
