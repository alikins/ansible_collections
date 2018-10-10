# Ansible module: ansible.module_junos_lldp_interface


Manage LLDP interfaces configuration on Juniper JUNOS network devices

## Description

This module provides declarative management of LLDP interfaces configuration on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "name": "{'description': ['Name of the interface LLDP should be configured on.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Value of C(present) ensures given LLDP configured on given I(interfaces) and is enabled, for value of C(absent) LLDP configuration on given I(interfaces) deleted. Value C(enabled) ensures LLDP protocol is enabled on given I(interfaces) and for value of C(disabled) it ensures LLDP is disabled on given I(interfaces).'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Configure LLDP on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: present

- name: Disable LLDP on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: disabled

- name: Enable LLDP on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: enabled

- name: Delete LLDP configuration on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: present

- name: Deactivate LLDP on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: present
    active: False

- name: Activate LLDP on specific interfaces
  junos_lldp_interface:
    name: ge-0/0/5
    state: present
    active: True

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
