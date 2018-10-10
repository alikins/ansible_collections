# Ansible module: ansible.module_ibm_sa_vol


Handle volumes on an IBM Spectrum Accelerate storage array

## Description

This module creates or deletes volumes to be used on IBM Spectrum Accelerate storage systems.

## Requirements

TODO

## Arguments

``` json
{
    "endpoints": "{'description': ['The hostname or management IP of Spectrum Accelerate storage system.'], 'required': True}",
    "password": "{'description': ['Password for username on the spectrum accelerate storage system.'], 'required': True}",
    "pool": "{'description': ['Volume pool.'], 'required': False}",
    "size": "{'description': ['Volume size.'], 'required': False}",
    "state": "{'description': ['Volume state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['Management user on the spectrum accelerate storage system.'], 'required': True}",
    "vol": "{'description': ['Volume name.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a new volume.
  ibm_sa_vol:
    vol: volume_name
    pool: pool_name
    size: 17
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete an existing volume.
  ibm_sa_vol:
    vol: volume_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system

```

## License

TODO

## Author Information
  - ['Tzur Eliyahu (tzure@il.ibm.com)']
