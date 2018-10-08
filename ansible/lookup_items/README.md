# Ansible lookup: ansible.lookup_items


list of items

## Description

this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['list of items'], 'required': True}",
}
```

## Examples


``` yaml

- name: "loop through list"
  debug:
    msg: "An item: {{item}}"
  with_items:
    - 1
    - 2
    - 3

- name: add several users
  user:
    name: "{{ item }}"
    groups: "wheel"
    state: present
  with_items:
     - testuser1
     - testuser2

- name: "loop through list from a variable"
  debug:
    msg: "An item: {{item}}"
  with_items: "{{ somelist }}"

- name: more complex items to add several users
  user:
    name: "{{ item.name }}"
    uid: "{{ item.uid }}"
    groups: "{{ item.groups }}"
    state: present
  with_items:
     - { name: testuser1, uid: 1002, groups: "wheel, staff" }
     - { name: testuser2, uid: 1003, groups: staff }


```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>']
