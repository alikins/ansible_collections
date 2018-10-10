# Ansible module: ansible.module_aos_external_router


Manage AOS External Router

## Description

Apstra AOS External Router module let you manage your External Router easily. You can create create and delete External Router by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "asn": "{'description': ['ASN id of the external_router.']}",
    "content": "{'description': ["Datastructure of the External Router to create. The format is defined by the I(content_format) parameter. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ["AOS Id of the External Router to manage (can't be used to create a new External Router), Only one of I(name), I(id) or I(content) can be set."]}",
    "loopback": "{'description': ['IP address of the Loopback interface of the external_router.']}",
    "name": "{'description': ['Name of the External Router to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the External Router (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Create an External Router"
  aos_external_router:
    session: "{{ aos_session }}"
    name: "my-external-router"
    loopback: 10.0.0.1
    asn: 65000
    state: present

- name: "Check if an External Router exist by ID"
  aos_external_router:
    session: "{{ aos_session }}"
    name: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: present

- name: "Delete an External Router by name"
  aos_external_router:
    session: "{{ aos_session }}"
    name: "my-external-router"
    state: absent

- name: "Delete an External Router by id"
  aos_external_router:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

# Save an External Router to a file
- name: "Access External Router 1/3"
  aos_external_router:
    session: "{{ aos_session }}"
    name: "my-external-router"
    state: present
  register: external_router

- name: "Save External Router into a file in JSON 2/3"
  copy:
    content: "{{ external_router.value | to_nice_json }}"
    dest: external_router_saved.json

- name: "Save External Router into a file in YAML 3/3"
  copy:
    content: "{{ external_router.value | to_nice_yaml }}"
    dest: external_router_saved.yaml

- name: "Load External Router from a JSON file"
  aos_external_router:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/external_router_saved.json') }}"
    state: present

- name: "Load External Router from a YAML file"
  aos_external_router:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/external_router_saved.yaml') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
