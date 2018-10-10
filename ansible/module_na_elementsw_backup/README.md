# Ansible module: ansible.module_na_elementsw_backup


NetApp Element Software Create Backups

## Description

Create backup

## Requirements

TODO

## Arguments

``` json
{
    "dest_hostname": "{'description': ['hostname for the backup source cluster', 'will be set equal to src_hostname if not specified'], 'required': False}",
    "dest_password": "{'description': ['password for the backup destination cluster', 'will be set equal to src_password if not specified'], 'required': False}",
    "dest_username": "{'description': ['username for the backup destination cluster', 'will be set equal to src_username if not specified'], 'required': False}",
    "dest_volume_id": "{'description': ['ID of the backup destination volume'], 'required': True}",
    "format": "{'description': ['Backup format to use'], 'choices': ['native', 'uncompressed'], 'required': False, 'default': 'native'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "script": "{'description': ['the backup script to be executed'], 'required': False}",
    "script_parameters": "{'description': ['the backup script parameters'], 'required': False}",
    "src_hostname": "{'description': ['hostname for the backup source cluster'], 'required': True, 'aliases': ['hostname']}",
    "src_password": "{'description': ['password for the backup source cluster'], 'required': True, 'aliases': ['password', 'pass']}",
    "src_username": "{'description': ['username for the backup source cluster'], 'required': True, 'aliases': ['username', 'user']}",
    "src_volume_id": "{'description': ['ID of the backup source volume.'], 'required': True, 'aliases': ['volume_id']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

na_elementsw_backup:
  src_hostname: "{{ source_cluster_hostname }}"
  src_username: "{{ source_cluster_username }}"
  src_password: "{{ source_cluster_password }}"
  src_volume_id: 1
  dest_hostname: "{{ destination_cluster_hostname }}"
  dest_username: "{{ destination_cluster_username }}"
  dest_password: "{{ destination_cluster_password }}"
  dest_volume_id: 3
  format: native

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
