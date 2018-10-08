# Ansible connection: ansible.connection_lxc


Run tasks in lxc containers via lxc python library

## Description

Run commands or put/fetch files to an existing lxc container using lxc python library

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'default': '/bin/sh', 'description': ['Shell executable'], 'vars': [{'name': 'ansible_executable'}, {'name': 'ansible_lxc_executable'}]}",
    "remote_addr": "{'description': ['Container identifier'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_lxc_host'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Joerg Thalheim <joerg@higgsboson.tk>']
