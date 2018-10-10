# Ansible module: ansible.module_net_user


Manage the aggregate of local users on network device

## Description

This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['The set of username objects to be configured on the remote network device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the C(name) argument.']}",
    "configured_password": "{'description': ['The password to be configured on the remote network device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as C(provider password).']}",
    "name": "{'description': ['The username to be configured on the remote network device. This argument accepts a string value and is mutually exclusive with the C(aggregate) argument. Please note that this option is not same as C(provider username).']}",
    "nopassword": "{'description': ['Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.'], 'type': 'bool'}",
    "privilege": "{'description': ['The C(privilege) argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15.']}",
    "purge": "{'description': ['Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).'], 'type': 'bool', 'default': False}",
    "role": "{'description': ['Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device.']}",
    "sshkey": "{'description': ['Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value.']}",
    "state": "{'description': ['Configures the state of the username definition as it relates to the device operational configuration. When set to I(present), the username(s) should be configured in the device active configuration and when set to I(absent) the username(s) should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password.  When set to C(always), the password will always be updated in the device and when set to C(on_create) the password will be updated only if the username is created.'], 'default': 'always', 'choices': ['on_create', 'always']}",
}
```

## Examples


``` yaml

- name: create a new user
  net_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  net_user:
    purge: yes

- name: set multiple users to privilege level 15
  net_user:
    aggregate:
      - { name: netop }
      - { name: netend }
    privilege: 15
    state: present

- name: Change Password for User netop
  net_user:
    name: netop
    password: "{{ new_password }}"
    update_password: always
    state: present

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
