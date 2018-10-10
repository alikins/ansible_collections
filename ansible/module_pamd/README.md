# Ansible module: ansible.module_pamd


Manage PAM Modules

## Description

Edit PAM service's type, control, module path and module arguments. In order for a PAM rule to be modified, the type, control and module_path must match an existing rule.  See man(5) pam.d for details.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "control": "{'required': True, 'description': ['The control of the PAM rule being modified.  This may be a complicated control with brackets.  If this is the case, be sure to put "[bracketed controls]" in quotes.  The type, control and module_path all must match a rule to be modified.']}",
    "module_arguments": "{'description': ["When state is 'updated', the module_arguments will replace existing module_arguments.  When state is 'args_absent' args matching those listed in module_arguments will be removed.  When state is 'args_present' any args listed in module_arguments are added if missing from the existing rule.  Furthermore, if the module argument takes a value denoted by '=', the value will be changed to that specified in module_arguments.  Note that module_arguments is a list.  Please see the examples for usage."]}",
    "module_path": "{'required': True, 'description': ['The module path of the PAM rule being modified.  The type, control and module_path all must match a rule to be modified.']}",
    "name": "{'required': True, 'description': ['The name generally refers to the PAM service file to change, for example system-auth.']}",
    "new_control": "{'description': ['The new control to assign to the new rule.']}",
    "new_module_path": "{'description': ['The new module path to be assigned to the new rule.']}",
    "new_type": "{'description': ['The new type to assign to the new rule.']}",
    "path": "{'default': '/etc/pam.d/', 'description': ['This is the path to the PAM service files']}",
    "state": "{'default': 'updated', 'choices': ['updated', 'before', 'after', 'args_present', 'args_absent', 'absent'], 'description': ["The default of 'updated' will modify an existing rule if type, control and module_path all match an existing rule.  With 'before', the new rule will be inserted before a rule matching type, control and module_path.  Similarly, with 'after', the new rule will be inserted after an existing rule matching type, control and module_path.  With either 'before' or 'after' new_type, new_control, and new_module_path must all be specified.  If state is 'args_absent' or 'args_present', new_type, new_control, and new_module_path will be ignored.  State 'absent' will remove the rule.  The 'absent' state was added in version 2.4 and is only available in Ansible versions >= 2.4."]}",
    "type": "{'required': True, 'description': ['The type of the PAM rule being modified.  The type, control and module_path all must match a rule to be modified.']}",
}
```

## Examples


``` yaml

- name: Update pamd rule's control in /etc/pam.d/system-auth
  pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    new_control: sufficient

- name: Update pamd rule's complex control in /etc/pam.d/system-auth
  pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    new_control: '[success=2 default=ignore]'

- name: Insert a new rule before an existing rule
  pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    new_type: auth
    new_control: sufficient
    new_module_path: pam_faillock.so
    state: before

- name: Insert a new rule pam_wheel.so with argument 'use_uid' after an         existing rule pam_rootok.so
  pamd:
    name: su
    type: auth
    control: sufficient
    module_path: pam_rootok.so
    new_type: auth
    new_control: required
    new_module_path: pam_wheel.so
    module_arguments: 'use_uid'
    state: after

- name: Remove module arguments from an existing rule
  pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: ''
    state: updated

- name: Replace all module arguments in an existing rule
  pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: 'preauth
        silent
        deny=3
        unlock_time=604800
        fail_interval=900'
    state: updated

- name: Remove specific arguments from a rule
  pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments: crond,quiet
    state: args_absent

- name: Ensure specific arguments are present in a rule
  pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments: crond,quiet
    state: args_present

- name: Ensure specific arguments are present in a rule (alternative)
  pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments:
    - crond
    - quiet
    state: args_present

- name: Module arguments requiring commas must be listed as a Yaml list
  pamd:
    name: special-module
    type: account
    control: required
    module_path: pam_access.so
    module_arguments:
    - listsep=,
    state: args_present

- name: Update specific argument value in a rule
  pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: 'fail_interval=300'
    state: args_present

- name: Add pam common-auth rule for duo
  pamd:
    name: common-auth
    new_type: auth
    new_control: '[success=1 default=ignore]'
    new_module_path: '/lib64/security/pam_duo.so'
    state: after
    type: auth
    module_path: pam_sss.so
    control: 'requisite'

```

## License

TODO

## Author Information
  - ['Kenneth D. Evensen (@kevensen)']
