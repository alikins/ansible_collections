# Ansible module: ansible.module_proxysql_replication_hostgroups


Manages replication hostgroups using the proxysql admin interface

## Description

Each row in mysql_replication_hostgroups represent a pair of writer_hostgroup and reader_hostgroup. ProxySQL will monitor the value of read_only for all the servers in specified hostgroups, and based on the value of read_only will assign the server to the writer or reader hostgroups.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Text field that can be used for any purposed defined by the user.']}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "reader_hostgroup": "{'description': ['Id of the reader hostgroup.'], 'required': True}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['When C(present) - adds the replication hostgroup, when C(absent) - removes the replication hostgroup.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "writer_hostgroup": "{'description': ['Id of the writer hostgroup.'], 'required': True}",
}
```

## Examples


``` yaml

---
# This example adds a replication hostgroup, it saves the mysql server config
# to disk, but avoids loading the mysql server config to runtime (this might be
# because several replication hostgroup are being added and the user wants to
# push the config to runtime in a single batch using the
# M(proxysql_manage_config) module).  It uses supplied credentials to connect
# to the proxysql admin interface.

- proxysql_replication_hostgroups:
    login_user: 'admin'
    login_password: 'admin'
    writer_hostgroup: 1
    reader_hostgroup: 2
    state: present
    load_to_runtime: False

# This example removes a replication hostgroup, saves the mysql server config
# to disk, and dynamically loads the mysql server config to runtime.  It uses
# credentials in a supplied config file to connect to the proxysql admin
# interface.

- proxysql_replication_hostgroups:
    config_file: '~/proxysql.cnf'
    writer_hostgroup: 3
    reader_hostgroup: 4
    state: absent

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
