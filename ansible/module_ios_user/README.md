# Ansible module: ansible.module_ios_user


Manage the aggregate of local users on Cisco IOS device

## Description

This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['The set of username objects to be configured on the remote Cisco IOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the C(name) argument.'], 'aliases': ['users', 'collection']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "configured_password": "{'description': ['The password to be configured on the Cisco IOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as C(provider password).']}",
    "name": "{'description': ['The username to be configured on the Cisco IOS device. This argument accepts a string value and is mutually exclusive with the C(aggregate) argument. Please note that this option is not same as C(provider username).']}",
    "nopassword": "{'description': ['Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.'], 'type': 'bool'}",
    "privilege": "{'description': ['The C(privilege) argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "purge": "{'description': ['Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).'], 'type': 'bool', 'default': False}",
    "sshkey": "{'description': ['Specifies the SSH public key to configure for the given username.  This argument accepts a valid SSH key value.'], 'version_added': '2.7'}",
    "state": "{'description': ['Configures the state of the username definition as it relates to the device operational configuration. When set to I(present), the username(s) should be configured in the device active configuration and when set to I(absent) the username(s) should not be in the device active configuration'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password.  When set to C(always), the password will always be updated in the device and when set to C(on_create) the password will be updated only if the username is created.'], 'default': 'always', 'choices': ['on_create', 'always']}",
    "view": "{'description': ['Configures the view for the username in the device running configuration. The argument accepts a string value defining the view name. This argument does not check if the view has been configured on the device.'], 'aliases': ['role']}",
}
```

## Examples


``` yaml

- name: create a new user
  ios_user:
    name: ansible
    nopassword: True
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  ios_user:
    purge: yes

- name: remove all users except admin and these listed users
  ios_user:
    aggregate:
      - name: testuser1
      - name: testuser2
      - name: testuser3
    purge: yes

- name: set multiple users to privilege level 15
  ios_user:
    aggregate:
      - name: netop
      - name: netend
    privilege: 15
    state: present

- name: set user view/role
  ios_user:
    name: netop
    view: network-operator
    state: present

- name: Change Password for User netop
  ios_user:
    name: netop
    configured_password: "{{ new_password }}"
    update_password: always
    state: present

- name: Aggregate of users
  ios_user:
    aggregate:
      - name: ansibletest2
      - name: ansibletest3
    view: network-admin

- name: Delete users with aggregate
  ios_user:
    aggregate:
      - name: ansibletest1
      - name: ansibletest2
      - name: ansibletest3
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
