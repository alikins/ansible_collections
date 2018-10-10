# Ansible module: ansible.module_junos_static_route


Manage static IP routes on Juniper JUNOS network devices

## Description

This module provides declarative management of static IP routes on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "address": "{'description': ['Network address with prefix of the static route.'], 'required': True, 'aliases': ['prefix']}",
    "aggregate": "{'description': ['List of static route definitions']}",
    "next_hop": "{'description': ['Next hop IP of the static route.'], 'required': True}",
    "preference": "{'description': ['Global admin preference of the static route.'], 'aliases': ['admin_distance']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "qualified_next_hop": "{'description': ['Qualified next hop IP of the static route. Qualified next hops allow to associate preference with a particular next-hop address.']}",
    "qualified_preference": "{'description': ['Assign preference for qualified next hop.']}",
    "state": "{'description': ['State of the static route configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure static route
  junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present

- name: delete static route
  junos_static_route:
    address: 192.168.2.0/24
    state: absent

- name: deactivate static route configuration
  junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present
    active: False

- name: activate static route configuration
  junos_static_route:
    address: 192.168.2.0/24
    next_hop: 10.0.0.1
    preference: 10
    qualified_next_hop: 10.0.0.2
    qualified_preference: 3
    state: present
    active: True

- name: Configure static route using aggregate
  junos_static_route:
    aggregate:
    - { address: 4.4.4.0/24, next_hop: 3.3.3.3, qualified_next_hop: 5.5.5.5, qualified_preference: 30 }
    - { address: 5.5.5.0/24, next_hop: 6.6.6.6, qualified_next_hop: 7.7.7.7, qualified_preference: 12 }
    preference: 10

- name: Delete static route using aggregate
  junos_static_route:
    aggregate:
    - address: 4.4.4.0/24
    - address: 5.5.5.0/24
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
