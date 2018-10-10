# Ansible module: ansible.module_purefb_fs


Manage filesystemon Pure Storage FlashBlade`

## Description

This module manages filesystems on Pure Storage FlashBlade.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashBlade API token for admin privileged user.']}",
    "eradicate": "{'description': ['Define whether to eradicate the filesystem on delete or leave in trash.'], 'required': False, 'type': 'bool', 'default': False}",
    "fastremove": "{'description': ['Define whether the fast remove directory is enabled for the filesystem.'], 'required': False, 'type': 'bool', 'default': False}",
    "fb_url": "{'description': ['FlashBlade management IP address or Hostname.']}",
    "http": "{'description': ['Define whether to HTTP/HTTPS protocol is enabled for the filesystem.'], 'required': False, 'type': 'bool', 'default': False}",
    "name": "{'description': ['Filesystem Name.'], 'required': True}",
    "nfs": "{'description': ['Define whether to NFS protocol is enabled for the filesystem.'], 'required': False, 'type': 'bool', 'default': True}",
    "nfs_rules": "{'description': ['Define the NFS rules in operation.'], 'required': False, 'default': '*(rw,no_root_squash)'}",
    "size": "{'description': ['Volume size in M, G, T or P units. See examples.'], 'required': False, 'default': '32G'}",
    "smb": "{'description': ['Define whether to SMB protocol is enabled for the filesystem.'], 'required': False, 'type': 'bool', 'default': False}",
    "snapshot": "{'description': ['Define whether a snapshot directory is enabled for the filesystem.'], 'required': False, 'type': 'bool', 'default': False}",
    "state": "{'description': ['Create, delete or modifies a filesystem.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Create new filesystem named foo
  purefb_fs:
    name: foo
    size: 1T
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete filesystem named foo
  purefb_fs:
    name: foo
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Recover filesystem named foo
  purefb_fs:
    name: foo
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Eradicate filesystem named foo
  purefb_fs:
    name: foo
    state: absent
    eradicate: true
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Modify attributes of an existing filesystem named foo
  purefb_fs:
    name: foo

    size: 2T
    nfs : true
    nfs_rules: '*(ro)'
    snapshot: true
    fastremove: true
    smb: true
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
