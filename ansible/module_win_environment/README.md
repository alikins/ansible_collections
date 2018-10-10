# Ansible module: ansible.module_win_environment


Modify environment variables on windows hosts

## Description

Uses .net Environment to set or remove environment variables and can set at User, Machine or Process level.
User level environment variables will be set, but not available until the user has logged off and on again.

## Requirements

TODO

## Arguments

``` json
{
    "level": "{'description': ['The level at which to set the environment variable.', 'Use C(machine) to set for all users.', 'Use C(user) to set for the current user that ansible is connected as.', 'Use C(process) to set for the current process.  Probably not that useful.'], 'choices': ['machine', 'user', 'process'], 'required': True}",
    "name": "{'description': ['The name of the environment variable.'], 'required': True}",
    "state": "{'description': ['Set to C(present) to ensure environment variable is set.', 'Set to C(absent) to ensure it is removed.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "value": "{'description': ['The value to store in the environment variable.', 'Must be set when C(state=present) and cannot be an empty string.', 'Can be omitted for C(state=absent).']}",
}
```

## Examples


``` yaml

- name: Set an environment variable for all users
  win_environment:
    state: present
    name: TestVariable
    value: Test value
    level: machine

- name: Remove an environment variable for the current user
  win_environment:
    state: absent
    name: TestVariable
    level: user

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
