# Ansible module: ansible.module_supervisorctl


Manage the state of a program or group of programs running via supervisord

## Description

Manage the state of a program or group of programs running via supervisord

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['The supervisor configuration file path'], 'version_added': '1.3'}",
    "name": "{'description': ['The name of the supervisord program or group to manage.', 'The name will be taken as group name when it ends with a colon I(:)', 'Group support is only available in Ansible version 1.6 or later.'], 'required': True}",
    "password": "{'description': ['password to use for authentication'], 'version_added': '1.3'}",
    "server_url": "{'description': ['URL on which supervisord server is listening'], 'version_added': '1.3'}",
    "signal": "{'description': ["The signal to send to the program/group, when combined with the 'signalled' state. Required when l(state=signalled)."], 'version_added': '2.8'}",
    "state": "{'description': ['The desired state of program/group.'], 'required': True, 'choices': ['present', 'started', 'stopped', 'restarted', 'absent', 'signalled']}",
    "supervisorctl_path": "{'description': ['path to supervisorctl executable'], 'version_added': '1.4'}",
    "username": "{'description': ['username to use for authentication'], 'version_added': '1.3'}",
}
```

## Examples


``` yaml

# Manage the state of program to be in 'started' state.
- supervisorctl:
    name: my_app
    state: started

# Manage the state of program group to be in 'started' state.
- supervisorctl:
    name: 'my_apps:'
    state: started

# Restart my_app, reading supervisorctl configuration from a specified file.
- supervisorctl:
    name: my_app
    state: restarted
    config: /var/opt/my_project/supervisord.conf

# Restart my_app, connecting to supervisord with credentials and server URL.
- supervisorctl:
    name: my_app
    state: restarted
    username: test
    password: testpass
    server_url: http://localhost:9001

# Send a signal to my_app via supervisorctl
- supervisorctl:
    name: my_app
    state: signalled
    signal: USR1

```

## License

TODO

## Author Information
  - ['Matt Wright (@mattupstate)', 'Aaron Wang (@inetfuture) <inetfuture@gmail.com>']
  - ['Matt Wright (@mattupstate)', 'Aaron Wang (@inetfuture) <inetfuture@gmail.com>']
