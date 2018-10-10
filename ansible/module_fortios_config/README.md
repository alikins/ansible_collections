# Ansible module: ansible.module_fortios_config


Manage config on Fortinet FortiOS firewall devices

## Description

This module provides management of FortiOS Devices configuration.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['This argument will cause the module to create a backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the i(backup) folder.'], 'default': False, 'type': 'bool'}",
    "backup_filename": "{'description': ['Specifies the backup filename. If omitted filename will be formatted like HOST_config.YYYY-MM-DD@HH:MM:SS']}",
    "backup_path": "{'description': ['Specifies where to store backup files. Required if I(backup=yes).']}",
    "config_file": "{'description': ['Path to configuration file. Required when I(file_mode) is True.'], 'version_added': '2.4'}",
    "file_mode": "{'description': ["Don't connect to any device, only use I(config_file) as input and Output."], 'default': False, 'type': 'bool', 'version_added': '2.4'}",
    "filter": "{'description': ['Only for partial backup, you can restrict by giving expected configuration path (ex. firewall address).'], 'default': ''}",
    "host": "{'description': ['Specifies the DNS hostname or IP address for connecting to the remote fortios device. Required when I(file_mode) is False.']}",
    "password": "{'description': ['Specifies the password used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "src": "{'description': ['The I(src) argument provides a path to the configuration template to load into the remote device.']}",
    "timeout": "{'description': ['Timeout in seconds for connecting to the remote device.'], 'default': 60}",
    "username": "{'description': ['Configures the username used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "vdom": "{'description': ['Specifies on which vdom to apply configuration']}",
}
```

## Examples


``` yaml

- name: Backup current config
  fortios_config:
    host: 192.168.0.254
    username: admin
    password: password
    backup: yes

- name: Backup only address objects
  fortios_config:
    host: 192.168.0.254
    username: admin
    password: password
    backup: yes
    backup_path: /tmp/forti_backup/
    filter: "firewall address"

- name: Update configuration from file
  fortios_config:
    host: 192.168.0.254
    username: admin
    password: password
    src: new_configuration.conf.j2


```

## License

TODO

## Author Information
  - ['Benjamin Jolivot (@bjolivot)']
