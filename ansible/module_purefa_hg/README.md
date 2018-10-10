# Ansible module: ansible.module_purefa_hg


Manage hostgroups on Pure Storage FlashArrays

## Description

Create, delete or modifiy hostgroups on Pure Storage FlashArrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "host": "{'description': ['List of existing hosts to add to hostgroup.']}",
    "hostgroup": "{'description': ['The name of the hostgroup.'], 'required': True}",
    "state": "{'description': ['Define whether the hostgroup should exist or not.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "volume": "{'description': ['List of existing volumes to add to hostgroup.']}",
}
```

## Examples


``` yaml

- name: Create empty hostgroup
  purefa_hg:
    hostgroup: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add hosts and volumes to existing or new hostgroup
  purefa_hg:
    hostgroup: foo
    host:
      - host1
      - host2
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete hosts and volumes from hostgroup
  purefa_hg:
    hostgroup: foo
    host:
      - host1
      - host2
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

# This will disconnect all hosts and volumes in the hostgroup
- name: Delete hostgroup
  purefa_hg:
    hostgroup: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Create host group with hosts and volumes
  purefa_hg:
    hostgroup: bar
    host:
      - host1
      - host2
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
