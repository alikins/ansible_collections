# Ansible module: ansible.module_infini_export


Create, Delete or Modify NFS Exports on Infinibox

## Description

This module creates, deletes or modifies NFS exports on Infinibox.

## Requirements

TODO

## Arguments

``` json
{
    "client_list": "{'description': ['List of dictionaries with client entries. See examples. Check infini_export_client module to modify individual NFS client entries for export.'], 'default': 'All Hosts(*), RW, no_root_squash: True', 'required': False}",
    "filesystem": "{'description': ['Name of exported file system.'], 'required': True}",
    "inner_path": "{'description': ['Internal path of the export.'], 'default': '/'}",
    "name": "{'description': ['Export name. Should always start with C(/). (ex. name=/data)'], 'aliases': ['export', 'path'], 'required': True}",
    "password": "{'description': ['Infinibox User password.'], 'required': False}",
    "state": "{'description': ['Creates/Modifies export when present and removes when absent.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "system": "{'description': ['Infinibox Hostname or IPv4 Address.'], 'required': True}",
    "user": "{'description': ['Infinibox User username with sufficient priveledges ( see notes ).'], 'required': False}",
}
```

## Examples


``` yaml

- name: Export bar filesystem under foo pool as /data
  infini_export:
    name: /data01
    filesystem: foo
    user: admin
    password: secret
    system: ibox001

- name: Export and specify client list explicitly
  infini_export:
    name: /data02
    filesystem: foo
    client_list:
      - client: 192.168.0.2
        access: RW
        no_root_squash: True
      - client: 192.168.0.100
        access: RO
        no_root_squash: False
      - client: 192.168.0.10-192.168.0.20
        access: RO
        no_root_squash: False
    system: ibox001
    user: admin
    password: secret

```

## License

TODO

## Author Information
  - ['Gregory Shulov (@GR360RY)']
