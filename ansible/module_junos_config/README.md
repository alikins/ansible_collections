# Ansible module: ansible.module_junos_config


Manage configuration on devices running Juniper JUNOS

## Description

This module provides an implementation for working with the active configuration running on Juniper JUNOS devices.  It provides a set of arguments for loading configuration, performing rollback operations and zeroing the active configuration on the device.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "comment": "{'description': ['The C(comment) argument specifies a text string to be used when committing the configuration.  If the C(confirm) argument is set to False, this argument is silently ignored.'], 'default': 'configured by junos_config'}",
    "confirm": "{'description': ['The C(confirm) argument will configure a time out value in minutes for the commit to be confirmed before it is automatically rolled back.  If the C(confirm) argument is set to False, this argument is silently ignored.  If the value for this argument is set to 0, the commit is confirmed immediately.'], 'default': 0}",
    "confirm_commit": "{'description': ['This argument will execute commit operation on remote device. It can be used to confirm a previous commit.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "lines": "{'description': ['This argument takes a list of C(set) or C(delete) configuration lines to push into the remote device.  Each line must start with either C(set) or C(delete).  This argument is mutually exclusive with the I(src) argument.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "replace": "{'description': ['The C(replace) argument will instruct the remote device to replace the current configuration hierarchy with the one specified in the corresponding hierarchy of the source configuration loaded from this module.', 'Note this argument should be considered deprecated.  To achieve the equivalent, set the I(update) argument to C(replace). This argument will be removed in a future release. The C(replace) and C(update) argument is mutually exclusive.'], 'type': 'bool', 'default': False}",
    "rollback": "{'description': ['The C(rollback) argument instructs the module to rollback the current configuration to the identifier specified in the argument.  If the specified rollback identifier does not exist on the remote device, the module will fail.  To rollback to the most recent commit, set the C(rollback) argument to 0.']}",
    "src": "{'description': ['The I(src) argument provides a path to the configuration file to load into the remote system. The path can either be a full system path to the configuration file if the value starts with / or relative to the root of the implemented role or playbook. This argument is mutually exclusive with the I(lines) argument.'], 'version_added': '2.2'}",
    "src_format": "{'description': ['The I(src_format) argument specifies the format of the configuration found int I(src).  If the I(src_format) argument is not provided, the module will attempt to determine the format of the configuration file specified in I(src).'], 'choices': ['xml', 'set', 'text', 'json'], 'version_added': '2.2'}",
    "update": "{'description': ['This argument will decide how to load the configuration data particulary when the candidate configuration and loaded configuration contain conflicting statements. Following are accepted values. C(merge) combines the data in the loaded configuration with the candidate configuration. If statements in the loaded configuration conflict with statements in the candidate configuration, the loaded statements replace the candidate ones. C(override) discards the entire candidate configuration and replaces it with the loaded configuration. C(replace) substitutes each hierarchy level in the loaded configuration for the corresponding level.'], 'default': 'merge', 'choices': ['merge', 'override', 'replace'], 'version_added': '2.3'}",
    "zeroize": "{'description': ['The C(zeroize) argument is used to completely sanitize the remote device configuration back to initial defaults.  This argument will effectively remove all current configuration statements on the remote device.']}",
}
```

## Examples


``` yaml

- name: load configure file into device
  junos_config:
    src: srx.cfg
    comment: update config

- name: load configure lines into device
  junos_config:
    lines:
      - set interfaces ge-0/0/1 unit 0 description "Test interface"
      - set vlans vlan01 description "Test vlan"
    comment: update config

- name: Set routed VLAN interface (RVI) IPv4 address
  junos_config:
    lines:
      - set vlans vlan01 vlan-id 1
      - set interfaces irb unit 10 family inet address 10.0.0.1/24
      - set vlans vlan01 l3-interface irb.10

- name: rollback the configuration to id 10
  junos_config:
    rollback: 10

- name: zero out the current configuration
  junos_config:
    zeroize: yes

- name: Set VLAN access and trunking
  junos_config:
    lines:
      - set vlans vlan02 vlan-id 6
      - set interfaces ge-0/0/6.0 family ethernet-switching interface-mode access vlan members vlan02
      - set interfaces ge-0/0/6.0 family ethernet-switching interface-mode trunk vlan members vlan02

- name: confirm a previous commit
  junos_config:
    confirm_commit: yes

- name: for idempotency, use full-form commands
  junos_config:
    lines:
      # - set int ge-0/0/1 unit 0 desc "Test interface"
      - set interfaces ge-0/0/1 unit 0 description "Test interface"

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
