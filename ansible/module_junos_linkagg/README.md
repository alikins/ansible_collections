# Ansible module: ansible.module_junos_linkagg


Manage link aggregation groups on Juniper JUNOS network devices

## Description

This module provides declarative management of link aggregation groups on Juniper JUNOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of link aggregation definitions.']}",
    "description": "{'description': ['Description of Interface.']}",
    "device_count": "{'description': ['Number of aggregated ethernet devices that can be configured. Acceptable integer value is between 1 and 128.']}",
    "members": "{'description': ['List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces.'], 'required': True}",
    "min_links": "{'description': ['Minimum members that should be up before bringing up the link aggregation group.']}",
    "mode": "{'description': ['Mode of the link aggregation group. A value of C(on) will enable LACP in C(passive) mode. C(active) configures the link to actively information about the state of the link, or it can be configured in C(passive) mode ie. send link state information only when received them from another link. A value of C(off) will disable LACP.'], 'default': False, 'choices': ['on', 'off', 'active', 'passive']}",
    "name": "{'description': ['Name of the link aggregation group.'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the link aggregation group.'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
}
```

## Examples


``` yaml

- name: configure link aggregation
  junos_linkagg:
    name: ae11
    members:
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
    lacp: active
    device_count: 4
    state: present

- name: delete link aggregation
  junos_linkagg:
    name: ae11
    members:
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
    lacp: active
    device_count: 4
    state: delete

- name: deactivate link aggregation
  junos_linkagg:
    name: ae11
    members:
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
    lacp: active
    device_count: 4
    state: present
    active: False

- name: Activate link aggregation
  junos_linkagg:
    name: ae11
    members:
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
    lacp: active
    device_count: 4
    state: present
    active: True

- name: Disable link aggregation
  junos_linkagg:
    name: ae11
    state: down

- name: Enable link aggregation
  junos_linkagg:
    name: ae11
    state: up

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
