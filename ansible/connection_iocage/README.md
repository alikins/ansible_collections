# Ansible connection: ansible.connection_iocage


Run tasks in iocage jails

## Description

Run commands or put/fetch files to an existing iocage jail

## Requirements

TODO

## Arguments

``` json
{
    "remote_addr": "{'description': ['Path to the jail'], 'default': "The set user as per docker's configuration", 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_iocage_host'}]}",
    "remote_user": "{'description': ['User to execute as inside the jail'], 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_iocage_user'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Stephan Lohse <dev-github@ploek.org>']
