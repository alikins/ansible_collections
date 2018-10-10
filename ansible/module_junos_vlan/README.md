# Ansible module: ansible.module_junos_vlan


Manage VLANs on Juniper JUNOS network devices

## Description

This module provides declarative management of VLANs on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "description": "{'description': ['Text description of VLANs.']}",
    "interfaces": "{'description': ['List of interfaces to check the VLAN has been configured correctly.']}",
    "l3_interface": "{'description': ['Name of logical layer 3 interface.'], 'version_added': '2.7'}",
    "name": "{'description': ['Name of the VLAN.'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['ID of the VLAN. Range 1-4094.'], 'required': True}",
}
```

## Examples


``` yaml

- name: configure VLAN ID and name
  junos_vlan:
    vlan_name: test
    vlan_id: 20
    name: test-vlan

- name: Link to logical layer 3 interface
  junos_vlan:
    vlan_name: test
    vlan_id: 20
    l3-interface: vlan.20
    name: test-vlan

- name: remove VLAN configuration
  junos_vlan:
    vlan_name: test
    state: absent

- name: deactive VLAN configuration
  junos_vlan:
    vlan_name: test
    state: present
    active: False

- name: activate VLAN configuration
  junos_vlan:
    vlan_name: test
    state: present
    active: True

- name: Create vlan configuration using aggregate
  junos_vlan:
    aggregate:
      - { vlan_id: 159, name: test_vlan_1, description: test vlan-1 }
      - { vlan_id: 160, name: test_vlan_2, description: test vlan-2 }

- name: Delete vlan configuration using aggregate
  junos_vlan:
    aggregate:
      - { vlan_id: 159, name: test_vlan_1 }
      - { vlan_id: 160, name: test_vlan_2 }
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
