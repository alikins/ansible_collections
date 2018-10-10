# Ansible module: ansible.module_net_put


Copy a file from Ansible Controller to a network device

## Description

This module provides functionality to copy file from Ansible controller to network devices.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['Specifies the destination file. The path to destination file can either be the full path or relative path as supported by network_os.'], 'default': ['Filename from src and at default directory of user shell on network_os.'], 'required': False}",
    "mode": "{'description': ['Set the file transfer mode. If mode is set to I(template) then I(src) file will go through Jinja2 template engine to replace any vars if present in the src file. If mode is set to I(binary) then file will be copied as it is to destination device.'], 'default': 'binary', 'choices': ['binary', 'text'], 'version_added': '2.7'}",
    "protocol": "{'description': ['Protocol used to transfer file.'], 'default': 'scp', 'choices': ['scp', 'sftp']}",
    "src": "{'description': ['Specifies the source file. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory.'], 'required': True}",
}
```

## Examples


``` yaml

- name: copy file from ansible controller to a network device
  net_put:
    src: running_cfg_ios1.txt

- name: copy file at root dir of flash in slot 3 of sw1(ios)
  net_put:
    src: running_cfg_sw1.txt
    protocol: sftp
    dest : flash3:/running_cfg_sw1.txt

```

## License

TODO

## Author Information
  - ['Deepak Agrawal (@dagrawal)']
