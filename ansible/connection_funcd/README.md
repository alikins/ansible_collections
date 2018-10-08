# Ansible connection: ansible.connection_funcd


Use funcd to connect to target

## Description

This transport permits you to use Ansible over Func.
For people who have already setup func and that wish to play with ansible, this permit to move gradually to ansible without having to redo completely the setup of the network.

## Requirements

TODO

## Arguments

``` json
{
    "remote_addr": "{'description': ['The path of the chroot you want to access.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_func_host'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Michael Scherer (@msherer) <misc@zarb.org>']
