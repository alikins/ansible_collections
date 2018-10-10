# Ansible module: ansible.module_urpmi


Urpmi manager

## Description

Manages packages with I(urpmi) (such as for Mageia or Mandriva)

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Assume "yes" is the answer to any question urpmi has to ask. Corresponds to the C(--force) option for I(urpmi).'], 'type': 'bool', 'default': True}",
    "name": "{'description': ['A list of package names to install, upgrade or remove.'], 'required': True, 'version_added': '2.6', 'aliases': ['package', 'pkg']}",
    "no-recommends": "{'description': ['Corresponds to the C(--no-recommends) option for I(urpmi).'], 'type': 'bool', 'default': True, 'aliases': ['no-recommends']}",
    "root": "{'description': ['Specifies an alternative install root, relative to which all packages will be installed. Corresponds to the C(--root) option for I(urpmi).'], 'default': '/', 'version_added': '2.4', 'aliases': ['installroot']}",
    "state": "{'description': ['Indicates the desired package state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "update_cache": "{'description': ['Update the package database first C(urpmi.update -a).'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Install package foo
  urpmi:
    pkg: foo
    state: present

- name: Remove package foo
  urpmi:
    pkg: foo
    state: absent

- name: Remove packages foo and bar
  urpmi:
    pkg: foo,bar
    state: absent

- name: Update the package database (urpmi.update -a -q) and install bar (bar will be the updated if a newer version exists)
- urpmi:
    name: bar
    state: present
    update_cache: yes

```

## License

TODO

## Author Information
  - ['Philippe Makowski (@pmakowski)']
