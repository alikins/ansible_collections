# Ansible module: ansible.module_proxysql_backend_servers


Adds or removes mysql hosts from proxysql admin interface

## Description

The M(proxysql_backend_servers) module adds or removes mysql hosts using the proxysql admin interface.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Text field that can be used for any purposed defined by the user. Could be a description of what the host stores, a reminder of when the host was added or disabled, or a JSON processed by some checker script.'], 'default': ''}",
    "compression": "{'description': ['If the value of I(compression) is greater than 0, new connections to that server will use compression. If omitted the proxysql database default for I(compression) is 0.']}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "hostgroup_id": "{'description': ['The hostgroup in which this mysqld instance is included. An instance can be part of one or more hostgroups.'], 'default': 0}",
    "hostname": "{'description': ['The ip address at which the mysqld instance can be contacted.'], 'required': True}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "max_connections": "{'description': ['The maximum number of connections ProxySQL will open to this backend server. If omitted the proxysql database default for I(max_connections) is 1000.']}",
    "max_latency_ms": "{'description': ['Ping time is monitored regularly. If a host has a ping time greater than I(max_latency_ms) it is excluded from the connection pool (although the server stays ONLINE). If omitted the proxysql database default for I(max_latency_ms) is 0.']}",
    "max_replication_lag": "{'description': ['If greater than 0, ProxySQL will reguarly monitor replication lag. If replication lag goes above I(max_replication_lag), proxysql will temporarily shun the server until replication catches up. If omitted the proxysql database default for I(max_replication_lag) is 0.']}",
    "port": "{'description': ['The port at which the mysqld instance can be contacted.'], 'default': 3306}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['When C(present) - adds the host, when C(absent) - removes the host.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "status": "{'description': ["ONLINE - Backend server is fully operational. OFFLINE_SOFT - When a server is put into C(OFFLINE_SOFT) mode, connections are kept in use until the current transaction is completed. This allows to gracefully detach a backend. OFFLINE_HARD - When a server is put into C(OFFLINE_HARD) mode, the existing connections are dropped, while new incoming connections aren't accepted either.\nIf omitted the proxysql database default for I(status) is C(ONLINE)."], 'choices': ['ONLINE', 'OFFLINE_SOFT', 'OFFLINE_HARD']}",
    "use_ssl": "{'description': ['If I(use_ssl) is set to C(True), connections to this server will be made using SSL connections. If omitted the proxysql database default for I(use_ssl) is C(False).']}",
    "weight": "{'description': ['The bigger the weight of a server relative to other weights, the higher the probability of the server being chosen from the hostgroup. If omitted the proxysql database default for I(weight) is 1.']}",
}
```

## Examples


``` yaml

---
# This example adds a server, it saves the mysql server config to disk, but
# avoids loading the mysql server config to runtime (this might be because
# several servers are being added and the user wants to push the config to
# runtime in a single batch using the M(proxysql_manage_config) module).  It
# uses supplied credentials to connect to the proxysql admin interface.

- proxysql_backend_servers:
    login_user: 'admin'
    login_password: 'admin'
    hostname: 'mysql01'
    state: present
    load_to_runtime: False

# This example removes a server, saves the mysql server config to disk, and
# dynamically loads the mysql server config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- proxysql_backend_servers:
    config_file: '~/proxysql.cnf'
    hostname: 'mysql02'
    state: absent

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
