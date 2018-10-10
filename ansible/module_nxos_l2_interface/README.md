# Ansible module: ansible.module_nxos_l2_interface


Manage Layer-2 interface on Cisco NXOS devices

## Description

This module provides declarative management of Layer-2 interface on Cisco NXOS devices.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['Configure given VLAN in access port. If C(mode=access), used as the access VLAN ID.']}",
    "aggregate": "{'description': ['List of Layer-2 interface definitions.']}",
    "mode": "{'description': ['Mode in which interface needs to be configured.'], 'choices': ['access', 'trunk']}",
    "name": "{'description': ['Full name of the interface excluding any logical unit number, i.e. Ethernet1/1.'], 'required': True, 'aliases': ['interface']}",
    "native_vlan": "{'description': ['Native VLAN to be configured in trunk port. If C(mode=trunk), used as the trunk native VLAN ID.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "state": "{'description': ['Manage the state of the Layer-2 Interface configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'unconfigured']}",
    "trunk_allowed_vlans": "{'description': ['List of allowed VLANs in a given trunk port. If C(mode=trunk), these are the only VLANs that will be configured on the trunk, i.e. "2-10,15".']}",
    "trunk_vlans": "{'description': ['List of VLANs to be configured in trunk port. If C(mode=trunk), used as the VLAN range to ADD or REMOVE from the trunk.'], 'aliases': ['trunk_add_vlans']}",
}
```

## Examples


``` yaml

- name: Ensure Eth1/5 is in its default l2 interface state
  nxos_l2_interface:
    name: Ethernet1/5
    state: unconfigured

- name: Ensure Eth1/5 is configured for access vlan 20
  nxos_l2_interface:
    name: Ethernet1/5
    mode: access
    access_vlan: 20

- name: Ensure Eth1/5 only has vlans 5-10 as trunk vlans
  nxos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 5-10

- name: Ensure eth1/5 is a trunk port and ensure 2-50 are being tagged (doesn't mean others aren't also being tagged)
  nxos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 2-50

- name: Ensure these VLANs are not being tagged on the trunk
  nxos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    trunk_vlans: 51-4094
    state: absent

-  name: Aggregate Configure interfaces for access_vlan with aggregate
   nxos_l2_interface:
     aggregate:
       - { name: "Ethernet1/2", access_vlan: 6 }
       - { name: "Ethernet1/7", access_vlan: 15 }
     mode: access

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']