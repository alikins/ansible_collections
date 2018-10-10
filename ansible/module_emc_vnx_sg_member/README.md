# Ansible module: ansible.module_emc_vnx_sg_member


Manage storage group member on EMC VNX

## Description

This module manages the members of an existing storage group.

## Requirements

TODO

## Arguments

``` json
{
    "lunid": "{'description': ['Lun id to be added.'], 'required': True}",
    "name": "{'description': ['Name of the Storage group to manage.'], 'required': True}",
    "sp_address": "{'description': ['Address of the SP of target/secondary storage.'], 'required': True}",
    "sp_password": "{'description': ['password for accessing SP.'], 'default': 'sysadmin', 'required': False}",
    "sp_user": "{'description': ['Username for accessing SP.'], 'default': 'sysadmin', 'required': False}",
    "state": "{'description': ['Indicates the desired lunid state.', 'C(present) ensures specified lunid is present in the Storage Group.', 'C(absent) ensures specified lunid is absent from Storage Group.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Add lun to storage group
  emc_vnx_sg_member:
    name: sg01
    sp_address: sp1a.fqdn
    sp_user: sysadmin
    sp_password: sysadmin
    lunid: 100
    state: present

- name: Remove lun from storage group
  emc_vnx_sg_member:
    name: sg01
    sp_address: sp1a.fqdn
    sp_user: sysadmin
    sp_password: sysadmin
    lunid: 100
    state: absent

```

## License

TODO

## Author Information
  - ["Luca 'remix_tj' Lorenzetto (@remixtj)"]
