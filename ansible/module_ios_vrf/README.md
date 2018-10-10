# Ansible module: ansible.module_ios_vrf


Manage the collection of VRF definitions on Cisco IOS devices

## Description

This module provides declarative management of VRF definitions on Cisco IOS devices.  It allows playbooks to manage individual or the entire VRF collection.  It also supports purging VRF definitions from the configuration that are not explicitly defined.

## Requirements

TODO

## Arguments

``` json
{
    "associated_interfaces": "{'description': ['This is a intent option and checks the operational state of the for given vrf C(name) for associated interfaces. If the value in the C(associated_interfaces) does not match with the operational state of vrf interfaces on device it will result in failure.'], 'version_added': '2.5'}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device.'], 'version_added': '2.4', 'default': 10}",
    "description": "{'description': ['Provides a short description of the VRF definition in the current active configuration.  The VRF definition value accepts alphanumeric characters used to provide additional information about the VRF.']}",
    "interfaces": "{'description': ['Identifies the set of interfaces that should be configured in the VRF.  Interfaces must be routed interfaces in order to be placed into a VRF.']}",
    "name": "{'description': ['The name of the VRF definition to be managed on the remote IOS device.  The VRF definition name is an ASCII string name used to uniquely identify the VRF.  This argument is mutually exclusive with the C(vrfs) argument']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "purge": "{'description': ['Instructs the module to consider the VRF definition absolute.  It will remove any previously configured VRFs on the device.'], 'default': False}",
    "rd": "{'description': ['The router-distinguisher value uniquely identifies the VRF to routing processes on the remote IOS system.  The RD value takes the form of C(A:B) where C(A) and C(B) are both numeric values.']}",
    "route_both": "{'description': ['Adds an export and import list of extended route target communities to the VRF.'], 'version_added': '2.5'}",
    "route_both_ipv4": "{'description': ['Adds an export and import list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "route_both_ipv6": "{'description': ['Adds an export and import list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "route_export": "{'description': ['Adds an export list of extended route target communities to the VRF.'], 'version_added': '2.5'}",
    "route_export_ipv4": "{'description': ['Adds an export list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "route_export_ipv6": "{'description': ['Adds an export list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "route_import": "{'description': ['Adds an import list of extended route target communities to the VRF.'], 'version_added': '2.5'}",
    "route_import_ipv4": "{'description': ['Adds an import list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "route_import_ipv6": "{'description': ['Adds an import list of extended route target communities in address-family configuration submode to the VRF.'], 'version_added': '2.7'}",
    "state": "{'description': ['Configures the state of the VRF definition as it relates to the device operational configuration.  When set to I(present), the VRF should be configured in the device active configuration and when set to I(absent) the VRF should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vrfs": "{'description': ['The set of VRF definition objects to be configured on the remote IOS device.  Ths list entries can either be the VRF name or a hash of VRF definitions and attributes.  This argument is mutually exclusive with the C(name) argument.']}",
}
```

## Examples


``` yaml

- name: configure a vrf named management
  ios_vrf:
    name: management
    description: oob mgmt vrf
    interfaces:
      - Management1

- name: remove a vrf named test
  ios_vrf:
    name: test
    state: absent

- name: configure set of VRFs and purge any others
  ios_vrf:
    vrfs:
      - red
      - blue
      - green
    purge: yes

- name: Creates a list of import RTs for the VRF with the same parameters
  ios_vrf:
    name: test_import
    rd: 1:100
    route_import:
      - 1:100
      - 3:100

- name: Creates a list of import RTs in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_import_ipv4
    rd: 1:100
    route_import_ipv4:
      - 1:100
      - 3:100

- name: Creates a list of import RTs in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_import_ipv6
    rd: 1:100
    route_import_ipv6:
      - 1:100
      - 3:100

- name: Creates a list of export RTs for the VRF with the same parameters
  ios_vrf:
    name: test_export
    rd: 1:100
    route_export:
      - 1:100
      - 3:100

- name: Creates a list of export RTs in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_export_ipv4
    rd: 1:100
    route_export_ipv4:
      - 1:100
      - 3:100

- name: Creates a list of export RTs in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_export_ipv6
    rd: 1:100
    route_export_ipv6:
      - 1:100
      - 3:100

- name: Creates a list of import and export route targets for the VRF with the same parameters
  ios_vrf:
    name: test_both
    rd: 1:100
    route_both:
      - 1:100
      - 3:100

- name: Creates a list of import and export route targets in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_both_ipv4
    rd: 1:100
    route_both_ipv4:
      - 1:100
      - 3:100

- name: Creates a list of import and export route targets in address-family configuration submode for the VRF with the same parameters
  ios_vrf:
    name: test_both_ipv6
    rd: 1:100
    route_both_ipv6:
      - 1:100
      - 3:100


```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
