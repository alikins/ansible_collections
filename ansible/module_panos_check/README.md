# Ansible module: ansible.module_panos_check


check if PAN-OS device is ready for configuration

## Description

Check if PAN-OS device is ready for being configured (no pending jobs).
The check could be done once or multiple times until the device is ready.

## Requirements

TODO

## Arguments

``` json
{
    "interval": "{'description': ['time waited between checks'], 'required': False, 'default': '0'}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "timeout": "{'description': ['timeout of API calls'], 'required': False, 'default': '0'}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# single check on 192.168.1.1 with credentials admin/admin
- name: check if ready
  panos_check:
    ip_address: "192.168.1.1"
    password: "admin"

# check for 10 times, every 30 seconds, if device 192.168.1.1
# is ready, using credentials admin/admin
- name: wait for reboot
  panos_check:
    ip_address: "192.168.1.1"
    password: "admin"
  register: result
  until: result is not failed
  retries: 10
  delay: 30

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
