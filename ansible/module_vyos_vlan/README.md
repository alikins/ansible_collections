# Ansible module: ansible.module_vyos_vlan


Manage VLANs on VyOS network devices

## Description

This module provides declarative management of VLANs on VyOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Configure Virtual interface address.']}",
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vlan C(name) for associated interfaces. If the value in the C(associated_interfaces) does not match with the operational state of vlan on device it will result in failure.'], 'version_added': '2.5'}",
    "delay": "{'description': ['Delay the play should wait to check for declarative intent params values.'], 'default': 10}",
    "interfaces": "{'description': ['List of interfaces that should be associated to the VLAN.'], 'required': True}",
    "name": "{'description': ['Name of the VLAN.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['ID of the VLAN. Range 0-4094.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create vlan
  vyos_vlan:
    vlan_id: 100
    name: vlan-100
    interfaces: eth1
    state: present

- name: Add interfaces to VLAN
  vyos_vlan:
    vlan_id: 100
    interfaces:
      - eth1
      - eth2

- name: Configure virtual interface address
  vyos_vlan:
    vlan_id: 100
    interfaces: eth1
    address: 172.26.100.37/24

- name: vlan interface config + intent
  vyos_vlan:
    vlan_id: 100
    interfaces: eth0
    associated_interfaces:
    - eth0

- name: vlan intent check
  vyos_vlan:
    vlan_id: 100
    associated_interfaces:
    - eth3
    - eth4

- name: Delete vlan
  vyos_vlan:
    vlan_id: 100
    interfaces: eth1
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
