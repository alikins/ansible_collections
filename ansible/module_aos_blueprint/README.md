# Ansible module: ansible.module_aos_blueprint


Manage AOS blueprint instance

## Description

Apstra AOS Blueprint module let you manage your Blueprint easily. You can create create and delete Blueprint by Name or ID. You can also use it to retrieve all data from a blueprint. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "id": "{'description': ["AOS Id of the IP Pool to manage (can't be used to create a new IP Pool). Only one of I(name) or I(id) can be set."]}",
    "name": "{'description': ['Name of the Blueprint to manage. Only one of I(name) or I(id) can be set.']}",
    "reference_arch": "{'description': ['When creating a blueprint, this value identifies a known AOS reference architecture value. I(Refer to AOS-server documentation for available values).']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Blueprint.'], 'choices': ['present', 'absent', 'build-ready'], 'default': 'present'}",
    "template": "{'description': ['When creating a blueprint, this value identifies, by name, an existing engineering design template within the AOS-server.']}",
    "timeout": "{'description': ['When I(state=build-ready), this timeout identifies timeout in seconds to wait before declaring a failure.'], 'default': 5}",
}
```

## Examples


``` yaml

- name: Creating blueprint
  aos_blueprint:
    session: "{{ aos_session }}"
    name: "my-blueprint"
    template: "my-template"
    reference_arch: two_stage_l3clos
    state: present

- name: Access a blueprint and get content
  aos_blueprint:
    session: "{{ aos_session }}"
    name: "{{ blueprint_name }}"
    template: "{{ blueprint_template }}"
    state: present
  register: bp

- name: Delete a blueprint
  aos_blueprint:
    session: "{{ aos_session }}"
    name: "my-blueprint"
    state: absent

- name: Await blueprint build-ready, and obtain contents
  aos_blueprint:
    session: "{{ aos_session }}"
    name: "{{ blueprint_name }}"
    state: build-ready
  register: bp

```

## License

TODO

## Author Information
  - ['jeremy@apstra.com (@jeremyschulman)']
