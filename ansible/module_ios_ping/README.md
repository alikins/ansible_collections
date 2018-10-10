# Ansible module: ansible.module_ios_ping


Tests reachability using ping from Cisco IOS network devices

## Description

Tests reachability using ping from switch to a remote destination.
For a general purpose network module, see the M(net_ping) module.
For Windows targets, use the M(win_ping) module instead.
For targets running Python, use the M(ping) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "count": "{'description': ['Number of packets to send.'], 'default': 5}",
    "dest": "{'description': ['The IP Address or hostname (resolvable by switch) of the remote node.'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "source": "{'description': ['The source IP Address.']}",
    "state": "{'description': ['Determines if the expected result is success or fail.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "vrf": "{'description': ['The VRF to use for forwarding.'], 'default': 'default'}",
}
```

## Examples


``` yaml

- name: Test reachability to 10.10.10.10 using default vrf
  ios_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using prod vrf
  ios_ping:
    dest: 10.20.20.20
    vrf: prod

- name: Test unreachability to 10.30.30.30 using default vrf
  ios_ping:
    dest: 10.30.30.30
    state: absent

- name: Test reachability to 10.40.40.40 using prod vrf and setting count and source
  ios_ping:
    dest: 10.40.40.40
    source: loopback0
    vrf: prod
    count: 20

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
