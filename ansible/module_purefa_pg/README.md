# Ansible module: ansible.module_purefa_pg


Manage protection groups on Pure Storage FlashArrays

## Description

Create, delete or modify protection groups on Pure Storage FlashArrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "enabled": "{'description': ['Define whether to enabled snapshots for the protection group.'], 'type': 'bool', 'default': True}",
    "eradicate": "{'description': ['Define whether to eradicate the protection group on delete and leave in trash.'], 'type': 'bool', 'default': False}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "host": "{'description': ['List of existing hosts to add to protection group.']}",
    "hostgroup": "{'description': ['List of existing hostgroups to add to protection group.']}",
    "pgroup": "{'description': ['The name of the protection group.'], 'required': True}",
    "state": "{'description': ['Define whether the protection group should exist or not.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "volume": "{'description': ['List of existing volumes to add to protection group.']}",
}
```

## Examples


``` yaml

- name: Create new protection group
  purefa_pg:
    pgroup: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create new protection group with snapshots disabled
  purefa_pg:
    pgroup: foo
    enabled: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete protection group
  purefa_pg:
    pgroup: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Create protection group for hostgroups
  purefa_pg:
    pgroup: bar
    hostgroup:
      - hg1
      - hg2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create protection group for hosts
  purefa_pg:
    pgroup: bar
    host:
      - host1
      - host2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create protection group for volumes
  purefa_pg:
    pgroup: bar
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
