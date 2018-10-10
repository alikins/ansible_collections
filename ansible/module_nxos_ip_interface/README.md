# Ansible module: ansible.module_nxos_ip_interface


Manages L3 attributes for IPv4 and IPv6 interfaces

## Description

Manages Layer 3 attributes for IPv4 and IPv6 interfaces.

## Requirements

TODO

## Arguments

``` json
{
    "addr": "{'description': ['IPv4 or IPv6 Address.']}",
    "allow_secondary": "{'description': ['Allow to configure IPv4 secondary addresses on interface.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "dot1q": "{'description': ['Configures IEEE 802.1Q VLAN encapsulation on the subinterface. The range is from 2 to 4093.'], 'version_added': '2.5'}",
    "interface": "{'description': ['Full name of interface, i.e. Ethernet1/1, vlan10.'], 'required': True}",
    "mask": "{'description': ['Subnet mask for IPv4 or IPv6 Address in decimal format.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tag": "{'description': ['Route tag for IPv4 or IPv6 Address in integer format.'], 'default': 0, 'version_added': '2.4'}",
    "version": "{'description': ['Version of IP address. If the IP address is IPV4 version should be v4. If the IP address is IPV6 version should be v6.'], 'default': 'v4', 'choices': ['v4', 'v6']}",
}
```

## Examples


``` yaml

- name: Ensure ipv4 address is configured on Ethernet1/32
  nxos_ip_interface:
    interface: Ethernet1/32
    transport: nxapi
    version: v4
    state: present
    addr: 20.20.20.20
    mask: 24

- name: Ensure ipv6 address is configured on Ethernet1/31
  nxos_ip_interface:
    interface: Ethernet1/31
    transport: cli
    version: v6
    state: present
    addr: '2001::db8:800:200c:cccb'
    mask: 64

- name: Ensure ipv4 address is configured with tag
  nxos_ip_interface:
    interface: Ethernet1/32
    transport: nxapi
    version: v4
    state: present
    tag: 100
    addr: 20.20.20.20
    mask: 24

- name: Ensure ipv4 address is configured on sub-intf with dot1q encapsulation
  nxos_ip_interface:
    interface: Ethernet1/32.10
    transport: nxapi
    version: v4
    state: present
    dot1q: 10
    addr: 20.20.20.20
    mask: 24

- name: Configure ipv4 address as secondary if needed
  nxos_ip_interface:
    interface: Ethernet1/32
    transport: nxapi
    version: v4
    state: present
    allow_secondary: true
    addr: 21.21.21.21
    mask: 24

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
