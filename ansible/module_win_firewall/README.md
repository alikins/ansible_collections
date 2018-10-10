# Ansible module: ansible.module_win_firewall


Enable or disable the Windows Firewall

## Description

Enable or Disable Windows Firewall profiles.

## Requirements

TODO

## Arguments

``` json
{
    "profiles": "{'description': ['Specify one or more profiles to change.'], 'type': 'list', 'choices': ['Domain', 'Private', 'Public'], 'default': ['Domain', 'Private', 'Public']}",
    "state": "{'description': ['Set state of firewall for given profile.'], 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Enable firewall for Domain, Public and Private profiles
  win_firewall:
    state: enabled
    profiles:
    - Domain
    - Private
    - Public
  tags: enable_firewall

- name: Disable Domain firewall
  win_firewall:
    state: disabled
    profiles:
    - Domain
  tags: disable_firewall

```

## License

TODO

## Author Information
  - ['Michael Eaton (@if-meaton)']
