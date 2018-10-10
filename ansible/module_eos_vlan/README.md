# Ansible module: ansible.module_eos_vlan


Manage VLANs on Arista EOS network devices

## Description

This module provides declarative management of VLANs on Arista EOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VLANs definitions.']}",
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vlan C(name) for associated interfaces. The name of interface is case sensitive and should be in expanded format and not abbreviated. If the value in the C(associated_interfaces) does not match with the operational state of vlan interfaces on device it will result in failure.'], 'version_added': '2.5'}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "delay": "{'description': ['Delay the play should wait to check for declarative intent params values.'], 'default': 10}",
    "interfaces": "{'description': ['List of interfaces that should be associated to the VLAN. The name of interface is case sensitive and should be in expanded format and not abbreviated.']}",
    "name": "{'description': ['Name of the VLAN.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(eapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(eapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['eapi', 'cli'], 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=eapi).  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool', 'default': 'yes'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VLAN configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'active', 'suspend']}",
    "vlan_id": "{'description': ['ID of the VLAN.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create vlan
  eos_vlan:
    vlan_id: 4000
    name: vlan-4000
    state: present

- name: Add interfaces to vlan
  eos_vlan:
    vlan_id: 4000
    state: present
    interfaces:
      - Ethernet1
      - Ethernet2

- name: Check if interfaces is assigned to vlan
  eos_vlan:
    vlan_id: 4000
    associated_interfaces:
      - Ethernet1
      - Ethernet2

- name: Suspend vlan
  eos_vlan:
    vlan_id: 4000
    state: suspend

- name: Unsuspend vlan
  eos_vlan:
    vlan_id: 4000
    state: active

- name: Create aggregate of vlans
  eos_vlan:
    aggregate:
      - vlan_id: 4000
      - {vlan_id: 4001, name: vlan-4001}

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
