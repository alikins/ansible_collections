# Ansible module: ansible.module_net_get


Copy a file from a network device to Ansible Controller

## Description

This module provides functionality to copy file from network device to ansible controller.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['Specifies the destination file. The path to the destination file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory.'], 'default': ['Same filename as specified in I(src). The path will be playbook root or role root directory if playbook is part of a role.']}",
    "protocol": "{'description': ['Protocol used to transfer file.'], 'default': 'scp', 'choices': ['scp', 'sftp']}",
    "src": "{'description': ['Specifies the source file. The path to the source file can either be the full path on the network device or a relative path as per path supported by destination network device.'], 'required': True}",
}
```

## Examples


``` yaml

- name: copy file from the network device to Ansible controller
  net_get:
    src: running_cfg_ios1.txt

- name: copy file from ios to common location at /tmp
  net_get:
    src: running_cfg_sw1.txt
    dest : /tmp/ios1.txt

```

## License

TODO

## Author Information
  - ['Deepak Agrawal (@dagrawal)']
