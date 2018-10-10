# Ansible module: ansible.module_proxysql_manage_config


Writes the proxysql configuration settings between layers

## Description

The M(proxysql_global_variables) module writes the proxysql configuration settings between layers. Currently this module will always report a changed state, so should typically be used with WHEN however this will change in a future version when the CHECKSUM table commands are available for all tables in proxysql.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The supplied I(action) combines with the supplied I(direction) to provide the semantics of how we want to move the I(config_settings) between the I(config_layers).'], 'choices': ['LOAD', 'SAVE'], 'required': True}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "config_layer": "{'description': ['RUNTIME - represents the in-memory data structures of ProxySQL used by the threads that are handling the requests. MEMORY - (sometimes also referred as main) represents the in-memory SQLite3 database. DISK - represents the on-disk SQLite3 database. CONFIG - is the classical config file. You can only LOAD FROM the config file.'], 'choices': ['MEMORY', 'DISK', 'RUNTIME', 'CONFIG'], 'required': True}",
    "config_settings": "{'description': ["The I(config_settings) specifies which configuration we're writing."], 'choices': ['MYSQL USERS', 'MYSQL SERVERS', 'MYSQL QUERY RULES', 'MYSQL VARIABLES', 'ADMIN VARIABLES', 'SCHEDULER'], 'required': True}",
    "direction": "{'description': ['FROM - denotes we\'re reading values FROM the supplied I(config_layer) and writing to the next layer. TO - denotes we\'re reading from the previous layer and writing TO the supplied I(config_layer)."'], 'choices': ['FROM', 'TO'], 'required': True}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
}
```

## Examples


``` yaml

---
# This example saves the mysql users config from memory to disk. It uses
# supplied credentials to connect to the proxysql admin interface.

- proxysql_global_variables:
    login_user: 'admin'
    login_password: 'admin'
    action: "SAVE"
    config_settings: "MYSQL USERS"
    direction: "FROM"
    config_layer: "MEMORY"

# This example loads the mysql query rules config from memory to to runtime. It
# uses supplied credentials to connect to the proxysql admin interface.

- proxysql_global_variables:
    config_file: '~/proxysql.cnf'
    action: "LOAD"
    config_settings: "MYSQL QUERY RULES"
    direction: "TO"
    config_layer: "RUNTIME"

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
