# Ansible module: ansible.module_panos_loadcfg


load configuration on PAN-OS device

## Description

Load configuration on PAN-OS device

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "file": "{'description': ['configuration file to load']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# Import and load config file from URL
  - name: import configuration
    panos_import:
      ip_address: "192.168.1.1"
      password: "admin"
      url: "{{ConfigURL}}"
      category: "configuration"
    register: result
  - name: load configuration
    panos_loadcfg:
      ip_address: "192.168.1.1"
      password: "admin"
      file: "{{result.filename}}"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
