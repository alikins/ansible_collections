# Ansible module: ansible.module_fortios_address


Manage fortios firewall address objects

## Description

This module provide management of firewall addresses on FortiOS devices.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['This argument will cause the module to create a backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the i(backup) folder.'], 'default': False, 'type': 'bool'}",
    "backup_filename": "{'description': ['Specifies the backup filename. If omitted filename will be formatted like HOST_config.YYYY-MM-DD@HH:MM:SS']}",
    "backup_path": "{'description': ['Specifies where to store backup files. Required if I(backup=yes).']}",
    "comment": "{'description': ['free text to describe address.']}",
    "config_file": "{'description': ['Path to configuration file. Required when I(file_mode) is True.'], 'version_added': '2.4'}",
    "country": "{'description': ['2 letter country code (like FR).']}",
    "end_ip": "{'description': ['Last ip in range (used only with type=iprange).']}",
    "file_mode": "{'description': ["Don't connect to any device, only use I(config_file) as input and Output."], 'default': False, 'type': 'bool', 'version_added': '2.4'}",
    "host": "{'description': ['Specifies the DNS hostname or IP address for connecting to the remote fortios device. Required when I(file_mode) is False.']}",
    "interface": "{'description': ['interface name the address apply to.'], 'default': 'any'}",
    "name": "{'description': ['Name of the address to add or delete.'], 'required': True}",
    "password": "{'description': ['Specifies the password used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "start_ip": "{'description': ['First ip in range (used only with type=iprange).']}",
    "state": "{'description': ['Specifies if address need to be added or deleted.'], 'required': True, 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['Timeout in seconds for connecting to the remote device.'], 'default': 60}",
    "type": "{'description': ['Type of the address.'], 'choices': ['iprange', 'fqdn', 'ipmask', 'geography']}",
    "username": "{'description': ['Configures the username used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "value": "{'description': ['Address value, based on type. If type=fqdn, somthing like www.google.com. If type=ipmask, you can use simple ip (192.168.0.1), ip+mask (192.168.0.1 255.255.255.0) or CIDR (192.168.0.1/32).']}",
    "vdom": "{'description': ['Specifies on which vdom to apply configuration']}",
}
```

## Examples


``` yaml

- name: Register french addresses
  fortios_address:
    host: 192.168.0.254
    username: admin
    password: p4ssw0rd
    state: present
    name: "fromfrance"
    type: geography
    country: FR
    comment: "French geoip address"

- name: Register some fqdn
  fortios_address:
    host: 192.168.0.254
    username: admin
    password: p4ssw0rd
    state: present
    name: "Ansible"
    type: fqdn
    value: www.ansible.com
    comment: "Ansible website"

- name: Register google DNS
  fortios_address:
    host: 192.168.0.254
    username: admin
    password: p4ssw0rd
    state: present
    name: "google_dns"
    type: ipmask
    value: 8.8.8.8


```

## License

TODO

## Author Information
  - ['Benjamin Jolivot (@bjolivot)']
