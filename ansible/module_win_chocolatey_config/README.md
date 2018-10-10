# Ansible module: ansible.module_win_chocolatey_config


Manages Chocolatey config settings

## Description

Used to manage Chocolatey config settings as well as unset the values.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the config setting to manage.', 'See U(https://chocolatey.org/docs/chocolatey-configuration) for a list of valid configuration settings that can be changed.', 'Any config values that contain encrypted values like a password are not idempotent as the plaintext value cannot be read.'], 'required': True}",
    "state": "{'description': ['When C(absent), it will ensure the setting is unset or blank.', 'When C(present), it will ensure the setting is set to the value of I(value).'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "value": "{'description': ['Used when C(state=present) that contains the value to set for the config setting.', 'Cannot be null or an empty string, use C(state=absent) to unset a config value instead.']}",
}
```

## Examples


``` yaml

- name: set the cache location
  win_chocolatey_config:
    name: cacheLocation
    state: present
    value: D:\chocolatey_temp

- name: unset the cache location
  win_chocolatey_config:
    name: cacheLocation
    state: absent

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
