# Ansible connection: ansible.connection_docker


Run tasks in docker containers

## Description

Run commands or put/fetch files to an existing docker container.

## Requirements

TODO

## Arguments

``` json
{
    "docker_extra_args": "{'description': ['Extra arguments to pass to the docker command line'], 'default': ''}",
    "remote_addr": "{'description': ['The name of the container you want to access.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_docker_host'}]}",
    "remote_user": "{'description': ['The user to execute as inside the container'], 'default': "The set user as per docker's configuration", 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_docker4_user'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Lorin Hochestein', 'Leendert Brouwer']
  - ['Lorin Hochestein', 'Leendert Brouwer']
