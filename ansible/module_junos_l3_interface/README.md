# Ansible module: ansible.module_junos_l3_interface


Manage L3 interfaces on Juniper JUNOS network devices

## Description

This module provides declarative management of L3 interfaces on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of L3 interfaces definitions']}",
    "ipv4": "{'description': ['IPv4 of the L3 interface.']}",
    "ipv6": "{'description': ['IPv6 of the L3 interface.']}",
    "name": "{'description': ['Name of the L3 interface.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the L3 interface configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "unit": "{'description': ['Logical interface number.'], 'default': 0}",
}
```

## Examples


``` yaml

- name: Set ge-0/0/1 IPv4 address
  junos_l3_interface:
    name: ge-0/0/1
    ipv4: 192.168.0.1

- name: Remove ge-0/0/1 IPv4 address
  junos_l3_interface:
    name: ge-0/0/1
    state: absent

- name: Set ipv4 address using aggregate
  junos_l3_interface:
    aggregate:
    - name: ge-0/0/1
      ipv4: 192.0.2.1
    - name: ge-0/0/2
      ipv4: 192.0.2.2
      ipv6: fd5d:12c9:2201:2::2

- name: Delete ipv4 address using aggregate
  junos_l3_interface:
    aggregate:
    - name: ge-0/0/1
      ipv4: 192.0.2.1
    - name: ge-0/0/2
      ipv4: 192.0.2.2
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
