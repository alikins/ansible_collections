# Ansible module: ansible.module_mysql_variables


Manage MySQL global variables

## Description

Query / Set MySQL variables

## Requirements

TODO

## Arguments

``` json
{
    "config_file": "{'description': ['Specify a config file from which user and password are to be read.'], 'default': '~/.my.cnf', 'version_added': '2.0'}",
    "connect_timeout": "{'description': ['The connection timeout when connecting to the MySQL server.'], 'default': 30, 'version_added': '2.1'}",
    "login_host": "{'description': ['Host running the database.'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_port": "{'description': ['Port of the MySQL server. Requires I(login_host) be defined as other then localhost if login_port is used.'], 'default': 3306}",
    "login_unix_socket": "{'description': ['The path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['The username used to authenticate with.']}",
    "ssl_ca": "{'version_added': '2.0', 'description': ['The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server.']}",
    "ssl_cert": "{'version_added': '2.0', 'description': ['The path to a client public key certificate.']}",
    "ssl_key": "{'version_added': '2.0', 'description': ['The path to the client private key.']}",
    "value": "{'description': ['If set, then sets variable value to this'], 'required': False}",
    "variable": "{'description': ['Variable name to operate'], 'required': True}",
}
```

## Examples


``` yaml

# Check for sync_binlog setting
- mysql_variables:
    variable: sync_binlog

# Set read_only variable to 1
- mysql_variables:
    variable: read_only
    value: 1

```

## License

TODO

## Author Information
  - ['Balazs Pocze (@banyek)']
