# Ansible module: ansible.module_junos_logging


Manage logging on network devices

## Description

This module provides declarative management of logging on Juniper JUNOS devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'default': True, 'type': 'bool'}",
    "aggregate": "{'description': ['List of logging definitions.']}",
    "dest": "{'description': ['Destination of the logs.'], 'choices': ['console', 'host', 'file', 'user']}",
    "facility": "{'description': ['Set logging facility.']}",
    "files": "{'description': ['Number of files to be archived, this is applicable if value of I(dest) is C(file). The acceptable value is in range from 1 to 1000.'], 'required': False}",
    "level": "{'description': ['Set logging severity levels.']}",
    "name": "{'description': ['If value of C(dest) is I(file) it indicates file-name, for I(user) it indicates username and for I(host) indicates the host name to be notified.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "rotate_frequency": "{'description': ['Rotate log frequency in minutes, this is applicable if value of I(dest) is C(file). The acceptable value is in range of 1 to 59. This controls the frequency after which log file is rotated.'], 'required': False}",
    "size": "{'description': ['Size of the file in archive, this is applicable if value of I(dest) is C(file). The acceptable value is in range from 65536 to 1073741824 bytes.'], 'required': False}",
    "state": "{'description': ['State of the logging configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure console logging
  junos_logging:
    dest: console
    facility: any
    level: critical

- name: remove console logging configuration
  junos_logging:
    dest: console
    state: absent

- name: configure file logging
  junos_logging:
    dest: file
    name: test
    facility: pfe
    level: error

- name: configure logging parameter
  junos_logging:
    files: 30
    size: 65536
    rotate_frequency: 10

- name: Configure file logging using aggregate
  junos_logging:
    dest: file
    aggregate:
    - name: test-1
      facility: pfe
      level: critical
    - name: test-2
      facility: kernel
      level: emergency
    active: True

- name: Delete file logging using aggregate
  junos_logging:
    aggregate:
    - { dest: file, name: test-1,  facility: pfe, level: critical }
    - { dest: file, name: test-2,  facility: kernel, level: emergency }
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
