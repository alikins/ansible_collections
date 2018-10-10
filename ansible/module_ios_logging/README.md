# Ansible module: ansible.module_ios_logging


Manage logging on network devices

## Description

This module provides declarative management of logging on Cisco Ios devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of logging definitions.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "dest": "{'description': ['Destination of the logs.'], 'choices': ['on', 'host', 'console', 'monitor', 'buffered']}",
    "facility": "{'description': ['Set logging facility.']}",
    "level": "{'description': ['Set logging severity levels.']}",
    "name": "{'description': ['If value of C(dest) is I(file) it indicates file-name, for I(user) it indicates username and for I(host) indicates the host name to be notified.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "size": "{'description': ['Size of buffer. The acceptable value is in range from 4096 to 4294967295 bytes.'], 'default': 4096}",
    "state": "{'description': ['State of the logging configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure host logging
  ios_logging:
    dest: host
    name: 172.16.0.1
    state: present

- name: remove host logging configuration
  ios_logging:
    dest: host
    name: 172.16.0.1
    state: absent

- name: configure console logging level and facility
  ios_logging:
    dest: console
    facility: local7
    level: debugging
    state: present

- name: enable logging to all
  ios_logging:
    dest : on

- name: configure buffer size
  ios_logging:
    dest: buffered
    size: 5000

- name: Configure logging using aggregate
  ios_logging:
    aggregate:
      - { dest: console, level: notifications }
      - { dest: buffered, size: 9000 }

- name: remove logging using aggregate
  ios_logging:
    aggregate:
      - { dest: console, level: notifications }
      - { dest: buffered, size: 9000 }
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
