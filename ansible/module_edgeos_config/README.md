# Ansible module: ansible.module_edgeos_config


Manage EdgeOS configuration on remote device

## Description

This module provides configuration file management of EdgeOS devices. It provides arguments for managing both the configuration file and state of the active configuration. All configuration statements are based on `set` and `delete` commands in the device configuration.
This is a network module and requires the C(connection: network_cli) in order to work properly.
For more information please see the L(Network Guide,../network/getting_started/index.html).

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ["The C(backup) argument will backup the current device's active configuration to the Ansible control host prior to making any changes. The backup file will be located in the backup folder in the playbook root directory or role root directory if the playbook is part of an ansible role. If the directory does not exist, it is created."], 'type': 'bool', 'default': False}",
    "comment": "{'description': ['Allows a commit description to be specified to be included when the configuration is committed. If the configuration is not changed or committed, this argument is ignored.'], 'default': 'configured by edgeos_config'}",
    "config": "{'description': ['The C(config) argument specifies the base configuration to use to compare against the desired configuration. If this value is not specified, the module will automatically retrieve the current active configuration from the remote device.']}",
    "lines": "{'description': ['The ordered set of configuration lines to be managed and compared with the existing configuration on the remote device.']}",
    "match": "{'description': ['The C(match) argument controls the method used to match against the current active configuration. By default, the desired config is matched against the active config and the deltas are loaded. If the C(match) argument is set to C(none) the active configuration is ignored and the configuration is always loaded.'], 'default': 'line', 'choices': ['line', 'none']}",
    "save": "{'description': ['The C(save) argument controls whether or not changes made to the active configuration are saved to disk. This is independent of committing the config. When set to C(True), the active configuration is saved.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['The C(src) argument specifies the path to the source config file to load. The source config file can either be in bracket format or set format. The source file can include Jinja2 template variables.']}",
}
```

## Examples


``` yaml

- name: configure the remote device
  edgeos_config:
    lines:
      - set system host-name {{ inventory_hostname }}
      - set service lldp
      - delete service dhcp-server

- name: backup and load from file
  edgeos_config:
    src: edgeos.cfg
    backup: yes

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)', 'Sam Doran (@samdoran)']
  - ['Nathaniel Case (@qalthos)', 'Sam Doran (@samdoran)']
