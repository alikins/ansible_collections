# Ansible module: ansible.module_purefa_pgsnap


Manage local protection group snapshots on Pure Storage FlashArrays

## Description

Create or delete local protection group snapshots on Pure Storage FlashArray.
This module only supports local protection groups.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "eradicate": "{'description': ['Define whether to eradicate the snapshot on delete or leave in trash.'], 'type': 'bool', 'default': False}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "name": "{'description': ['The name of the source protection group.'], 'required': True}",
    "restore": "{'description': ['Restore a specific volume from a protection group snapshot. This implies overwrite of the current full volume. USE WITH CARE!!'], 'version_added': 2.7}",
    "state": "{'description': ['Define whether the protection group snapshot should exist or not. Copy (added in 2.7) will force an overwrite of an exisitng volume from a snapshot.'], 'choices': ['absent', 'present', 'copy'], 'default': 'present'}",
    "suffix": "{'description': ['Suffix of snapshot name.']}",
}
```

## Examples


``` yaml

- name: Create protection group snapshot foo.ansible
  purefa_pgsnap:
    name: foo
    suffix: ansible
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate protection group snapshot named foo.snap
  purefa_pgsnap:
    name: foo
    suffix: snap
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Restore volume data from protection group snapshot named foo.snap
        USE WITH CARE! This will overwrite your existing volume
  purefa_pgsnap:
    name: foo
    suffix: snap
    restore: data
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
