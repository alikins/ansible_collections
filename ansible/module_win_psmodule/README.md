# Ansible module: ansible.module_win_psmodule


Adds or removes a Powershell Module

## Description

This module helps to install Powershell modules and register custom modules repository on Windows Server.

## Requirements

TODO

## Arguments

``` json
{
    "allow_clobber": "{'description': ['If C(yes) imports all commands, even if they have the same names as commands that already exists. Available only in Powershell 5.1 or higher.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the powershell module that has to be installed.'], 'required': True}",
    "repository": "{'description': ['Name of the custom repository to register or use.']}",
    "state": "{'description': ['If C(present) a new module is installed.', 'If C(absent) a module is removed.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "url": "{'description': ['URL of the custom repository to register.']}",
}
```

## Examples


``` yaml

---
- name: Add a powershell module
  win_psmodule:
    name: PowershellModule
    state: present

- name: Add a powershell module and register a repository
  win_psmodule:
    name: MyCustomModule
    repository: MyRepository
    url: https://myrepo.com
    state: present

- name: Add a powershell module from a specific repository
  win_psmodule:
    name: PowershellModule
    repository: MyRepository
    state: present

- name: Remove a powershell module
  win_psmodule:
    name: PowershellModule
    state: absent

- name: Remove a powershell module and a repository
  win_psmodule:
    name: MyCustomModule
    repository: MyRepository
    state: absent

```

## License

TODO

## Author Information
  - ['Daniele Lazzari']
