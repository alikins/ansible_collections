# Ansible module: ansible.module_panos_commit


commit firewall's candidate configuration

## Description

PanOS module that will commit firewall's candidate configuration on
the device. The new configuration will become active immediately.

## Requirements

TODO

## Arguments

``` json
{
    "interval": "{'description': ['interval for checking commit job'], 'default': 0.5}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "sync": "{'description': ['if commit should be synchronous'], 'type': 'bool', 'default': True}",
    "timeout": "{'description': ['timeout for commit job']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# Commit candidate config on 192.168.1.1 in sync mode
- panos_commit:
    ip_address: "192.168.1.1"
    username: "admin"
    password: "admin"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
