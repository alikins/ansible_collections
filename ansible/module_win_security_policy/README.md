# Ansible module: ansible.module_win_security_policy


Change local security policy settings

## Description

Allows you to set the local security policies that are configured by SecEdit.exe.

## Requirements

TODO

## Arguments

``` json
{
    "key": "{'description': ['The ini key of the section or policy name to modify.', 'The module will return an error if this key is invalid.'], 'required': True}",
    "section": "{'description': ['The ini section the key exists in.', 'If the section does not exist then the module will return an error.', "Example sections to use are 'Account Policies', 'Local Policies', 'Event Log', 'Restricted Groups', 'System Services', 'Registry' and 'File System'"], 'required': True}",
    "value": "{'description': ['The value for the ini key or policy name.', 'If the key takes in a boolean value then 0 = False and 1 = True.'], 'required': True}",
}
```

## Examples


``` yaml

- name: change the guest account name
  win_security_policy:
    section: System Access
    key: NewGuestName
    value: Guest Account

- name: set the maximum password age
  win_security_policy:
    section: System Access
    key: MaximumPasswordAge
    value: 15

- name: do not store passwords using reversible encryption
  win_security_policy:
    section: System Access
    key: ClearTextPassword
    value: 0

- name: enable system events
  win_security_policy:
    section: Event Audit
    key: AuditSystemEvents
    value: 1

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
