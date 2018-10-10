# Ansible module: ansible.module_cyberark_user


Module for CyberArk User Management using PAS Web Services SDK

## Description

CyberArk User Management using PAS Web Services SDK. It currently supports the following actions Get User Details, Add User, Update User, Delete User.

## Requirements

TODO

## Arguments

``` json
{
    "change_password_on_the_next_logon": "{'type': 'bool', 'default': False, 'description': ['Whether or not the user must change their password in their next logon. Valid values = true/false.']}",
    "cyberark_session": "{'required': True, 'description': ['Dictionary set by a CyberArk authentication containing the different values to perform actions on a logged-on CyberArk session, please see M(cyberark_authentication) module for an example of cyberark_session.']}",
    "disabled": "{'type': 'bool', 'default': False, 'description': ['Whether or not the user will be disabled. Valid values = true/false.']}",
    "email": "{'description': ['The user email address.']}",
    "expiry_date": "{'description': ['The date and time when the user account will expire and become disabled.']}",
    "first_name": "{'description': ['The user first name.']}",
    "group_name": "{'description': ['The name of the group the user will be added to.']}",
    "initial_password": "{'description': ['The password that the new user will use to log on the first time. This password must meet the password policy requirements. this parameter is required when state is present -- Add User.']}",
    "last_name": "{'description': ['The user last name.']}",
    "location": "{'description': ['The Vault Location for the user.']}",
    "new_password": "{'description': ['The user updated password. Make sure that this password meets the password policy requirements.']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Specifies the state needed for the user present for create user, absent for delete user.']}",
    "user_type_name": "{'default': 'EPVUser', 'description': ['The type of user.']}",
    "username": "{'required': True, 'description': ['The name of the user who will be queried (for details), added, updated or deleted.']}",
}
```

## Examples


``` yaml

- name: Logon to CyberArk Vault using PAS Web Services SDK
  cyberark_authentication:
    api_base_url: "https://components.cyberark.local"
    use_shared_logon_authentication: true

- name: Create user & immediately add it to a group
  cyberark_user:
    username: "username"
    initial_password: "password"
    user_type_name: "EPVUser"
    change_password_on_the_next_logon: false
    group_name: "GroupOfUsers"
    state: present
    cyberark_session: "{{ cyberark_session }}"

- name: Make sure user is present and reset user credential if present
  cyberark_user:
    username: "Username"
    new_password: "password"
    disabled: false
    state: present
    cyberark_session: "{{ cyberark_session }}"

- name: Logoff from CyberArk Vault
  cyberark_authentication:
    state: absent
    cyberark_session: "{{ cyberark_session }}"

```

## License

TODO

## Author Information
  - ['Edward Nunez @ CyberArk BizDev (@enunez-cyberark, @cyberark-bizdev, @erasmix)']
