# Ansible module: ansible.module_purefa_snap


Manage volume snapshots on Pure Storage FlashArrays

## Description

Create or delete volumes and volume snapshots on Pure Storage FlashArray.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "eradicate": "{'description': ['Define whether to eradicate the snapshot on delete or leave in trash.'], 'type': 'bool', 'default': False}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "name": "{'description': ['The name of the source volume.'], 'required': True}",
    "overwrite": "{'description': ['Define whether to overwrite existing volume when creating from snapshot.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Define whether the volume snapshot should exist or not.'], 'choices': ['absent', 'copy', 'present'], 'default': 'present'}",
    "suffix": "{'description': ['Suffix of snapshot name.']}",
    "target": "{'description': ['Name of target volume if creating from snapshot.']}",
}
```

## Examples


``` yaml

- name: Create snapshot foo.ansible
  purefa_snap:
    name: foo
    suffix: ansible
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create R/W clone foo_clone from snapshot foo.snap
  purefa_snap:
    name: foo
    suffix: snap
    target: foo_clone
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Overwrite existing volume foo_clone with snapshot foo.snap
  purefa_snap:
    name: foo
    suffix: snap
    target: foo_clone
    overwrite: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Delete and eradicate snapshot named foo.snap
  purefa_snap:
    name: foo
    suffix: snap
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
