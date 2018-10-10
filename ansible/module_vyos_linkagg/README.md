# Ansible module: ansible.module_vyos_linkagg


Manage link aggregation groups on VyOS network devices

## Description

This module provides declarative management of link aggregation groups on VyOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of link aggregation definitions.']}",
    "members": "{'description': ['List of members of the link aggregation group.']}",
    "mode": "{'description': ['Mode of the link aggregation group.'], 'choices': ['802.3ad', 'active-backup', 'broadcast', 'round-robin', 'transmit-load-balance', 'adaptive-load-balance', 'xor-hash', 'on']}",
    "name": "{'description': ['Name of the link aggregation group.'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the link aggregation group.'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
}
```

## Examples


``` yaml

- name: configure link aggregation group
  vyos_linkagg:
    name: bond0
    members:
      - eth0
      - eth1

- name: remove configuration
  vyos_linkagg:
    name: bond0
    state: absent

- name: Create aggregate of linkagg definitions
  vyos_linkagg:
    aggregate:
        - { name: bond0, members: [eth1] }
        - { name: bond1, members: [eth2] }

- name: Remove aggregate of linkagg definitions
  vyos_linkagg:
    aggregate:
      - name: bond0
      - name: bond1
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
