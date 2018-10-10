# Ansible module: ansible.module_infini_pool


Create, Delete and Modify Pools on Infinibox

## Description

This module to creates, deletes or modifies pools on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Pool Name'], 'required': True}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "size": "{'description': ['Pool Physical Capacity in MB, GB or TB units. If pool size is not set on pool creation, size will be equal to 1TB. See examples.'], 'required': False}",
    "ssd_cache": "{'description': ['Enable/Disable SSD Cache on Pool'], 'required': False, 'default': True, 'type': 'bool'}",
    "state": "{'description': ['Creates/Modifies Pool when present or removes when absent'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
    "vsize": "{'description': ['Pool Virtual Capacity in MB, GB or TB units. If pool vsize is not set on pool creation, Virtual Capacity will be equal to Physical Capacity. See examples.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Make sure pool foo exists. Set pool physical capacity to 10TB
  infini_pool:
    name: foo
    size: 10TB
    vsize: 10TB
    user: admin
    password: secret
    system: ibox001

- name: Disable SSD Cache on pool
  infini_pool:
    name: foo
    ssd_cache: no
    user: admin
    password: secret
    system: ibox001

```

## License

TODO

## Author Information
  - ['Gregory Shulov (@GR360RY)']
