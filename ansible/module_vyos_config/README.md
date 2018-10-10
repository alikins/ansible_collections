# Ansible module: ansible.module_vyos_config


Manage VyOS configuration on remote device

## Description

This module provides configuration file management of VyOS devices.  It provides arguments for managing both the configuration file and state of the active configuration.   All configuration statements are based on `set` and `delete` commands in the device configuration.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['The C(backup) argument will backup the current devices active configuration to the Ansible control host prior to making any changes.  The backup file will be located in the backup folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.'], 'type': 'bool', 'default': False}",
    "comment": "{'description': ['Allows a commit description to be specified to be included when the configuration is committed.  If the configuration is not changed or committed, this argument is ignored.'], 'default': 'configured by vyos_config'}",
    "config": "{'description': ['The C(config) argument specifies the base configuration to use to compare against the desired configuration.  If this value is not specified, the module will automatically retrieve the current active configuration from the remote device.']}",
    "lines": "{'description': ['The ordered set of configuration lines to be managed and compared with the existing configuration on the remote device.']}",
    "match": "{'description': ['The C(match) argument controls the method used to match against the current active configuration.  By default, the desired config is matched against the active config and the deltas are loaded.  If the C(match) argument is set to C(none) the active configuration is ignored and the configuration is always loaded.'], 'default': 'line', 'choices': ['line', 'none']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "save": "{'description': ['The C(save) argument controls whether or not changes made to the active configuration are saved to disk.  This is independent of committing the config.  When set to True, the active configuration is saved.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['The C(src) argument specifies the path to the source config file to load.  The source config file can either be in bracket format or set format.  The source file can include Jinja2 template variables.']}",
}
```

## Examples


``` yaml

- name: configure the remote device
  vyos_config:
    lines:
      - set system host-name {{ inventory_hostname }}
      - set service lldp
      - delete service dhcp-server

- name: backup and load from file
  vyos_config:
    src: vyos.cfg
    backup: yes

- name: render a Jinja2 template onto the VyOS router
  vyos_config:
    src: vyos_template.j2

- name: for idempotency, use full-form commands
  vyos_config:
    lines:
      # - set int eth eth2 description 'OUTSIDE'
      - set interface ethernet eth2 description 'OUTSIDE'

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
