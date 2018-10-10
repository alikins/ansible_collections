# Ansible module: ansible.module_aos_rack_type


Manage AOS Rack Type

## Description

Apstra AOS Rack Type module let you manage your Rack Type easily. You can create create and delete Rack Type by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the Rack Type to create. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ["AOS Id of the Rack Type to manage (can't be used to create a new Rack Type), Only one of I(name), I(id) or I(content) can be set."]}",
    "name": "{'description': ['Name of the Rack Type to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Rack Type (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Delete a Rack Type by name"
  aos_rack_type:
    session: "{{ aos_session }}"
    name: "my-rack-type"
    state: absent

- name: "Delete a Rack Type by id"
  aos_rack_type:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

# Save a Rack Type to a file

- name: "Access Rack Type 1/3"
  aos_rack_type:
    session: "{{ aos_session }}"
    name: "my-rack-type"
    state: present
  register: rack_type

- name: "Save Rack Type into a JSON file 2/3"
  copy:
    content: "{{ rack_type.value | to_nice_json }}"
    dest: rack_type_saved.json
- name: "Save Rack Type into a YAML file 3/3"
  copy:
    content: "{{ rack_type.value | to_nice_yaml }}"
    dest: rack_type_saved.yaml

- name: "Load Rack Type from a JSON file"
  aos_rack_type:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/rack_type_saved.json') }}"
    state: present

- name: "Load Rack Type from a YAML file"
  aos_rack_type:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/rack_type_saved.yaml') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
