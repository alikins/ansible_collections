# Ansible callback: ansible.callback_syslog_json


sends JSON events to syslog

## Description

This plugin logs ansible-playbook and ansible runs to a syslog server in JSON format
Before 2.4 only environment variables were available for configuration

## Requirements

TODO

## Arguments

``` json
{
    "facility": "{'description': ['syslog facility to log as'], 'env': [{'name': 'SYSLOG_FACILITY'}], 'default': 'user', 'ini': [{'section': 'callback_syslog_json', 'key': 'syslog_facility'}]}",
    "port": "{'description': ['port on which the syslog server is listening'], 'env': [{'name': 'SYSLOG_PORT'}], 'default': 514, 'ini': [{'section': 'callback_syslog_json', 'key': 'syslog_port'}]}",
    "server": "{'description': ['syslog server that will receive the event'], 'env': [{'name': 'SYSLOG_SERVER'}], 'default': 'localhost', 'ini': [{'section': 'callback_syslog_json', 'key': 'syslog_server'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
