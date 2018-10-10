# Ansible module: ansible.module_infini_host


Create, Delete and Modify Hosts on Infinibox

## Description

This module creates, deletes or modifies hosts on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Host Name'], 'required': True}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "state": "{'description': ['Creates/Modifies Host when present or removes when absent'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
    "volume": "{'description': ['Volume name to map to the host'], 'required': False}",
    "wwns": "{'description': ['List of wwns of the host'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create new new host
  infini_host:
    name: foo.example.com
    user: admin
    password: secret
    system: ibox001

- name: Make sure host bar is available with wwn ports
  infini_host:
    name: bar.example.com
    wwns:
      - "00:00:00:00:00:00:00"
      - "11:11:11:11:11:11:11"
    system: ibox01
    user: admin
    password: secret

- name: Map host foo.example.com to volume bar
  infini_host:
    name: foo.example.com
    volume: bar
    system: ibox01
    user: admin
    password: secret

```

## License

TODO

## Author Information
  - ['Gregory Shulov (@GR360RY)']
