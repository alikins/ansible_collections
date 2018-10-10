# Ansible module: ansible.module_junos_l2_interface


Manage Layer-2 interface on Juniper JUNOS network devices

## Description

This module provides declarative management of Layer-2 interface on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port. The value of C(access_vlan) should be vlan name.']}",
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "description": "{'description': ['Description of Interface.']}",
    "enhanced_layer": "{'description': ['True if your device has Enhanced Layer 2 Software (ELS).'], 'default': True, 'type': 'bool', 'version_added': '2.7'}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'choices': ['access', 'trunk']}",
    "name": "{'description': ['Name of the interface excluding any logical unit number.']}",
    "native_vlan": "{'description': ['Native VLAN to be configured in trunk port. The value of C(native_vlan) should be vlan id.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trunk_vlans": "{'description': ['List of VLAN names to be configured in trunk port. The value of C(trunk_vlans) should be list of vlan names.']}",
    "unit": "{'description': ['Logical interface number. Value of C(unit) should be of type integer.'], 'default': 0}",
}
```

## Examples


``` yaml

- name: Configure interface in access mode
  junos_l2_interface:
    name: ge-0/0/1
    description: interface-access
    mode: access
    access_vlan: red
    active: True
    state: present

- name: Configure interface in trunk mode
  junos_l2_interface:
    name: ge-0/0/1
    description: interface-trunk
    mode: trunk
    trunk_vlans:
    - blue
    - green
    native_vlan: 100
    active: True
    state: present

- name: Configure interface in access and trunk mode using aggregate
  junos_l2_interface:
    aggregate:
    - name: ge-0/0/1
      description: test-interface-access
      mode: access
      access_vlan: red
    - name: ge-0/0/2
      description: test-interface-trunk
      mode: trunk
      trunk_vlans:
      - blue
      - green
      native_vlan: 100
    active: True
    state: present

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
