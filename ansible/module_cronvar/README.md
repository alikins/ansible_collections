# Ansible module: ansible.module_cronvar


Manage variables in crontabs

## Description

Use this module to manage crontab variables. This module allows you to create, update, or delete cron variable definitions.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['If set, create a backup of the crontab before it is modified. The location of the backup is returned in the C(backup) variable by this module.'], 'type': 'bool', 'default': False}",
    "cron_file": "{'description': ["If specified, uses this file instead of an individual user's crontab. Without a leading /, this is assumed to be in /etc/cron.d.  With a leading /, this is taken as absolute."]}",
    "insertafter": "{'description': ['If specified, the variable will be inserted after the variable specified.', 'Used with C(state=present).']}",
    "insertbefore": "{'description': ['Used with C(state=present). If specified, the variable will be inserted just before the variable specified.']}",
    "name": "{'description': ['Name of the crontab variable.'], 'required': True}",
    "state": "{'description': ['Whether to ensure that the variable is present or absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "user": "{'description': ['The specific user whose crontab should be modified.'], 'default': 'root'}",
    "value": "{'description': ['The value to set this variable to.', 'Required if C(state=present).']}",
}
```

## Examples


``` yaml

- name: Ensure entry like "EMAIL=doug@ansibmod.con.com" exists
  cronvar:
    name: EMAIL
    value: doug@ansibmod.con.com

- name: Ensure a variable does not exist. This may remove any variable named "LEGACY"
  cronvar:
    name: LEGACY
    state: absent

- name: Add a variable to a file under /etc/cron.d
  cronvar:
    name: LOGFILE
    value: /var/log/yum-autoupdate.log
    user: root
    cron_file: ansible_yum-autoupdate

```

## License

TODO

## Author Information
  - ['Doug Luce (@dougluce)']
