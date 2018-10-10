# Ansible module: ansible.module_aos_asn_pool


Manage AOS ASN Pool

## Description

Apstra AOS ASN Pool module let you manage your ASN Pool easily. You can create and delete ASN Pool by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the ASN Pool to manage. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ['AOS Id of the ASN Pool to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "name": "{'description': ['Name of the ASN Pool to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "ranges": "{'description': ['List of ASNs ranges to add to the ASN Pool. Each range must have 2 values.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the ASN Pool (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: "Create ASN Pool"
  aos_asn_pool:
    session: "{{ aos_session }}"
    name: "my-asn-pool"
    ranges:
      - [ 100, 200 ]
    state: present
  register: asnpool

- name: "Save ASN Pool into a file in JSON"
  copy:
    content: "{{ asnpool.value | to_nice_json }}"
    dest: resources/asn_pool_saved.json

- name: "Save ASN Pool into a file in YAML"
  copy:
    content: "{{ asnpool.value | to_nice_yaml }}"
    dest: resources/asn_pool_saved.yaml


- name: "Delete ASN Pool"
  aos_asn_pool:
    session: "{{ aos_session }}"
    name: "my-asn-pool"
    state: absent

- name: "Load ASN Pool from File(JSON)"
  aos_asn_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/asn_pool_saved.json') }}"
    state: present

- name: "Delete ASN Pool from File(JSON)"
  aos_asn_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/asn_pool_saved.json') }}"
    state: absent

- name: "Load ASN Pool from File(Yaml)"
  aos_asn_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/asn_pool_saved.yaml') }}"
    state: present
  register: test

- name: "Delete ASN Pool from File(Yaml)"
  aos_asn_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/asn_pool_saved.yaml') }}"
    state: absent

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
