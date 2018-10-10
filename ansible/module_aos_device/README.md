# Ansible module: ansible.module_aos_device


Manage Devices on AOS Server

## Description

Apstra AOS Device module let you manage your devices in AOS easily. You can approve devices and define in which state the device should be. Currently only the state I(normal) is supported but the goal is to extend this module with additional state. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "approve": "{'description': ['The approve argument instruct the module to convert a device in quarantine mode into approved mode.'], 'default': False, 'type': 'bool'}",
    "id": "{'description': ['The AOS internal id for a device; i.e. uniquely identifies the device in the AOS system. Only one of I(name) or I(id) can be set.']}",
    "location": "{'description': ["When approving a device using the I(approve) argument, it's possible define the location of the device."]}",
    "name": "{'description': ['The device serial-number; i.e. uniquely identifies the device in the AOS system. Only one of I(name) or I(id) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Define in which state the device should be. Currently only I(normal) is supported but the goal is to add I(maint) and I(decomm).'], 'default': 'normal', 'choices': ['normal']}",
}
```

## Examples


``` yaml


- name: Approve a new device
  aos_device:
    session: "{{ aos_session }}"
    name: D2060B2F105429GDABCD123
    state: 'normal'
    approve: true
    location: "rack-45, ru-18"

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
