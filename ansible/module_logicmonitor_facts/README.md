# Ansible module: ansible.module_logicmonitor_facts


Collect facts about LogicMonitor objects

## Description

LogicMonitor is a hosted, full-stack, infrastructure monitoring platform.
This module collects facts about hosts and host groups within your LogicMonitor account.

## Requirements

TODO

## Arguments

``` json
{
    "collector": "{'description': ['The fully qualified domain name of a collector in your LogicMonitor account.', 'This is optional for querying a LogicMonitor host when a displayname is specified.', 'This is required for querying a LogicMonitor host when a displayname is not specified.']}",
    "company": "{'description': ['The LogicMonitor account company name. If you would log in to your account at "superheroes.logicmonitor.com" you would use "superheroes".'], 'required': True}",
    "displayname": "{'description': ['The display name of a host in your LogicMonitor account or the desired display name of a device to add into monitoring.'], 'default': 'hostname -f'}",
    "fullpath": "{'description': ['The fullpath of the hostgroup object you would like to manage.', 'Recommend running on a single ansible host.', 'Required for management of LogicMonitor host groups (target=hostgroup).']}",
    "hostname": "{'description': ['The hostname of a host in your LogicMonitor account, or the desired hostname of a device to add into monitoring.', 'Required for managing hosts (target=host).'], 'default': 'hostname -f'}",
    "password": "{'description': ['The password for the chosen LogicMonitor User.', 'If an md5 hash is used, the digest flag must be set to true.'], 'required': True}",
    "target": "{'description': ['The LogicMonitor object you wish to manage.'], 'required': True, 'choices': ['host', 'hostgroup']}",
    "user": "{'description': ['A LogicMonitor user name. The module will authenticate and perform actions on behalf of this user.'], 'required': True}",
}
```

## Examples


``` yaml

# Always run those modules on localhost using delegate_to:localhost, or localaction

- name: query a list of hosts
  logicmonitor_facts:
    target: host
    company: yourcompany
    user: Luigi
    password: ImaLuigi,number1!
  delegate_to: localhost

- name: query a host group
  logicmonitor_facts:
    target: hostgroup
    fullpath: /servers/production
    company: yourcompany
    user: mario
    password: itsame.Mario!
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ethan Culler-Mayeno (@ethanculler)', 'Jeff Wozniak (@woz5999)']
  - ['Ethan Culler-Mayeno (@ethanculler)', 'Jeff Wozniak (@woz5999)']
