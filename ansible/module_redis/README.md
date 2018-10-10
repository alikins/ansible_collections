# Ansible module: ansible.module_redis


Various redis commands, slave and flush

## Description

Unified utility to interact with redis instances.

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['The selected redis command', 'C(config) (new in 1.6), ensures a configuration setting on an instance.', 'C(flush) flushes all the instance or a specified db.', 'C(slave) sets a redis instance in slave or master mode.'], 'required': True, 'choices': ['config', 'flush', 'slave']}",
    "db": "{'description': ['The database to flush (used in db mode) [flush command]']}",
    "flush_mode": "{'description': ['Type of flush (all the dbs in a redis instance or a specific one) [flush command]'], 'default': 'all', 'choices': ['all', 'db']}",
    "login_host": "{'description': ['The host running the database'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with (usually not used)']}",
    "login_port": "{'description': ['The port to connect to'], 'default': 6379}",
    "master_host": "{'description': ['The host of the master instance [slave command]']}",
    "master_port": "{'description': ['The port of the master instance [slave command]']}",
    "name": "{'description': ['A redis config key.'], 'version_added': 1.6}",
    "slave_mode": "{'description': ['the mode of the redis instance [slave command]'], 'default': 'slave', 'choices': ['master', 'slave']}",
    "value": "{'description': ['A redis config value.'], 'version_added': 1.6}",
}
```

## Examples


``` yaml

- name: Set local redis instance to be slave of melee.island on port 6377
  redis:
    command: slave
    master_host: melee.island
    master_port: 6377

- name: Deactivate slave mode
  redis:
    command: slave
    slave_mode: master

- name: Flush all the redis db
  redis:
    command: flush
    flush_mode: all

- name: Flush only one db in a redis instance
  redis:
    command: flush
    db: 1
    flush_mode: db

- name: Configure local redis to have 10000 max clients
  redis:
    command: config
    name: maxclients
    value: 10000

- name: Configure local redis to have lua time limit of 100 ms
  redis:
    command: config
    name: lua-time-limit
    value: 100

```

## License

TODO

## Author Information
  - ['Xabier Larrakoetxea (@slok)']
