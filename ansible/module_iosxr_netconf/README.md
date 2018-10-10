# Ansible module: ansible.module_iosxr_netconf


Configures NetConf sub-system service on Cisco IOS-XR devices

## Description

This module provides an abstraction that enables and configures the netconf system service running on Cisco IOS-XR Software. This module can be used to easily enable the Netconf API. Netconf provides a programmatic interface for working with configuration and state resources as defined in RFC 6242.

## Requirements

TODO

## Arguments

``` json
{
    "netconf_port": "{'description': ['This argument specifies the port the netconf service should listen on for SSH connections.  The default port as defined in RFC 6242 is 830.'], 'required': False, 'default': 830, 'aliases': ['listens_on']}",
    "netconf_vrf": "{'description': ['netconf vrf name'], 'required': False, 'default': 'default', 'aliases': ['vrf']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Specifies the state of the C(iosxr_netconf) resource on the remote device.  If the I(state) argument is set to I(present) the netconf service will be configured.  If the I(state) argument is set to I(absent) the netconf service will be removed from the configuration.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: enable netconf service on port 830
  iosxr_netconf:
    listens_on: 830
    state: present

- name: disable netconf service
  iosxr_netconf:
    state: absent

```

## License

TODO

## Author Information
  - ['Kedar Kekan (@kedarX)']
