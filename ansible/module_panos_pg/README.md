# Ansible module: ansible.module_panos_pg


create a security profiles group

## Description

Create a security profile group

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "data_filtering": "{'description': ['name of the data filtering profile']}",
    "file_blocking": "{'description': ['name of the file blocking profile']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "pg_name": "{'description': ['name of the security profile group'], 'required': True}",
    "spyware": "{'description': ['name of the spyware profile']}",
    "url_filtering": "{'description': ['name of the url filtering profile']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
    "virus": "{'description': ['name of the anti-virus profile']}",
    "vulnerability": "{'description': ['name of the vulnerability profile']}",
    "wildfire": "{'description': ['name of the wildfire analysis profile']}",
}
```

## Examples


``` yaml

- name: setup security profile group
  panos_pg:
    ip_address: "192.168.1.1"
    password: "admin"
    username: "admin"
    pg_name: "pg-default"
    virus: "default"
    spyware: "default"
    vulnerability: "default"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
