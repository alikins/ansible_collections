# Ansible module: ansible.module_win_share


Manage Windows shares

## Description

Add, modify or remove Windows share and set share permissions.

## Requirements

TODO

## Arguments

``` json
{
    "caching_mode": "{'description': ['Set the CachingMode for this share.'], 'choices': ['BranchCache', 'Documents', 'Manual', 'None', 'Programs', 'Unknown'], 'default': 'Manual', 'version_added': '2.3'}",
    "change": "{'description': ['Specify user list that should get read and write access on share, separated by comma.']}",
    "deny": "{'description': ['Specify user list that should get no access, regardless of implied access on share, separated by comma.']}",
    "description": "{'description': ['Share description.']}",
    "encrypt": "{'description': ['Sets whether to encrypt the traffic to the share or not.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "full": "{'description': ['Specify user list that should get full access on share, separated by comma.']}",
    "list": "{'description': ['Specify whether to allow or deny file listing, in case user has no permission on share. Also known as Access-Based Enumeration.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Share name.'], 'required': True}",
    "path": "{'description': ['Share directory.'], 'required': True, 'type': 'path'}",
    "read": "{'description': ['Specify user list that should get read access on share, separated by comma.']}",
    "state": "{'description': ['Specify whether to add C(present) or remove C(absent) the specified share.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Playbook example
# Add share and set permissions
---
- name: Add secret share
  win_share:
    name: internal
    description: top secret share
    path: C:\shares\internal
    list: no
    full: Administrators,CEO
    read: HR-Global
    deny: HR-External

- name: Add public company share
  win_share:
    name: company
    description: top secret share
    path: C:\shares\company
    list: yes
    full: Administrators,CEO
    read: Global

- name: Remove previously added share
  win_share:
    name: internal
    state: absent

```

## License

TODO

## Author Information
  - ['Hans-Joachim Kliemeck (@h0nIg)', 'David Baumann (@daBONDi)']
  - ['Hans-Joachim Kliemeck (@h0nIg)', 'David Baumann (@daBONDi)']
