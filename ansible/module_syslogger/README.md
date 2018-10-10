# Ansible module: ansible.module_syslogger


Log messages in the syslog

## Description

Uses syslog to add log entries to the host.
Can specify facility and priority.

## Requirements

TODO

## Arguments

``` json
{
    "facility": "{'description': ['Set the log facility'], 'choices': ['kern', 'user', 'mail', 'daemon', 'auth', 'lpr', 'news', 'uucp', 'cron', 'syslog', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'], 'required': False, 'default': 'daemon'}",
    "log_pid": "{'description': ['Log the pid in brackets'], 'type': 'bool', 'required': False, 'default': False}",
    "msg": "{'description': ['This is the message to place in syslog'], 'required': True}",
    "priority": "{'description': ['Set the log priority'], 'choices': ['emerg', 'alert', 'crit', 'err', 'warning', 'notice', 'info', 'debug'], 'required': False, 'default': 'info'}",
}
```

## Examples


``` yaml

# Full example
- name: Test syslog
  syslogger:
    msg: "Hello from ansible"
    priority: "err"
    facility: "daemon"
    log_pid: true

# Basic usage
- name: Simple Usage
  syslogger:
    msg: "I will end up as daemon.info"


```

## License

TODO

## Author Information
  - ['Tim Rightnour (@garbled1)']
