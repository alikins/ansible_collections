# Ansible module: ansible.module_ios_vlan


Manage VLANs on IOS network devices

## Description

This module provides declarative management of VLANs on Cisco IOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vlan C(name) for associated interfaces. If the value in the C(associated_interfaces) does not match with the operational state of vlan interfaces on device it will result in failure.'], 'version_added': '2.5'}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "delay": "{'description': ['Delay the play should wait to check for declarative intent params values.'], 'default': 10}",
    "interfaces": "{'description': ['List of interfaces that should be associated to the VLAN.'], 'required': True}",
    "name": "{'description': ['Name of the VLAN.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'active', 'suspend']}",
    "vlan_id": "{'description': ['ID of the VLAN. Range 1-4094.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create vlan
  ios_vlan:
    vlan_id: 100
    name: test-vlan
    state: present

- name: Add interfaces to VLAN
  ios_vlan:
    vlan_id: 100
    interfaces:
      - GigabitEthernet0/0
      - GigabitEthernet0/1

- name: Check if interfaces is assigned to VLAN
  ios_vlan:
    vlan_id: 100
    associated_interfaces:
      - GigabitEthernet0/0
      - GigabitEthernet0/1

- name: Delete vlan
  ios_vlan:
    vlan_id: 100
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
