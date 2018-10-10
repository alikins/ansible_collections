# Ansible module: ansible.module_panos_import


import file on PAN-OS devices

## Description

Import file on PAN-OS device

## Requirements

TODO

## Arguments

``` json
{
    "category": "{'description': ['Category of file uploaded. The default is software.', 'See API > Import section of the API reference for category options.'], 'default': 'software'}",
    "file": "{'description': ['Location of the file to import into device.']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "url": "{'description': ['URL of the file that will be imported to device.']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. Disabling certificate validation is not recommended.'], 'default': True, 'type': 'bool', 'version_added': '2.6'}",
}
```

## Examples


``` yaml

# import software image PanOS_vm-6.1.1 on 192.168.1.1
- name: import software image into PAN-OS
  panos_import:
    ip_address: 192.168.1.1
    username: admin
    password: admin
    file: /tmp/PanOS_vm-6.1.1
    category: software

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
