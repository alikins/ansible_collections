# Ansible module: ansible.module_iosxr_logging


Configuration management of system logging services on network devices

## Description

This module provides declarative management configuration of system logging (syslog) on Cisco IOS XR devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of syslog logging configuration definitions.']}",
    "dest": "{'description': ['Destination for system logging (syslog) messages.'], 'choices': ['host', 'console', 'monitor', 'buffered', 'file']}",
    "facility": "{'description': ['To configure the type of syslog facility in which system logging (syslog) messages are sent to syslog servers Optional config for C(dest) = C(host)'], 'default': 'local7'}",
    "hostnameprefix": "{'description': ['To append a hostname prefix to system logging (syslog) messages logged to syslog servers. Optional config for C(dest) = C(host)'], 'version_added': 2.5}",
    "level": "{'description': ['Specifies the severity level for the logging.'], 'default': 'debugging', 'aliases': ['severity']}",
    "name": "{'description': ['When C(dest) = I(file) name indicates file-name', 'When C(dest) = I(host) name indicates the host-name or ip-address of syslog server.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "size": "{'description': ['Size of buffer when C(dest) = C(buffered). The acceptable value is in the range I(307200 to 125000000 bytes). Default 307200', 'Size of file when C(dest) = C(file). The acceptable value is in the range I(1 to 2097152)KB. Default 2 GB']}",
    "state": "{'description': ['Existential state of the logging configuration on the node.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vrf": "{'description': ['vrf name when syslog server is configured, C(dest) = C(host)'], 'default': 'default', 'version_added': 2.5}",
}
```

## Examples


``` yaml

- name: configure logging for syslog server host
  iosxr_logging:
    dest: host
    name: 10.10.10.1
    level: critical
    state: present

- name: add hostnameprefix configuration
  iosxr_logging:
    hostnameprefix: host1
    state: absent

- name: add facility configuration
  iosxr_logging:
    facility: local1
    state: present

- name: configure console logging level
  iosxr_logging:
    dest: console
    level: debugging
    state: present

- name: configure monitor logging level
  iosxr_logging:
    dest: monitor
    level: errors
    state: present

- name: configure syslog to a file
  iosxr_logging:
    dest: file
    name: file_name
    size: 2048
    level: errors
    state: present

- name: configure buffered logging with size
  iosxr_logging:
    dest: buffered
    size: 5100000

- name: Configure logging using aggregate
  iosxr_logging:
    aggregate:
      - { dest: console, level: warning }
      - { dest: buffered, size: 4800000 }
      - { dest: file, name: file3, size: 2048}
      - { dest: host, name: host3, level: critical}

- name: Delete logging using aggregate
  iosxr_logging:
    aggregate:
      - { dest: console, level: warning }
      - { dest: buffered, size: 4800000 }
      - { dest: file, name: file3, size: 2048}
      - { dest: host, name: host3, level: critical}
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)', 'Kedar Kekan (@kedarX)']
  - ['Trishna Guha (@trishnaguha)', 'Kedar Kekan (@kedarX)']
