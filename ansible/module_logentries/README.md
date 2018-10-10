# Ansible module: ansible.module_logentries


Module for tracking logs via logentries.com

## Description

Sends logs to LogEntries in realtime

## Requirements

TODO

## Arguments

``` json
{
    "logtype": "{'description': ['type of the log'], 'required': False}",
    "name": "{'description': ['name of the log'], 'required': False}",
    "path": "{'description': ['path to a log file'], 'required': True}",
    "state": "{'description': ['following state of the log'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
}
```

## Examples


``` yaml

# Track nginx logs
- logentries:
    path: /var/log/nginx/access.log
    state: present
    name: nginx-access-log

# Stop tracking nginx logs
- logentries:
    path: /var/log/nginx/error.log
    state: absent

```

## License

TODO

## Author Information
  - ['Ivan Vanderbyl (@ivanvanderbyl)']
