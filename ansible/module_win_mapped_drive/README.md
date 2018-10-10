# Ansible module: ansible.module_win_mapped_drive


Map network drives for users

## Description

Allows you to modify mapped network drives for individual users.

## Requirements

TODO

## Arguments

``` json
{
    "letter": "{'description': ['The letter of the network path to map to.', 'This letter must not already be in use with Windows.'], 'required': True}",
    "password": "{'description': ['The password for C(username).']}",
    "path": "{'description': ['The UNC path to map the drive to.', 'This is required if C(state=present).', 'If C(state=absent) and path is not set, the module will delete the mapped drive regardless of the target.', 'If C(state=absent) and the path is set, the module will throw an error if path does not match the target of the mapped drive.'], 'type': 'path'}",
    "state": "{'description': ['If C(present) will ensure the mapped drive exists.', 'If C(absent) will ensure the mapped drive does not exist.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "username": "{'description': ['Credentials to map the drive with.', 'The username MUST include the domain or servername like SERVER\\user, see the example for more information.']}",
}
```

## Examples


``` yaml

- name: Create a mapped drive under Z
  win_mapped_drive:
    letter: Z
    path: \\domain\appdata\accounting

- name: Delete any mapped drives under Z
  win_mapped_drive:
    letter: Z
    state: absent

- name: Only delete the mapped drive Z if the paths match (error is thrown otherwise)
  win_mapped_drive:
    letter: Z
    path: \\domain\appdata\accounting
    state: absent

- name: Create mapped drive with local credentials
  win_mapped_drive:
    letter: M
    path: \\SERVER\c$
    username: SERVER\Administrator
    password: Password

- name: Create mapped drive with domain credentials
  win_mapped_drive:
    letter: M
    path: \\domain\appdata\it
    username: DOMAIN\IT
    password: Password

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
