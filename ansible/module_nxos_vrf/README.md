# Ansible module: ansible.module_nxos_vrf


Manages global VRF configuration

## Description

This module provides declarative management of VRFs on CISCO NXOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['Administrative state of the VRF.'], 'default': 'up', 'choices': ['up', 'down']}",
    "aggregate": "{'description': ['List of VRFs definitions.'], 'version_added': 2.5}",
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vrf C(name) for associated interfaces. If the value in the C(associated_interfaces) does not match with the operational state of vrf interfaces on device it will result in failure.'], 'version_added': '2.5'}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.'], 'default': 10}",
    "description": "{'description': ["Description of the VRF or keyword 'default'."]}",
    "interfaces": "{'description': ["List of interfaces to check the VRF has been configured correctly or keyword 'default'."], 'version_added': 2.5}",
    "name": "{'description': ['Name of VRF to be managed.'], 'required': True, 'aliases': ['vrf']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "purge": "{'description': ['Purge VRFs not defined in the I(aggregate) parameter.'], 'type': 'bool', 'default': False, 'version_added': 2.5}",
    "rd": "{'description': ["VPN Route Distinguisher (RD). Valid values are a string in one of the route-distinguisher formats (ASN2:NN, ASN4:NN, or IPV4:NN); the keyword 'auto', or the keyword 'default'."], 'version_added': '2.2'}",
    "state": "{'description': ['Manages desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vni": "{'description': ["Specify virtual network identifier. Valid values are Integer or keyword 'default'."], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: Ensure ntc VRF exists on switch
  nxos_vrf:
    name: ntc
    description: testing
    state: present

- name: Aggregate definition of VRFs
  nxos_vrf:
    aggregate:
      - { name: test1, description: Testing, admin_state: down }
      - { name: test2, interfaces: Ethernet1/2 }

- name: Aggregate definitions of VRFs with Purge
  nxos_vrf:
    aggregate:
      - { name: ntc1, description: purge test1 }
      - { name: ntc2, description: purge test2 }
    state: present
    purge: yes

- name: Delete VRFs exist on switch
  nxos_vrf:
    aggregate:
      - { name: ntc1 }
      - { name: ntc2 }
    state: absent

- name: Assign interfaces to VRF declaratively
  nxos_vrf:
    name: test1
    interfaces:
      - Ethernet2/3
      - Ethernet2/5

- name: Check interfaces assigend to VRF
  nxos_vrf:
    name: test1
    associated_interfaces:
      - Ethernet2/3
      - Ethernet2/5

- name: Ensure VRF is tagged with interface Ethernet2/5 only (Removes from Ethernet2/3)
  nxos_vrf:
    name: test1
    interfaces:
      - Ethernet2/5

- name: Delete VRF
  nxos_vrf:
    name: ntc
    state: absent

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)', 'Trishna Guha (@trishnaguha)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)', 'Trishna Guha (@trishnaguha)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)', 'Trishna Guha (@trishnaguha)']
