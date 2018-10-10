# Ansible module: ansible.module_aos_logical_device_map


Manage AOS Logical Device Map

## Description

Apstra AOS Logical Device Map module let you manage your Logical Device Map easily. You can create create and delete Logical Device Map by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the Logical Device Map to manage. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value). Only one of I(name), I(id) or I(content) can be set."]}",
    "id": "{'description': ["AOS Id of the Logical Device Map to manage (can't be used to create a new Logical Device Map), Only one of I(name), I(id) or I(content) can be set."]}",
    "name": "{'description': ['Name of the Logical Device Map to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Logical Device Map (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Create an Logical Device Map with one subnet"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    name: "my-logical-device-map"
    state: present

- name: "Create an Logical Device Map with multiple subnets"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    name: "my-other-logical-device-map"
    state: present

- name: "Check if an Logical Device Map exist with same subnets by ID"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    name: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: present

- name: "Delete an Logical Device Map by name"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    name: "my-logical-device-map"
    state: absent

- name: "Delete an Logical Device Map by id"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

# Save an Logical Device Map to a file

- name: "Access Logical Device Map 1/3"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    name: "my-logical-device-map"
    state: present
  register: logical_device_map

- name: "Save Logical Device Map into a file in JSON 2/3"
  copy:
    content: "{{ logical_device_map.value | to_nice_json }}"
    dest: logical_device_map_saved.json

- name: "Save Logical Device Map into a file in YAML 3/3"
  copy:
    content: "{{ logical_device_map.value | to_nice_yaml }}"
    dest: logical_device_map_saved.yaml

- name: "Load Logical Device Map from a JSON file"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/logical_device_map_saved.json') }}"
    state: present

- name: "Load Logical Device Map from a YAML file"
  aos_logical_device_map:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/logical_device_map_saved.yaml') }}"
    state: present


```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
