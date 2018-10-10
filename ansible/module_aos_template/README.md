# Ansible module: ansible.module_aos_template


Manage AOS Template

## Description

Apstra AOS Template module let you manage your Template easily. You can create create and delete Template by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the Template to create. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ["AOS Id of the Template to manage (can't be used to create a new Template), Only one of I(name), I(id) or I(src) can be set."]}",
    "name": "{'description': ['Name of the Template to manage. Only one of I(name), I(id) or I(src) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Template (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Check if an Template exist by name"
  aos_template:
    session: "{{ aos_session }}"
    name: "my-template"
    state: present

- name: "Check if an Template exist by ID"
  aos_template:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: present

- name: "Delete an Template by name"
  aos_template:
    session: "{{ aos_session }}"
    name: "my-template"
    state: absent

- name: "Delete an Template by id"
  aos_template:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

- name: "Access Template 1/3"
  aos_template:
    session: "{{ aos_session }}"
    name: "my-template"
    state: present
  register: template

- name: "Save Template into a JSON file 2/3"
  copy:
    content: "{{ template.value | to_nice_json }}"
    dest: template_saved.json
- name: "Save Template into a YAML file 2/3"
  copy:
    content: "{{ template.value | to_nice_yaml }}"
    dest: template_saved.yaml

- name: "Load Template from File (Json)"
  aos_template:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/template_saved.json') }}"
    state: present

- name: "Load Template from File (yaml)"
  aos_template:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/template_saved.yaml') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
