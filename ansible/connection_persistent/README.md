# Ansible connection: ansible.connection_persistent


Use a persistent unix socket for connection

## Description

This is a helper plugin to allow making other connections persistent.

## Requirements

TODO

## Arguments

``` json
{
    "persistent_command_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait for a command to return from the remote device.  If this timer is exceeded before the command returns, the connection plugin will raise an exception and close'], 'default': 10, 'ini': [{'section': 'persistent_connection', 'key': 'command_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_COMMAND_TIMEOUT'}], 'vars': [{'name': 'ansible_command_timeout'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
