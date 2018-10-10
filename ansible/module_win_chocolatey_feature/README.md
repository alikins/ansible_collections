# Ansible module: ansible.module_win_chocolatey_feature


Manages Chocolatey features

## Description

Used to enable or disable features in Chocolatey.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the feature to manage.', 'Run C(choco.exe feature list) to get a list of features that can be managed.'], 'required': True}",
    "state": "{'description': ['When C(disabled) then the feature will be disabled.', 'When C(enabled) then the feature will be enabled.'], 'choices': ['disabled', 'enabled'], 'default': 'enabled'}",
}
```

## Examples


``` yaml

- name: disable file checksum matching
  win_chocolatey_feature:
    name: checksumFiles
    state: disabled

- name: stop Chocolatey on the first package failure
  win_chocolatey_feature:
    name: stopOnFirstPackageFailure
    state: enabled

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
