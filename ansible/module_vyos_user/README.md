# Ansible module: ansible.module_vyos_user


Manage the collection of local users on VyOS device

## Description

This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the collection of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['The set of username objects to be configured on the remote VyOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the C(name) argument.'], 'aliases': ['users', 'collection']}",
    "configured_password": "{'description': ['The password to be configured on the VyOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as C(provider password).']}",
    "full_name": "{'description': ['The C(full_name) argument provides the full name of the user account to be created on the remote device. This argument accepts any text string value.']}",
    "level": "{'description': ['The C(level) argument configures the level of the user when logged into the system. This argument accepts string values admin or operator.'], 'aliases': ['role']}",
    "name": "{'description': ['The username to be configured on the VyOS device. This argument accepts a string value and is mutually exclusive with the C(aggregate) argument. Please note that this option is not same as C(provider username).']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "purge": "{'description': ['Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Configures the state of the username definition as it relates to the device operational configuration. When set to I(present), the username(s) should be configured in the device active configuration and when set to I(absent) the username(s) should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password.  When set to C(always), the password will always be updated in the device and when set to C(on_create) the password will be updated only if the username is created.'], 'default': 'always', 'choices': ['on_create', 'always']}",
}
```

## Examples


``` yaml

- name: create a new user
  vyos_user:
    name: ansible
    configured_password: password
    state: present
- name: remove all users except admin
  vyos_user:
    purge: yes
- name: set multiple users to level operator
  vyos_user:
    aggregate:
      - name: netop
      - name: netend
    level: operator
    state: present
- name: Change Password for User netop
  vyos_user:
    name: netop
    configured_password: "{{ new_password }}"
    update_password: always
    state: present

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
