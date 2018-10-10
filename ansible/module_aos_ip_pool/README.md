# Ansible module: ansible.module_aos_ip_pool


Manage AOS IP Pool

## Description

Apstra AOS Ip Pool module let you manage your IP Pool easily. You can create create and delete IP Pool by Name, ID or by using a JSON File. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["Datastructure of the IP Pool to manage. The data can be in YAML / JSON or directly a variable. It's the same datastructure that is returned on success in I(value)."]}",
    "id": "{'description': ["AOS Id of the IP Pool to manage (can't be used to create a new IP Pool), Only one of I(name), I(id) or I(content) can be set."]}",
    "name": "{'description': ['Name of the IP Pool to manage. Only one of I(name), I(id) or I(content) can be set.']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the IP Pool (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnets": "{'description': ['List of subnet that needs to be part of the IP Pool.']}",
}
```

## Examples


``` yaml


- name: "Create an IP Pool with one subnet"
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: "my-ip-pool"
    subnets: [ 172.10.0.0/16 ]
    state: present

- name: "Create an IP Pool with multiple subnets"
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: "my-other-ip-pool"
    subnets: [ 172.10.0.0/16, 192.168.0.0./24 ]
    state: present

- name: "Check if an IP Pool exist with same subnets by ID"
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    subnets: [ 172.10.0.0/16, 192.168.0.0./24 ]
    state: present

- name: "Delete an IP Pool by name"
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: "my-ip-pool"
    state: absent

- name: "Delete an IP pool by id"
  aos_ip_pool:
    session: "{{ aos_session }}"
    id: "45ab26fc-c2ed-4307-b330-0870488fa13e"
    state: absent

# Save an IP Pool to a file

- name: "Access IP Pool 1/3"
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: "my-ip-pool"
    subnets: [ 172.10.0.0/16, 172.12.0.0/16 ]
    state: present
  register: ip_pool

- name: "Save Ip Pool into a file in JSON 2/3"
  copy:
    content: "{{ ip_pool.value | to_nice_json }}"
    dest: ip_pool_saved.json

- name: "Save Ip Pool into a file in YAML 3/3"
  copy:
    content: "{{ ip_pool.value | to_nice_yaml }}"
    dest: ip_pool_saved.yaml

- name: "Load IP Pool from a JSON file"
  aos_ip_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/ip_pool_saved.json') }}"
    state: present

- name: "Load IP Pool from a YAML file"
  aos_ip_pool:
    session: "{{ aos_session }}"
    content: "{{ lookup('file', 'resources/ip_pool_saved.yaml') }}"
    state: present

- name: "Load IP Pool from a Variable"
  aos_ip_pool:
    session: "{{ aos_session }}"
    content:
      display_name: my-ip-pool
      id: 4276738d-6f86-4034-9656-4bff94a34ea7
      subnets:
        - network: 172.10.0.0/16
        - network: 172.12.0.0/16
    state: present

```

## License

TODO

## Author Information
  - ['Damien Garros (@dgarros)']
