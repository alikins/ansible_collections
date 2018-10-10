# Ansible module: ansible.module_mongodb_parameter


Change an administrative parameter on a MongoDB server

## Description

Change an administrative parameter on a MongoDB server.

## Requirements

TODO

## Arguments

``` json
{
    "database": "{'description': ['The name of the database to add/remove the user from'], 'required': True}",
    "login_database": "{'description': ['The database where login credentials are stored']}",
    "login_host": "{'description': ['The host running the database'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_port": "{'description': ['The port to connect to'], 'default': 27017}",
    "login_user": "{'description': ['The username used to authenticate with']}",
    "param": "{'description': ['MongoDB administrative parameter to modify'], 'required': True}",
    "param_type": "{'description': ['Define the parameter value (str, int)'], 'default': 'str'}",
    "replica_set": "{'description': ['Replica set to connect to (automatically connects to primary for writes)']}",
    "ssl": "{'description': ['Whether to use an SSL connection when connecting to the database'], 'type': 'bool', 'default': False}",
    "value": "{'description': ['MongoDB administrative parameter value to set'], 'required': True}",
}
```

## Examples


``` yaml

# Set MongoDB syncdelay to 60 (this is an int)
- mongodb_parameter:
    param: syncdelay
    value: 60
    param_type: int

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
