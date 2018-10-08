# Ansible connection: ansible.connection_lxd


Run tasks in lxc containers via lxc CLI

## Description

Run commands or put/fetch files to an existing lxc container using lxc CLI

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['shell to use for execution inside container'], 'default': '/bin/sh', 'vars': [{'name': 'ansible_executable'}, {'name': 'ansible_lxd_executable'}]}",
    "remote_addr": "{'description': ['Container identifier'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_lxd_host'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Matt Clay <matt@mystile.com>']
