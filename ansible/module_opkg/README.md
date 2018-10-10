# Ansible module: ansible.module_opkg


Package manager for OpenWrt

## Description

Manages OpenWrt packages

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['opkg --force parameter used'], 'choices': ['', 'depends', 'maintainer', 'reinstall', 'overwrite', 'downgrade', 'space', 'postinstall', 'remove', 'checksum', 'removal-of-dependent-packages'], 'default': 'absent', 'version_added': '2.0'}",
    "name": "{'description': ['name of package to install/remove'], 'required': True}",
    "state": "{'description': ['state of the package'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "update_cache": "{'description': ['update the package db first'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

- opkg:
    name: foo
    state: present

- opkg:
    name: foo
    state: present
    update_cache: yes

- opkg:
    name: foo
    state: absent

- opkg:
    name: foo,bar
    state: absent

- opkg:
    name: foo
    state: present
    force: overwrite

```

## License

TODO

## Author Information
  - ['Patrick Pelletier (@skinp)']
