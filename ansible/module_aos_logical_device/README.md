# Ansible module: ansible.module_aos_logical_device


Manage AOS Logical Device

## Description

Apstra AOS Logical Device module let you manage your Logical Devices easily. You can create create and delete Logical Device by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the Logical Device to create. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ["AOS Id of the Logical Device to manage (can't be used to create a new Logical Device), Only one of I(name), I(id) or I(content) can be set."]}",
    "name": "{'description': ['Name of the Logical Device to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Logical Device (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Delete a Logical Device by name"
  aos_logical_device:
    session: "{{ aos_session }}"
    name: "my-logical-device"
    state: absent

- name: "Delete a Logical Device by id"
  aos_logical_device:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

# Save a Logical Device to a file

- name: "Access Logical Device 1/3"
  aos_logical_device:
    session: "{{ aos_session }}"
    name: "my-logical-device"
    state: present
  register: logical_device

- name: "Save Logical Device into a JSON file 2/3"
  copy:
    content: "{{ logical_device.value | to_nice_json }}"
    dest: logical_device_saved.json
- name: "Save Logical Device into a YAML file 3/3"
  copy:
    content: "{{ logical_device.value | to_nice_yaml }}"
    dest: logical_device_saved.yaml

- name: "Load Logical Device from a JSON file"
  aos_logical_device:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/logical_device_saved.json') }}"
    state: present

- name: "Load Logical Device from a YAML file"
  aos_logical_device:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/logical_device_saved.yaml') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
