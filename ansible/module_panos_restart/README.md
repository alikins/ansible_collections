# Ansible module: ansible.module_panos_restart


restart a device

## Description

Restart a device

## Requirements

TODO

## Arguments

``` json
{
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- panos_restart:
    ip_address: "192.168.1.1"
    username: "admin"
    password: "admin"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
