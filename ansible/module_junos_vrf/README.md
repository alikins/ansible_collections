# Ansible module: ansible.module_junos_vrf


Manage the VRF definitions on Juniper JUNOS devices

## Description

This module provides declarative management of VRF definitions on Juniper JUNOS devices.  It allows playbooks to manage individual or the entire VRF collection.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['The set of VRF definition objects to be configured on the remote JUNOS device.  Ths list entries can either be the VRF name or a hash of VRF definitions and attributes.  This argument is mutually exclusive with the C(name) argument.']}",
    "description": "{'description': ['Provides a short description of the VRF definition in the current active configuration.  The VRF definition value accepts alphanumeric characters used to provide additional information about the VRF.']}",
    "interfaces": "{'description': ['Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF.']}",
    "name": "{'description': ['The name of the VRF definition to be managed on the remote IOS device.  The VRF definition name is an ASCII string name used to uniquely identify the VRF.  This argument is mutually exclusive with the C(aggregate) argument']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "rd": "{'description': ['The router-distinguisher value uniquely identifies the VRF to routing processes on the remote IOS system.  The RD value takes the form of C(A:B) where C(A) and C(B) are both numeric values.']}",
    "state": "{'description': ['Configures the state of the VRF definition as it relates to the device operational configuration.  When set to I(present), the VRF should be configured in the device active configuration and when set to I(absent) the VRF should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
    "table_label": "{'description': ['Causes JUNOS to allocate a VPN label per VRF rather than per VPN FEC. This allows for forwarding of traffic to directly connected subnets, COS Egress filtering etc.'], 'type': 'bool'}",
    "target": "{'description': ['It configures VRF target community configuration. The target value takes the form of C(target:A:B) where C(A) and C(B) are both numeric values.']}",
}
```

## Examples


``` yaml

- name: Configure vrf configuration
  junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    state: present

- name: Remove vrf configuration
  junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    state: absent

- name: Deactivate vrf configuration
  junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    active: False

- name: Activate vrf configuration
  junos_vrf:
    name: test-1
    description: test-vrf-1
    interfaces:
      - ge-0/0/3
      - ge-0/0/2
    rd: 192.0.2.1:10
    target: target:65514:113
    active: True

- name: Create vrf using aggregate
  junos_vrf:
    aggregate:
    - name: test-1
      description: test-vrf-1
      interfaces:
        - ge-0/0/3
         - ge-0/0/2
      rd: 192.0.2.1:10
      target: target:65514:113
    - name: test-2
      description: test-vrf-2
      interfaces:
        - ge-0/0/4
        - ge-0/0/5
      rd: 192.0.2.2:10
      target: target:65515:114
  state: present

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
