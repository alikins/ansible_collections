# Ansible module: ansible.module_aos_blueprint_virtnet


Manage AOS blueprint parameter values

## Description

Apstra AOS Blueprint Virtual Network module let you manage your Virtual Network easily. You can create access, define and delete Virtual Network by name or by using a JSON / Yaml file. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "blueprint": "{'description': ['Blueprint Name or Id as defined in AOS.'], 'required': True}",
    "content": "{'description': ["Datastructure of the Virtual Network to manage. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "name": "{'description': ['Name of Virtual Network as part of the Blueprint.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Virtual Network (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Access Existing Virtual Network"
  aos_blueprint_virtnet:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    name: "my-virtual-network"
    state: present

- name: "Delete Virtual Network with JSON File"
  aos_blueprint_virtnet:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    content: "{{ lookup('file', 'resources/virtual-network-02.json') }}"
    state: absent

- name: "Create Virtual Network"
  aos_blueprint_virtnet:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    content: "{{ lookup('file', 'resources/virtual-network-02.json') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
