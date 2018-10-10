# Ansible module: ansible.module_icinga2_feature


Manage Icinga2 feature

## Description

This module can be used to enable or disable an Icinga2 feature.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['This is the feature name to enable or disable.'], 'required': True}",
    "state": "{'description': ['If set to C(present) and feature is disabled, then feature is enabled.', 'If set to C(present) and feature is already enabled, then nothing is changed.', 'If set to C(absent) and feature is enabled, then feature is disabled.', 'If set to C(absent) and feature is already disabled, then nothing is changed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Enable ido-pgsql feature
  icinga2_feature:
    name: ido-pgsql
    state: present

- name: Disable api feature
  icinga2_feature:
    name: api
    state: absent

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
