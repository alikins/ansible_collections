# Ansible module: ansible.module_fortios_ipv4_policy


Manage IPv4 policy objects on Fortinet FortiOS firewall devices

## Description

This module provides management of firewall IPv4 policies on FortiOS devices.

## Requirements

TODO

## Arguments

``` json
{
    "application_list": "{'description': ['Specifies Application Control name.']}",
    "av_profile": "{'description': ['Specifies Antivirus profile name.']}",
    "backup": "{'description': ['This argument will cause the module to create a backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the i(backup) folder.'], 'default': False, 'type': 'bool'}",
    "backup_filename": "{'description': ['Specifies the backup filename. If omitted filename will be formatted like HOST_config.YYYY-MM-DD@HH:MM:SS']}",
    "backup_path": "{'description': ['Specifies where to store backup files. Required if I(backup=yes).']}",
    "comment": "{'description': ['free text to describe policy.']}",
    "config_file": "{'description': ['Path to configuration file. Required when I(file_mode) is True.'], 'version_added': '2.4'}",
    "dst_addr": "{'description': ['Specifies destination address (or group) object name(s). Required when I(state=present).']}",
    "dst_addr_negate": "{'description': ['Negate destination address param.'], 'default': False, 'type': 'bool'}",
    "dst_intf": "{'description': ['Specifies destination interface name(s).'], 'default': 'any'}",
    "file_mode": "{'description': ["Don't connect to any device, only use I(config_file) as input and Output."], 'default': False, 'type': 'bool', 'version_added': '2.4'}",
    "fixedport": "{'description': ['Use fixed port for nat.'], 'default': False, 'type': 'bool'}",
    "host": "{'description': ['Specifies the DNS hostname or IP address for connecting to the remote fortios device. Required when I(file_mode) is False.']}",
    "id": "{'description': ["Policy ID. Warning: policy ID number is different than Policy sequence number. The policy ID is the number assigned at policy creation. The sequence number represents the order in which the Fortigate will evaluate the rule for policy enforcement, and also the order in which rules are listed in the GUI and CLI. These two numbers do not necessarily correlate: this module is based off policy ID. TIP: policy ID can be viewed in the GUI by adding 'ID' to the display columns"], 'required': True}",
    "ips_sensor": "{'description': ['Specifies IPS Sensor profile name.']}",
    "logtraffic": "{'version_added': '2.4', 'description': ['Logs sessions that matched policy.'], 'default': 'utm', 'choices': ['disable', 'utm', 'all']}",
    "logtraffic_start": "{'version_added': '2.4', 'description': ['Logs beginning of session as well.'], 'default': False, 'type': 'bool'}",
    "nat": "{'description': ['Enable or disable Nat.'], 'default': False, 'type': 'bool'}",
    "password": "{'description': ['Specifies the password used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "policy_action": "{'description': ['Specifies accept or deny action policy. Required when I(state=present).'], 'choices': ['accept', 'deny'], 'aliases': ['action']}",
    "poolname": "{'description': ['Specifies NAT pool name.']}",
    "schedule": "{'description': ['defines policy schedule.'], 'default': 'always'}",
    "service": "{'description': ["Specifies policy service(s), could be a list (ex: ['MAIL','DNS']). Required when I(state=present)."], 'aliases': ['services']}",
    "service_negate": "{'description': ['Negate policy service(s) defined in service value.'], 'default': False, 'type': 'bool'}",
    "src_addr": "{'description': ['Specifies source address (or group) object name(s). Required when I(state=present).']}",
    "src_addr_negate": "{'description': ['Negate source address param.'], 'default': False, 'type': 'bool'}",
    "src_intf": "{'description': ['Specifies source interface name(s).'], 'default': 'any'}",
    "state": "{'description': ['Specifies if policy I(id) need to be added or deleted.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Timeout in seconds for connecting to the remote device.'], 'default': 60}",
    "username": "{'description': ['Configures the username used to authenticate to the remote device. Required when I(file_mode) is True.']}",
    "vdom": "{'description': ['Specifies on which vdom to apply configuration']}",
    "webfilter_profile": "{'description': ['Specifies Webfilter profile name.']}",
}
```

## Examples


``` yaml

- name: Allow external DNS call
  fortios_ipv4_policy:
    host: 192.168.0.254
    username: admin
    password: password
    id: 42
    src_addr: internal_network
    dst_addr: all
    service: dns
    nat: True
    state: present
    policy_action: accept
    logtraffic: disable

- name: Public Web
  fortios_ipv4_policy:
    host: 192.168.0.254
    username: admin
    password: password
    id: 42
    src_addr: all
    dst_addr: webservers
    services:
      - http
      - https
    state: present
    policy_action: accept

- name: Some Policy
  fortios_ipv4_policy:
    host: 192.168.0.254
    username: admin
    password: password
    id: 42
    comment: "no comment (created by ansible)"
    src_intf: vl1000
    src_addr:
      - some_serverA
      - some_serverB
    dst_intf:
      - vl2000
      - vl3000
    dst_addr: all
    services:
      - HTTP
      - HTTPS
    nat: True
    state: present
    policy_action: accept
    logtraffic: disable
  tags:
    - policy

```

## License

TODO

## Author Information
  - ['Benjamin Jolivot (@bjolivot)']
