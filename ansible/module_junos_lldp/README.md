# Ansible module: ansible.module_junos_lldp


Manage LLDP configuration on Juniper JUNOS network devices

## Description

This module provides declarative management of LLDP service on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "hold_multiplier": "{'description': ['Specify the number of seconds that LLDP information is held before it is discarded. The multiplier value is used in combination with the C(interval) value.']}",
    "interval": "{'description': ['Frequency at which LLDP advertisements are sent (in seconds).']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Value of C(present) ensures given LLDP configuration is present on device and LLDP is enabled, for value of C(absent) LLDP configuration is deleted and LLDP is in disabled state. Value C(enabled) ensures LLDP protocol is enabled and LLDP configuration if any is configured on remote device, for value of C(disabled) it ensures LLDP protocol is disabled any LLDP configuration if any is still present.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "transmit_delay": "{'description': ['Specify the number of seconds the device waits before sending advertisements to neighbors after a change is made in local system.']}",
}
```

## Examples


``` yaml

- name: Enable LLDP service
  junos_lldp:
    state: enabled

- name: Disable LLDP service
  junos_lldp:
    state: disabled

- name: Set LLDP parameters
  junos_lldp:
    interval: 10
    hold_multiplier: 5
    transmit_delay: 30
    state: present

- name: Delete LLDP parameters
  junos_lldp:
    interval: 10
    hold_multiplier: 5
    transmit_delay: 30
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
