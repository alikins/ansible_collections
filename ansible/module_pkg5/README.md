# Ansible module: ansible.module_pkg5


Manages packages with the Solaris 11 Image Packaging System

## Description

IPS packages are the native packages in Solaris 11 and higher.

## Requirements

TODO

## Arguments

``` json
{
    "accept_licenses": "{'description': ['Accept any licences.'], 'type': 'bool', 'default': False, 'aliases': ['accept', 'accept_licences']}",
    "name": "{'description': ['An FRMI of the package(s) to be installed/removed/updated.', 'Multiple packages may be specified, separated by C(,).'], 'required': True}",
    "state": "{'description': ['Whether to install (I(present), I(latest)), or remove (I(absent)) a package.'], 'choices': ['absent', 'latest', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Install Vim
  pkg5:
    name: editor/vim

- name: Remove finger daemon
  pkg5:
    name: service/network/finger
    state: absent

- name: Install several packages at once
  pkg5:
    name:
    - /file/gnu-findutils
    - /text/gnu-grep

```

## License

TODO

## Author Information
  - ['Peter Oliver (@mavit)']
