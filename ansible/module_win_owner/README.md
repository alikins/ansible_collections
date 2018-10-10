# Ansible module: ansible.module_win_owner


Set owner

## Description

Set owner of files or directories

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Path to be used for changing owner'], 'required': True, 'type': 'path'}",
    "recurse": "{'description': ['Indicates if the owner should be changed recursively'], 'type': 'bool', 'default': False}",
    "user": "{'description': ['Name to be used for changing owner'], 'required': True}",
}
```

## Examples


``` yaml

- name: Change owner of Path
  win_owner:
    path: C:\apache
    user: apache
    recurse: yes

- name: Set the owner of root directory
  win_owner:
    path: C:\apache
    user: SYSTEM
    recurse: no

```

## License

TODO

## Author Information
  - ['Hans-Joachim Kliemeck (@h0nIg)']
