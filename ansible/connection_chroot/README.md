# Ansible connection: ansible.connection_chroot


Interact with local chroot

## Description

Run commands or put/fetch files to an existing chroot on the Ansible controller.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['User specified executable shell'], 'ini': [{'section': 'defaults', 'key': 'executable'}], 'env': [{'name': 'ANSIBLE_EXECUTABLE'}], 'vars': [{'name': 'ansible_executable'}]}",
    "remote_addr": "{'description': ['The path of the chroot you want to access.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Maykel Moya <mmoya@speedyrails.com>']
