# Ansible module: ansible.module_apt_rpm


apt_rpm package manager

## Description

Manages packages with I(apt-rpm). Both low-level (I(rpm)) and high-level (I(apt-get)) package manager binaries required.

## Requirements

TODO

## Arguments

``` json
{
    "pkg": "{'description': ['name of package to install, upgrade or remove.'], 'required': True}",
    "state": "{'description': ['Indicates the desired package state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "update_cache": "{'description': ['update the package database first C(apt-get update).'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Install package foo
  apt_rpm:
    pkg: foo
    state: present

- name: Remove package foo
  apt_rpm:
    pkg: foo
    state: absent

- name: Remove packages foo and bar
  apt_rpm:
    pkg: foo,bar
    state: absent

# bar will be the updated if a newer version exists
- name: Update the package database and install bar
  apt_rpm:
    name: bar
    state: present
    update_cache: yes

```

## License

TODO

## Author Information
  - ['Evgenii Terechkov (@evgkrsk)']
