# Ansible module: ansible.module_pacman


Manage packages with *pacman*

## Description

Manage packages with the I(pacman) package manager, which is used by Arch Linux and its variants.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['When removing package - force remove package, without any checks. When update_cache - force redownload repo databases.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "name": "{'description': ['Name or list of names of the packages to install, upgrade, or remove.'], 'aliases': ['package', 'pkg']}",
    "recurse": "{'description': ['When removing a package, also remove its dependencies, provided that they are not required by other packages and were not explicitly installed by a user.'], 'type': 'bool', 'default': False, 'version_added': '1.3'}",
    "state": "{'description': ['Desired state of the package.'], 'default': 'present', 'choices': ['absent', 'latest', 'present']}",
    "update_cache": "{'description': ['Whether or not to refresh the master package lists. This can be run as part of a package installation or as a separate step.'], 'type': 'bool', 'default': False, 'aliases': ['update-cache']}",
    "upgrade": "{'description': ['Whether or not to upgrade whole system.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Install package foo
  pacman:
    name: foo
    state: present

- name: Upgrade package foo
  pacman:
    name: foo
    state: latest
    update_cache: yes

- name: Remove packages foo and bar
  pacman:
    name: foo,bar
    state: absent

- name: Recursively remove package baz
  pacman:
    name: baz
    state: absent
    recurse: yes

- name: Run the equivalent of "pacman -Sy" as a separate step
  pacman:
    update_cache: yes

- name: Run the equivalent of "pacman -Su" as a separate step
  pacman:
    upgrade: yes

- name: Run the equivalent of "pacman -Syu" as a separate step
  pacman:
    update_cache: yes
    upgrade: yes

- name: Run the equivalent of "pacman -Rdd", force remove package baz
  pacman:
    name: baz
    state: absent
    force: yes

```

## License

TODO

## Author Information
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Aaron Bull Schaefer (@elasticdog) <aaron@elasticdog.com>', 'Afterburn']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Aaron Bull Schaefer (@elasticdog) <aaron@elasticdog.com>', 'Afterburn']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Aaron Bull Schaefer (@elasticdog) <aaron@elasticdog.com>', 'Afterburn']
