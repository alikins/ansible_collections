# Ansible connection: ansible.connection_buildah


Interact with an existing buildah container

## Description

Run commands or put/fetch files to an existing container using buildah tool.

## Requirements

TODO

## Arguments

``` json
{
    "remote_addr": "{'description': ['The ID of the container you want to access.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}]}",
    "remote_user": "{'description': ['User specified via name or ID which is used to execute commands inside the container.'], 'ini': [{'section': 'defaults', 'key': 'remote_user'}], 'env': [{'name': 'ANSIBLE_REMOTE_USER'}], 'vars': [{'name': 'ansible_user'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Tomas Tomecek (ttomecek@redhat.com)']
