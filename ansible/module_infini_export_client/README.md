# Ansible module: ansible.module_infini_export_client


Create, Delete or Modify NFS Client(s) for existing exports on Infinibox

## Description

This module creates, deletes or modifys NFS client(s) for existing exports on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "access_mode": "{'description': ['Read Write or Read Only Access.'], 'choices': ['RW', 'RO'], 'default': 'RW', 'required': False}",
    "client": "{'description': ['Client IP or Range. Ranges can be defined as follows 192.168.0.1-192.168.0.254.'], 'aliases': ['name'], 'required': True}",
    "export": "{'description': ['Name of the export.'], 'required': True}",
    "no_root_squash": "{'description': ['Don\'t squash root user to anonymous. Will be set to "no" on creation if not specified explicitly.'], 'type': 'bool', 'default': False, 'required': False}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "state": "{'description': ['Creates/Modifies client when present and removes when absent.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
}
```

## Examples


``` yaml

- name: Make sure nfs client 10.0.0.1 is configured for export. Allow root access
  infini_export_client:
    client: 10.0.0.1
    access_mode: RW
    no_root_squash: yes
    export: /data
    user: admin
    password: secret
    system: ibox001

- name: Add multiple clients with RO access. Squash root privileges
  infini_export_client:
    client: "{{ item }}"
    access_mode: RO
    no_root_squash: no
    export: /data
    user: admin
    password: secret
    system: ibox001
  with_items:
    - 10.0.0.2
    - 10.0.0.3

```

## License

TODO

## Author Information
  - ['Gregory Shulov (@GR360RY)']
