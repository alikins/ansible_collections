# Ansible module: ansible.module_infini_vol


Create, Delete or Modify volumes on Infinibox

## Description

This module creates, deletes or modifies volume on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Volume Name'], 'required': True}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "pool": "{'description': ['Pool that volume will reside on'], 'required': True}",
    "size": "{'description': ['Volume size in MB, GB or TB units. See examples.'], 'required': False}",
    "state": "{'description': ['Creates/Modifies volume when present or removes when absent'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create new volume named foo under pool named bar
  infini_vol:
    name: foo
    size: 1TB
    pool: bar
    state: present
    user: admin
    password: secret
    system: ibox001

```

## License

TODO

## Author Information
  - ['Gregory Shulov (@GR360RY)']
