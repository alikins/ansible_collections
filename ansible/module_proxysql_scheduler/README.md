# Ansible module: ansible.module_proxysql_scheduler


Adds or removes schedules from proxysql admin interface

## Description

The M(proxysql_scheduler) module adds or removes schedules using the proxysql admin interface.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['A schedule with I(active) set to C(False) will be tracked in the database, but will be never loaded in the in-memory data structures.'], 'default': True}",
    "arg1": "{'description': ['Argument that can be passed to the job.']}",
    "arg2": "{'description': ['Argument that can be passed to the job.']}",
    "arg3": "{'description': ['Argument that can be passed to the job.']}",
    "arg4": "{'description': ['Argument that can be passed to the job.']}",
    "arg5": "{'description': ['Argument that can be passed to the job.']}",
    "comment": "{'description': ['Text field that can be used for any purposed defined by the user.']}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "filename": "{'description': ['Full path of the executable to be executed.'], 'required': True}",
    "force_delete": "{'description': ["By default we avoid deleting more than one schedule in a single batch, however if you need this behaviour and you're not concerned about the schedules deleted, you can set I(force_delete) to C(True)."], 'default': False}",
    "interval_ms": "{'description': ['How often (in millisecond) the job will be started. The minimum value for I(interval_ms) is 100 milliseconds.'], 'default': 10000}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['When C(present) - adds the schedule, when C(absent) - removes the schedule.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

---
# This example adds a schedule, it saves the scheduler config to disk, but
# avoids loading the scheduler config to runtime (this might be because
# several servers are being added and the user wants to push the config to
# runtime in a single batch using the M(proxysql_manage_config) module).  It
# uses supplied credentials to connect to the proxysql admin interface.

- proxysql_scheduler:
    login_user: 'admin'
    login_password: 'admin'
    interval_ms: 1000
    filename: "/opt/maintenance.py"
    state: present
    load_to_runtime: False

# This example removes a schedule, saves the scheduler config to disk, and
# dynamically loads the scheduler config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- proxysql_scheduler:
    config_file: '~/proxysql.cnf'
    filename: "/opt/old_script.py"
    state: absent

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
