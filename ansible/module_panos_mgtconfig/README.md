# Ansible module: ansible.module_panos_mgtconfig


configure management settings of device

## Description

Configure management settings of device

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "dns_server_primary": "{'description': ['address of primary DNS server']}",
    "dns_server_secondary": "{'description': ['address of secondary DNS server']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "panorama_primary": "{'description': ['address of primary Panorama server']}",
    "panorama_secondary": "{'description': ['address of secondary Panorama server']}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: set dns and panorama
  panos_mgtconfig:
    ip_address: "192.168.1.1"
    password: "admin"
    dns_server_primary: "1.1.1.1"
    dns_server_secondary: "1.1.1.2"
    panorama_primary: "1.1.1.3"
    panorama_secondary: "1.1.1.4"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
