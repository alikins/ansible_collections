# Ansible module: ansible.module_ios_l2_interface


Manage Layer-2 interface on Cisco IOS devices

## Description

This module provides declarative management of Layer-2 interfaces on Cisco IOS devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port. If C(mode=access), used as the access VLAN ID.']}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'default': 'access', 'choices': ['access', 'trunk']}",
    "name": "{'description': ['Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1.'], 'required': True, 'aliases': ['interface']}",
    "native_vlan": "{'description': ['Native VLAN to be configured in trunk port. If C(mode=trunk), used as the trunk native VLAN ID.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "state": "{'description': ['Manage the state of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'unconfigured']}",
    "trunk_allowed_vlans": "{'description': ['List of allowed VLANs in a given trunk port. If C(mode=trunk), these are the only VLANs that will be configured on the trunk, i.e. "2-10,15".']}",
    "trunk_vlans": "{'description': ['List of VLANs to be configured in trunk port. If C(mode=trunk), used as the VLAN range to ADD or REMOVE from the trunk.']}",
}
```

## Examples


``` yaml

- name: Ensure GigabitEthernet0/5 is in its default l2 interface state
  ios_l2_interface:
    name: GigabitEthernet0/5
    state: unconfigured

- name: Ensure GigabitEthernet0/5 is configured for access vlan 20
  ios_l2_interface:
    name: GigabitEthernet0/5
    mode: access
    access_vlan: 20

- name: Ensure GigabitEthernet0/5 only has vlans 5-10 as trunk vlans
  ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 5-10

- name: Ensure GigabitEthernet0/5 is a trunk port and ensure 2-50 are being tagged (doesn't mean others aren't also being tagged)
  ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 2-50

- name: Ensure these VLANs are not being tagged on the trunk
  ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    trunk_vlans: 51-4094
    state: absent

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
