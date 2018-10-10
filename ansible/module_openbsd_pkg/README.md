# Ansible module: ansible.module_openbsd_pkg


Manage packages on OpenBSD

## Description

Manage packages on OpenBSD using the pkg tools.

## Requirements

TODO

## Arguments

``` json
{
    "build": "{'description': ["Build the package from source instead of downloading and installing a binary. Requires that the port source tree is already installed. Automatically builds and installs the 'sqlports' package, if it is not already installed."], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "clean": "{'description': ['When updating or removing packages, delete the extra configuration file(s) in the old packages which are annotated with @extra in the packaging-list.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "name": "{'description': ['A name or a list of names of the packages.'], 'required': True}",
    "ports_dir": "{'description': ['When used in combination with the C(build) option, allows overriding the default ports source directory.'], 'default': '/usr/ports', 'version_added': '2.1'}",
    "quick": "{'description': ['Replace or delete packages quickly; do not bother with checksums before removing normal files.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "state": "{'description': ['C(present) will make sure the package is installed. C(latest) will make sure the latest version of the package is installed. C(absent) will make sure the specified package is not installed.'], 'choices': ['absent', 'latest', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Make sure nmap is installed
  openbsd_pkg:
    name: nmap
    state: present

- name: Make sure nmap is the latest version
  openbsd_pkg:
    name: nmap
    state: latest

- name: Make sure nmap is not installed
  openbsd_pkg:
    name: nmap
    state: absent

- name: Make sure nmap is installed, build it from source if it is not
  openbsd_pkg:
    name: nmap
    state: present
    build: yes

- name: Specify a pkg flavour with '--'
  openbsd_pkg:
    name: vim--no_x11
    state: present

- name: Specify the default flavour to avoid ambiguity errors
  openbsd_pkg:
    name: vim--
    state: present

- name: Specify a package branch (requires at least OpenBSD 6.0)
  openbsd_pkg:
    name: python%3.5
    state: present

- name: Update all packages on the system
  openbsd_pkg:
    name: '*'
    state: latest

- name: Purge a package and it's configuration files
  openbsd_pkg:
    name: mpd
    clean: yes
    state: absent

- name: Quickly remove a package without checking checksums
  openbsd_pkg:
    name: qt5
    quick: yes
    state: absent

```

## License

TODO

## Author Information
  - ['Patrik Lundin (@eest)']
