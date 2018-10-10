# Ansible module: ansible.module_seboolean


Toggles SELinux booleans

## Description

Toggles SELinux booleans.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the boolean to configure.'], 'required': True}",
    "persistent": "{'description': ['Set to C(yes) if the boolean setting should survive a reboot.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Desired boolean value'], 'type': 'bool', 'required': True}",
}
```

## Examples


``` yaml

- name: Set httpd_can_network_connect flag on and keep it persistent across reboots
  seboolean:
    name: httpd_can_network_connect
    state: yes
    persistent: yes

```

## License

TODO

## Author Information
  - ['Stephen Fromm (@sfromm)']
