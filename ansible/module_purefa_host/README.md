# Ansible module: ansible.module_purefa_host


Manage hosts on Pure Storage FlashArrays

## Description

Create, delete or modify hosts on Pure Storage FlashArrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "host": "{'description': ['The name of the host.'], 'required': True}",
    "iqn": "{'description': ['List of IQNs of the host if protocol is iscsi or mixed.']}",
    "personality": "{'description': ['Define which operating systen the host is. Recommend for ActiveCluster integration'], 'choices': ['hpux', 'vms', 'aix', 'esxi', 'solaris', 'hitachi-vsp', 'oracle-vm-server', ''], 'version_added': '2.7'}",
    "protocol": "{'description': ['Defines the host connection protocol for volumes.'], 'default': 'iscsi', 'choices': ['fc', 'iscsi', 'mixed']}",
    "state": "{'description': ['Define whether the host should exist or not.', 'When removing host all connected volumes will be disconnected.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "volume": "{'description': ['Volume name to map to the host.']}",
    "wwns": "{'description': ['List of wwns of the host if protocol is fc or mixed.']}",
}
```

## Examples


``` yaml

- name: Create new AIX host
  purefa_host:
    host: foo
    personaility: aix
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete host
  purefa_host:
    host: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Make host bar with wwn ports
  purefa_host:
    host: bar
    protocol: fc
    wwns:
    - 00:00:00:00:00:00:00
    - 11:11:11:11:11:11:11
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Make host bar with iSCSI ports
  purefa_host:
    host: bar
    protocol: iscsi
    iqn:
    - iqn.1994-05.com.redhat:7d366003913
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Make mixed protocol host
  purefa_host:
    host: bar
    protocol: mixed
    iqn:
    - iqn.1994-05.com.redhat:7d366003914
    wwns:
    - 00:00:00:00:00:00:01
    - 11:11:11:11:11:11:12
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Map host foo to volume bar
  purefa_host:
    host: foo
    volume: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
