# Ansible module: ansible.module_junos_user


Manage local user accounts on Juniper JUNOS devices

## Description

This module manages locally configured user accounts on remote network devices running the JUNOS operating system.  It provides a set of arguments for creating, removing and updating locally defined accounts

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "aggregate": "{'description': ['The C(aggregate) argument defines a list of users to be configured on the remote device.  The list of users will be compared against the current users and only changes will be added or removed from the device configuration.  This argument is mutually exclusive with the name argument.'], 'version_added': '2.4', 'aliases': ['users', 'collection']}",
    "full_name": "{'description': ['The C(full_name) argument provides the full name of the user account to be created on the remote device.  This argument accepts any text string value.']}",
    "name": "{'description': ['The C(name) argument defines the username of the user to be created on the system.  This argument must follow appropriate usernaming conventions for the target device running JUNOS.  This argument is mutually exclusive with the C(aggregate) argument.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "purge": "{'description': ['The C(purge) argument instructs the module to consider the users definition absolute.  It will remove any previously configured users on the device with the exception of the current defined set of aggregate.'], 'type': 'bool', 'default': False}",
    "role": "{'description': ['The C(role) argument defines the role of the user account on the remote system.  User accounts can have more than one role configured.'], 'choices': ['operator', 'read-only', 'super-user', 'unauthorized']}",
    "sshkey": "{'description': ['The C(sshkey) argument defines the public SSH key to be configured for the user account on the remote system.  This argument must be a valid SSH key']}",
    "state": "{'description': ['The C(state) argument configures the state of the user definitions as it relates to the device operational configuration.  When set to I(present), the user should be configured in the device active configuration and when set to I(absent) the user should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: create new user account
  junos_user:
    name: ansible
    role: super-user
    sshkey: "{{ lookup('file', '~/.ssh/ansible.pub') }}"
    state: present

- name: remove a user account
  junos_user:
    name: ansible
    state: absent

- name: remove all user accounts except ansible
  junos_user:
    aggregate:
    - name: ansible
    purge: yes

- name: Create list of users
  junos_user:
    aggregate:
      - {name: test_user1, full_name: test_user2, role: operator, state: present}
      - {name: test_user2, full_name: test_user2, role: read-only, state: present}

- name: Delete list of users
  junos_user:
    aggregate:
      - {name: test_user1, full_name: test_user2, role: operator, state: absent}
      - {name: test_user2, full_name: test_user2, role: read-only, state: absent}

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
