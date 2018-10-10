# Ansible module: ansible.module_vyos_static_route


Manage static IP routes on Vyatta VyOS network devices

## Description

This module provides declarative management of static IP routes on Vyatta VyOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "admin_distance": "{'description': ['Admin distance of the static route.']}",
    "aggregate": "{'description': ['List of static route definitions']}",
    "mask": "{'description': ['Network prefix mask of the static route.']}",
    "next_hop": "{'description': ['Next hop IP of the static route.']}",
    "prefix": "{'description': ['Network prefix of the static route. C(mask) param should be ignored if C(prefix) is provided with C(mask) value C(prefix/mask).']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the static route configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure static route
  vyos_static_route:
    prefix: 192.168.2.0
    mask: 24
    next_hop: 10.0.0.1

- name: configure static route prefix/mask
  vyos_static_route:
    prefix: 192.168.2.0/16
    next_hop: 10.0.0.1

- name: remove configuration
  vyos_static_route:
    prefix: 192.168.2.0
    mask: 16
    next_hop: 10.0.0.1
    state: absent

- name: configure aggregates of static routes
  vyos_static_route:
    aggregate:
      - { prefix: 192.168.2.0, mask: 24, next_hop: 10.0.0.1 }
      - { prefix: 192.168.3.0, mask: 16, next_hop: 10.0.2.1 }
      - { prefix: 192.168.3.0/16, next_hop: 10.0.2.1 }

- name: Remove static route collections
  vyos_static_route:
    aggregate:
      - { prefix: 172.24.1.0/24, next_hop: 192.168.42.64 }
      - { prefix: 172.24.3.0/24, next_hop: 192.168.42.64 }
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
