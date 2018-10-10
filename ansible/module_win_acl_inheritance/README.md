# Ansible module: ansible.module_win_acl_inheritance


Change ACL inheritance

## Description

Change ACL (Access Control List) inheritance and optionally copy inherited ACE's (Access Control Entry) to dedicated ACE's or vice versa.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Path to be used for changing inheritance'], 'required': True, 'type': 'path'}",
    "reorganize": "{'description': ["For P(state) = I(absent), indicates if the inherited ACE's should be copied from the parent directory. This is necessary (in combination with removal) for a simple ACL instead of using multiple ACE deny entries.", "For P(state) = I(present), indicates if the inherited ACE's should be deduplicated compared to the parent directory. This removes complexity of the ACL structure."], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Specify whether to enable I(present) or disable I(absent) ACL inheritance'], 'choices': ['absent', 'present'], 'default': 'absent'}",
}
```

## Examples


``` yaml

- name: Disable inherited ACE's
  win_acl_inheritance:
    path: C:\apache
    state: absent

- name: Disable and copy inherited ACE's
  win_acl_inheritance:
    path: C:\apache
    state: absent
    reorganize: yes

- name: Enable and remove dedicated ACE's
  win_acl_inheritance:
    path: C:\apache
    state: present
    reorganize: yes

```

## License

TODO

## Author Information
  - ['Hans-Joachim Kliemeck (@h0nIg)']
