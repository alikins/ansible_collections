# Ansible module: ansible.module_bower


Manage bower packages with bower

## Description

Manage bower packages with bower

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of a bower package to install']}",
    "offline": "{'description': ['Install packages from local cache, if the packages were installed before'], 'type': 'bool', 'default': False}",
    "path": "{'description': ['The base path where to install the bower packages'], 'required': True}",
    "production": "{'description': ['Install with --production flag'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "relative_execpath": "{'description': ['Relative path to bower executable from install path'], 'version_added': '2.1'}",
    "state": "{'description': ['The state of the bower package'], 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
    "version": "{'description': ['The version to be installed']}",
}
```

## Examples


``` yaml

- name: Install "bootstrap" bower package.
  bower:
    name: bootstrap

- name: Install "bootstrap" bower package on version 3.1.1.
  bower:
    name: bootstrap
    version: '3.1.1'

- name: Remove the "bootstrap" bower package.
  bower:
    name: bootstrap
    state: absent

- name: Install packages based on bower.json.
  bower:
    path: /app/location

- name: Update packages based on bower.json to their latest version.
  bower:
    path: /app/location
    state: latest

# install bower locally and run from there
- npm:
    path: /app/location
    name: bower
    global: no
- bower:
    path: /app/location
    relative_execpath: node_modules/.bin

```

## License

TODO

## Author Information
  - ['Michael Warkentin (@mwarkentin)']
