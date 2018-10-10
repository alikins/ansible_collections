# Ansible module: ansible.module_proxysql_global_variables


Gets or sets the proxysql global variables

## Description

The M(proxysql_global_variables) module gets or sets the proxysql global variables.

## Requirements

TODO

## Arguments

``` json
{
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "value": "{'description': ['Defines a value the variable specified using I(variable) should be set to.']}",
    "variable": "{'description': ['Defines which variable should be returned, or if I(value) is specified which variable should be updated.'], 'required': True}",
}
```

## Examples


``` yaml

---
# This example sets the value of a variable, saves the mysql admin variables
# config to disk, and dynamically loads the mysql admin variables config to
# runtime. It uses supplied credentials to connect to the proxysql admin
# interface.

- proxysql_global_variables:
    login_user: 'admin'
    login_password: 'admin'
    variable: 'mysql-max_connections'
    value: 4096

# This example gets the value of a variable.  It uses credentials in a
# supplied config file to connect to the proxysql admin interface.

- proxysql_global_variables:
    config_file: '~/proxysql.cnf'
    variable: 'mysql-default_query_delay'

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
