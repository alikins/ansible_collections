# Ansible module: ansible.module_purefb_snap


Manage filesystem snapshots on Pure Storage FlashBlades

## Description

Create or delete volumes and filesystem snapshots on Pure Storage FlashBlades.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashBlade API token for admin privileged user.']}",
    "eradicate": "{'description': ['Define whether to eradicate the snapshot on delete or leave in trash.'], 'type': 'bool', 'default': False}",
    "fb_url": "{'description': ['FlashBlade management IP address or Hostname.']}",
    "name": "{'description': ['The name of the source filesystem.'], 'required': True}",
    "state": "{'description': ['Define whether the filesystem snapshot should exist or not.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "suffix": "{'description': ['Suffix of snapshot name.']}",
}
```

## Examples


``` yaml

- name: Create snapshot foo.ansible
  purefb_snap:
    name: foo
    suffix: ansible
    fb_url: 10.10.10.2
    fb_api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete snapshot named foo.snap
  purefb_snap:
    name: foo
    suffix: snap
    fb_url: 10.10.10.2
    fb_api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Recover deleted snapshot foo.ansible
  purefb_snap:
    name: foo
    suffix: ansible
    fb_url: 10.10.10.2
    fb_api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Eradicate snapshot named foo.snap
  purefb_snap:
    name: foo
    suffix: snap
    eradicate: true
    fb_url: 10.10.10.2
    fb_api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
