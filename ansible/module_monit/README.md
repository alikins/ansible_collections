# Ansible module: ansible.module_monit


Manage the state of a program monitored via Monit

## Description

Manage the state of a program monitored via I(Monit)

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the I(monit) program/process to manage'], 'required': True}",
    "state": "{'description': ['The state of service'], 'required': True, 'choices': ['present', 'started', 'stopped', 'restarted', 'monitored', 'unmonitored', 'reloaded']}",
    "timeout": "{'description': ['If there are pending actions for the service monitored by monit, then Ansible will check for up to this many seconds to verify the requested action has been performed. Ansible will sleep for five seconds between each check.'], 'default': 300, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# Manage the state of program "httpd" to be in "started" state.
- monit:
    name: httpd
    state: started

```

## License

TODO

## Author Information
  - ['Darryl Stoflet (@dstoflet)']
