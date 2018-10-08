# Ansible connection: ansible.connection_jail


Run tasks in jails

## Description

Run commands or put/fetch files to an existing jail

## Requirements

TODO

## Arguments

``` json
{
    "remote_addr": "{'description': ['Path to the jail'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_jail_host'}]}",
    "remote_user": "{'description': ['User to execute as inside the jail'], 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_jail_user'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
