# Ansible module: ansible.module_mksysb


Generates AIX mksysb rootvg backups

## Description

This module manages a basic AIX mksysb (image) of rootvg.

## Requirements

TODO

## Arguments

``` json
{
    "backup_crypt_files": "{'description': ['Backup encrypted files.'], 'type': 'bool', 'default': True}",
    "backup_dmapi_fs": "{'description': ['Back up DMAPI filesystem files.'], 'type': 'bool', 'default': True}",
    "create_map_files": "{'description': ['Creates a new MAP files.'], 'type': 'bool', 'default': False}",
    "exclude_files": "{'description': ['Excludes files using C(/etc/rootvg.exclude).'], 'type': 'bool', 'default': False}",
    "exclude_wpar_files": "{'description': ['Excludes WPAR files.'], 'type': 'bool', 'default': False}",
    "extended_attrs": "{'description': ['Backup extended attributes.'], 'type': 'bool', 'default': True}",
    "name": "{'description': ['Backup name'], 'required': True}",
    "new_image_data": "{'description': ['Creates a new file data.'], 'type': 'bool', 'default': True}",
    "software_packing": "{'description': ['Exclude files from packing option listed in C(/etc/exclude_packing.rootvg).'], 'type': 'bool', 'default': False}",
    "storage_path": "{'description': ['Storage path where the mksysb will stored.'], 'required': True}",
    "use_snapshot": "{'description': ['Creates backup using snapshots.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Running a backup image mksysb
  mksysb:
    name: myserver
    storage_path: /repository/images
    exclude_files: yes
    exclude_wpar_files: yes

```

## License

TODO

## Author Information
  - ['Kairo Araujo (@kairoaraujo)']
