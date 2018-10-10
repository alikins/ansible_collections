# Ansible module: ansible.module_proxysql_mysql_users


Adds or removes mysql users from proxysql admin interface

## Description

The M(proxysql_mysql_users) module adds or removes mysql users using the proxysql admin interface.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['A user with I(active) set to C(False) will be tracked in the database, but will be never loaded in the in-memory data structures. If omitted the proxysql database default for I(active) is C(True).']}",
    "backend": "{'description': ['If I(backend) is set to C(True), this (username, password) pair is used for authenticating to the ProxySQL instance.'], 'default': True}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "default_hostgroup": "{'description': ['If there is no matching rule for the queries sent by this user, the traffic it generates is sent to the specified hostgroup. If omitted the proxysql database default for I(use_ssl) is 0.']}",
    "default_schema": "{'description': ['The schema to which the connection should change to by default.']}",
    "fast_forward": "{'description': ['If I(fast_forward) is set to C(True), I(fast_forward) will bypass the query processing layer (rewriting, caching) and pass through the query directly as is to the backend server. If omitted the proxysql database default for I(fast_forward) is C(False).']}",
    "frontend": "{'description': ['If I(frontend) is set to C(True), this (username, password) pair is used for authenticating to the mysqld servers against any hostgroup.'], 'default': True}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "max_connections": "{'description': ['The maximum number of connections ProxySQL will open to the backend for this user. If omitted the proxysql database default for I(max_connections) is 10000.']}",
    "password": "{'description': ['Password of the user connecting to the mysqld or ProxySQL instance.']}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['When C(present) - adds the user, when C(absent) - removes the user.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "transaction_persistent": "{'description': ['If this is set for the user with which the MySQL client is connecting to ProxySQL (thus a "frontend" user), transactions started within a hostgroup will remain within that hostgroup regardless of any other rules. If omitted the proxysql database default for I(transaction_persistent) is C(False).']}",
    "use_ssl": "{'description': ['If I(use_ssl) is set to C(True), connections by this user will be made using SSL connections. If omitted the proxysql database default for I(use_ssl) is C(False).']}",
    "username": "{'description': ['Name of the user connecting to the mysqld or ProxySQL instance.'], 'required': True}",
}
```

## Examples


``` yaml

---
# This example adds a user, it saves the mysql user config to disk, but
# avoids loading the mysql user config to runtime (this might be because
# several users are being added and the user wants to push the config to
# runtime in a single batch using the M(proxysql_manage_config) module).  It
# uses supplied credentials to connect to the proxysql admin interface.

- proxysql_mysql_users:
    login_user: 'admin'
    login_password: 'admin'
    username: 'productiondba'
    state: present
    load_to_runtime: False

# This example removes a user, saves the mysql user config to disk, and
# dynamically loads the mysql user config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- proxysql_mysql_users:
    config_file: '~/proxysql.cnf'
    username: 'mysqlboy'
    state: absent

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
