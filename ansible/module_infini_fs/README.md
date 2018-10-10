# Ansible module: ansible.module_infini_fs


Create, Delete or Modify filesystems on Infinibox

## Description

This module creates, deletes or modifies filesystems on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['File system name.'], 'required': True}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "pool": "{'description': ['Pool that will host file system.'], 'required': True}",
    "size": "{'description': ['File system size in MB, GB or TB units. See examples.'], 'required': False}",
    "state": "{'description': ['Creates/Modifies file system when present or removes when absent.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create new file system named foo under pool named bar
  infini_fs:
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
