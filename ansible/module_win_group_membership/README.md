# Ansible module: ansible.module_win_group_membership


Manage Windows local group membership

## Description

Allows the addition and removal of local, service and domain users, and domain groups from a local group.

## Requirements

TODO

## Arguments

``` json
{
    "members": "{'description': ['A list of members to ensure are present/absent from the group.', 'Accepts local users as .\\username, and SERVERNAME\\username.', 'Accepts domain users and groups as DOMAIN\\username and username@DOMAIN.', 'Accepts service users as NT AUTHORITY\\username.', 'Accepts all local, domain and service user types as username, favoring domain lookups when in a domain.'], 'required': True, 'type': 'list'}",
    "name": "{'description': ['Name of the local group to manage membership on.'], 'required': True}",
    "state": "{'description': ['Desired state of the members in the group.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add a local and domain user to a local group
  win_group_membership:
    name: Remote Desktop Users
    members:
      - NewLocalAdmin
      - DOMAIN\TestUser
    state: present

- name: Remove a domain group and service user from a local group
  win_group_membership:
    name: Backup Operators
    members:
      - DOMAIN\TestGroup
      - NT AUTHORITY\SYSTEM
    state: absent

```

## License

TODO

## Author Information
  - ['Andrew Saraceni (@andrewsaraceni)']
