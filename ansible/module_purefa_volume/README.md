# Ansible module: ansible.module_purefa_volume


Manage volumes on Pure Storage FlashArrays

## Description

Create, delete or extend the capacity of a volume on Pure Storage FlashArray.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "eradicate": "{'description': ['Define whether to eradicate the volume on delete or leave in trash.'], 'type': 'bool', 'default': False}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "name": "{'description': ['The name of the volume.'], 'required': True}",
    "overwrite": "{'description': ['Define whether to overwrite a target volume if it already exisits.'], 'type': 'bool', 'default': False}",
    "size": "{'description': ['Volume size in M, G, T or P units.']}",
    "state": "{'description': ['Define whether the volume should exist or not.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "target": "{'description': ['The name of the target volume, if copying.']}",
}
```

## Examples


``` yaml

- name: Create new volume named foo
  purefa_volume:
    name: foo
    size: 1T
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Extend the size of an existing volume named foo
  purefa_volume:
    name: foo
    size: 2T
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate volume named foo
  purefa_volume:
    name: foo
    eradicate: yes
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Create clone of volume bar named foo
  purefa_volume:
    name: foo
    target: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Overwrite volume bar with volume foo
  purefa_volume:
    name: foo
    target: bar
    overwrite: yes
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
