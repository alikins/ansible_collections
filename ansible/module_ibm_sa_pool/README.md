# Ansible module: ansible.module_ibm_sa_pool


Handles pools on an IBM Spectrum Accelerate storage array

## Description

This module creates or deletes pools to be used on IBM Spectrum Accelerate storage systems.

## Requirements

TODO

## Arguments

``` json
{
    "domain": "{'description': ['Adds the pool to the specified domain.'], 'required': False}",
    "endpoints": "{'description': ['The hostname or management IP of Spectrum Accelerate storage system.'], 'required': True}",
    "password": "{'description': ['Password for username on the spectrum accelerate storage system.'], 'required': True}",
    "perf_class": "{'description': ['Assigns a perf_class to the pool.'], 'required': False}",
    "pool": "{'description': ['Pool name.'], 'required': True}",
    "size": "{'description': ['Pool size in GB'], 'required': False}",
    "snapshot_size": "{'description': ['Pool snapshot size in GB'], 'required': False}",
    "state": "{'description': ['Pool state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['Management user on the spectrum accelerate storage system.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create new pool.
  ibm_sa_pool:
    name: pool_name
    size: 300
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete pool.
  ibm_sa_pool:
    name: pool_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system

```

## License

TODO

## Author Information
  - ['Tzur Eliyahu (tzure@il.ibm.com)']
