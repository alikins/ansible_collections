# Ansible module: ansible.module_ejabberd_user


Manages users for ejabberd servers

## Description

This module provides user management for ejabberd servers

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['the ejabberd host associated with this username'], 'required': True}",
    "logging": "{'description': ['enables or disables the local syslog facility for this module'], 'required': False, 'default': False, 'type': 'bool'}",
    "password": "{'description': ['the password to assign to the username'], 'required': False}",
    "state": "{'description': ['describe the desired state of the user to be managed'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['the name of the user to manage'], 'required': True}",
}
```

## Examples


``` yaml

# Example playbook entries using the ejabberd_user module to manage users state.

- name: create a user if it does not exist
  ejabberd_user:
    username: test
    host: server
    password: password

- name: delete a user if it exists
  ejabberd_user:
    username: test
    host: server
    state: absent

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
