# Ansible module: ansible.module_win_user_right


Manage Windows User Rights

## Description

Add, remove or set User Rights for a group or users or groups.
You can set user rights for both local and domain accounts.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['C(add) will add the users/groups to the existing right.', 'C(remove) will remove the users/groups from the existing right.', 'C(set) will replace the users/groups of the existing right.'], 'default': 'set', 'choices': ['add', 'remove', 'set']}",
    "name": "{'description': ['The name of the User Right as shown by the C(Constant Name) value from U(https://technet.microsoft.com/en-us/library/dd349804.aspx).', 'The module will return an error if the right is invalid.'], 'required': True}",
    "users": "{'description': ['A list of users or groups to add/remove on the User Right.', 'These can be in the form DOMAIN\\user-group, user-group@DOMAIN.COM for domain users/groups.', 'For local users/groups it can be in the form user-group, .\\user-group, SERVERNAME\\user-group where SERVERNAME is the name of the remote server.', 'You can also add special local accounts like SYSTEM and others.'], 'required': True, 'type': 'list'}",
}
```

## Examples


``` yaml

---
- name: replace the entries of Deny log on locally
  win_user_right:
    name: SeDenyInteractiveLogonRight
    users:
    - Guest
    - Users
    action: set

- name: add account to Log on as a service
  win_user_right:
    name: SeServiceLogonRight
    users:
    - .\Administrator
    - '{{ansible_hostname}}\local-user'
    action: add

- name: remove accounts who can create Symbolic links
  win_user_right:
    name: SeCreateSymbolicLinkPrivilege
    users:
    - SYSTEM
    - Administrators
    - DOMAIN\User
    - group@DOMAIN.COM
    action: remove

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
