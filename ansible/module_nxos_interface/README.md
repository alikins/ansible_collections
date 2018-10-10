# Ansible module: ansible.module_nxos_interface


Manages physical attributes of interfaces

## Description

Manages physical attributes of interfaces of NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['Administrative state of the interface.'], 'default': 'up', 'choices': ['up', 'down']}",
    "aggregate": "{'description': ['List of Interfaces definitions.'], 'version_added': 2.5}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.'], 'default': 10}",
    "description": "{'description': ['Interface description.']}",
    "duplex": "{'description': ['Interface link status. Applicable for ethernet interface only.'], 'default': 'auto', 'choices': ['full', 'half', 'auto'], 'version_added': 2.5}",
    "fabric_forwarding_anycast_gateway": "{'description': ['Associate SVI with anycast gateway under VLAN configuration mode. Applicable for SVI interface only.'], 'type': 'bool', 'version_added': 2.2}",
    "interface_type": "{'description': ['Interface type to be unconfigured from the device.'], 'choices': ['loopback', 'portchannel', 'svi', 'nve'], 'version_added': 2.2}",
    "ip_forward": "{'description': ['Enable/Disable ip forward feature on SVIs.'], 'choices': ['enable', 'disable'], 'version_added': 2.2}",
    "mode": "{'description': ['Manage Layer 2 or Layer 3 state of the interface. This option is supported for ethernet and portchannel interface. Applicable for ethernet and portchannel interface only.'], 'choices': ['layer2', 'layer3']}",
    "mtu": "{'description': ['MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for ethernet interface only.'], 'version_added': 2.5}",
    "name": "{'description': ['Full name of interface, i.e. Ethernet1/1, port-channel10.'], 'required': True, 'aliases': ['interface']}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for LLDP neighbor.', 'The following suboptions are available. This is state check parameter only.'], 'suboptions': {'host': {'description': ['LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['LLDP neighbor port to which given interface C(name) is connected.']}}, 'version_added': 2.5}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)'], 'version_added': 2.5}",
    "speed": "{'description': ['Interface link speed. Applicable for ethernet interface only.'], 'version_added': 2.5}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'default']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)'], 'version_added': 2.5}",
}
```

## Examples


``` yaml

- name: Ensure an interface is a Layer 3 port and that it has the proper description
  nxos_interface:
    name: Ethernet1/1
    description: 'Configured by Ansible'
    mode: layer3

- name: Admin down an interface
  nxos_interface:
    name: Ethernet2/1
    admin_state: down

- name: Remove all loopback interfaces
  nxos_interface:
    name: loopback
    state: absent

- name: Remove all logical interfaces
  nxos_interface:
    interface_type: "{{ item }} "
    state: absent
  loop:
    - loopback
    - portchannel
    - svi
    - nve

- name: Admin up all loopback interfaces
  nxos_interface:
    name: loopback 0-1023
    admin_state: up

- name: Admin down all loopback interfaces
  nxos_interface:
    name: looback 0-1023
    admin_state: down

- name: Check neighbors intent arguments
  nxos_interface:
    name: Ethernet2/3
    neighbors:
    - port: Ethernet2/3
      host: abc.mycompany.com

- name: Add interface using aggregate
  nxos_interface:
    aggregate:
    - { name: Ethernet0/1, mtu: 256, description: test-interface-1 }
    - { name: Ethernet0/2, mtu: 516, description: test-interface-2 }
    duplex: full
    speed: 100
    state: present

- name: Delete interface using aggregate
  nxos_interface:
    aggregate:
    - name: Loopback9
    - name: Loopback10
    state: absent

- name: Check intent arguments
  nxos_interface:
    name: Ethernet0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Trishna Guha (@trishnaguha)']
  - ['Jason Edelman (@jedelman8)', 'Trishna Guha (@trishnaguha)']
