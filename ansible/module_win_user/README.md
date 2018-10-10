# Ansible module: ansible.module_win_user


Manages local Windows user accounts

## Description

Manages local Windows user accounts.
For non-Windows targets, use the M(user) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "account_disabled": "{'description': ['C(yes) will disable the user account.', 'C(no) will clear the disabled flag.'], 'type': 'bool', 'version_added': '1.9'}",
    "account_locked": "{'description': ['C(no) will unlock the user account if locked.'], 'choices': ['no'], 'version_added': '1.9'}",
    "description": "{'description': ['Description of the user.'], 'version_added': '1.9'}",
    "fullname": "{'description': ['Full name of the user.'], 'version_added': '1.9'}",
    "groups": "{'description': ["Adds or removes the user from this comma-separated lis of groups, depending on the value of I(groups_action). When I(groups_action) is C(replace) and I(groups) is set to the empty string ('groups='), the user is removed from all groups."], 'version_added': '1.9'}",
    "groups_action": "{'description': ['If C(add), the user is added to each group in I(groups) where not already a member.', 'If C(replace), the user is added as a member of each group in I(groups) and removed from any other groups.', 'If C(remove), the user is removed from each group in I(groups).'], 'choices': ['add', 'replace', 'remove'], 'default': 'replace', 'version_added': '1.9'}",
    "name": "{'description': ['Name of the user to create, remove or modify.'], 'required': True}",
    "password": "{'description': ["Optionally set the user's password to this (plain text) value."]}",
    "password_expired": "{'description': ['C(yes) will require the user to change their password at next login.', 'C(no) will clear the expired password flag.'], 'type': 'bool', 'version_added': '1.9'}",
    "password_never_expires": "{'description': ['C(yes) will set the password to never expire.', 'C(no) will allow the password to expire.'], 'type': 'bool', 'version_added': '1.9'}",
    "state": "{'description': ['When C(absent), removes the user account if it exists.', 'When C(present), creates or updates the user account.', 'When C(query) (new in 1.9), retrieves the user account details without making any changes.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "update_password": "{'description': ['C(always) will update passwords if they differ.  C(on_create) will only set the password for newly created users.'], 'choices': ['always', 'on_create'], 'default': 'always', 'version_added': '1.9'}",
    "user_cannot_change_password": "{'description': ['C(yes) will prevent the user from changing their password.', 'C(no) will allow the user to change their password.'], 'type': 'bool', 'version_added': '1.9'}",
}
```

## Examples


``` yaml

- name: Ensure user bob is present
  win_user:
    name: bob
    password: B0bP4ssw0rd
    state: present
    groups:
      - Users

- name: Ensure user bob is absent
  win_user:
    name: bob
    state: absent

```

## License

TODO

## Author Information
  - ['Paul Durivage (@angstwad)', 'Chris Church (@cchurch)']
  - ['Paul Durivage (@angstwad)', 'Chris Church (@cchurch)']
