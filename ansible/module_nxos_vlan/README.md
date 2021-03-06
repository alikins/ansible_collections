# Ansible module: ansible.module_nxos_vlan


Manages VLAN resources and attributes

## Description

Manages VLAN configurations on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['Manage the VLAN administrative state of the VLAN equivalent to shut/no shut in VLAN config mode.'], 'default': 'up', 'choices': ['up', 'down']}",
    "aggregate": "{'description': ['List of VLANs definitions.'], 'version_added': '2.5'}",
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vlan C(name) for associated interfaces. If the value in the C(associated_interfaces) does not match with the operational state of vlan interfaces on device it will result in failure.'], 'version_added': '2.5'}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.'], 'default': 10}",
    "interfaces": "{'description': ["List of interfaces that should be associated to the VLAN or keyword 'default'."], 'version_added': '2.5'}",
    "mapped_vni": "{'description': ["The Virtual Network Identifier (VNI) ID that is mapped to the VLAN. Valid values are integer and keyword 'default'. Range 4096-16773119."], 'version_added': '2.2'}",
    "mode": "{'description': ['Set VLAN mode to classical ethernet or fabricpath. This is a valid option for Nexus 5000 and 7000 series.'], 'choices': ['ce', 'fabricpath'], 'version_added': '2.4'}",
    "name": "{'description': ["Name of VLAN or keyword 'default'."]}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "purge": "{'description': ['Purge VLANs not defined in the I(aggregate) parameter. This parameter can be used without aggregate as well.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['Single VLAN ID.']}",
    "vlan_range": "{'description': ['Range of VLANs such as 2-10 or 2,5,10-15, etc.']}",
    "vlan_state": "{'description': ['Manage the vlan operational state of the VLAN'], 'default': 'active', 'choices': ['active', 'suspend']}",
}
```

## Examples


``` yaml

- name: Ensure a range of VLANs are not present on the switch
  nxos_vlan:
    vlan_range: "2-10,20,50,55-60,100-150"
    state: absent

- name: Ensure VLAN 50 exists with the name WEB and is in the shutdown state
  nxos_vlan:
    vlan_id: 50
    admin_state: down
    name: WEB

- name: Ensure VLAN is NOT on the device
  nxos_vlan:
    vlan_id: 50
    state: absent

- name: Add interfaces to VLAN and check intent (config + intent)
  nxos_vlan:
    vlan_id: 100
    interfaces:
      - Ethernet2/1
      - Ethernet2/5
    associated_interfaces:
      - Ethernet2/1
      - Ethernet2/5

- name: Check interfaces assigned to VLAN
  nxos_vlan:
    vlan_id: 100
    associated_interfaces:
      - Ethernet2/1
      - Ethernet2/5

- name: Create aggregate of vlans
  nxos_vlan:
    aggregate:
      - { vlan_id: 4000, mode: ce }
      - { vlan_id: 4001, name: vlan-4001 }

- name: purge vlans - removes all other vlans except the ones mentioned in aggregate)
  nxos_vlan:
    aggregate:
      - vlan_id: 1
      - vlan_id: 4001
    purge: yes


```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)']
