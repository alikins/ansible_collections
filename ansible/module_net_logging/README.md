# Ansible module: ansible.module_net_logging


Manage logging on network devices

## Description

This module provides declarative management of logging on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of logging definitions.']}",
    "dest": "{'description': ['Destination of the logs.'], 'choices': ['console', 'host']}",
    "facility": "{'description': ['Set logging facility.']}",
    "level": "{'description': ['Set logging severity levels.']}",
    "name": "{'description': ['If value of C(dest) is I(host) it indicates file-name the host name to be notified.']}",
    "purge": "{'description': ['Purge logging not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the logging configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure console logging
  net_logging:
    dest: console
    facility: any
    level: critical

- name: remove console logging configuration
  net_logging:
    dest: console
    state: absent

- name: configure host logging
  net_logging:
    dest: host
    name: 192.0.2.1
    facility: kernel
    level: critical

- name: Configure file logging using aggregate
  net_logging:
    dest: file
    aggregate:
    - name: test-1
      facility: pfe
      level: critical
    - name: test-2
      facility: kernel
      level: emergency
- name: Delete file logging using aggregate
  net_logging:
    dest: file
    aggregate:
    - name: test-1
      facility: pfe
      level: critical
    - name: test-2
      facility: kernel
      level: emergency
    state: absent

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
