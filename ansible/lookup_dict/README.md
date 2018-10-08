# Ansible lookup: ansible.lookup_dict


returns key/value pair items from dictionaries

## Description

Takes dictionaries as input and returns a list with each item in the list being a dictionary with 'key' and 'value' as keys to the previous dictionary's structure.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['A list of dictionaries'], 'required': True}",
}
```

## Examples


``` yaml

vars:
  users:
    alice:
      name: Alice Appleworth
      telephone: 123-456-7890
    bob:
      name: Bob Bananarama
      telephone: 987-654-3210
tasks:
  # with predefined vars
  - name: Print phone records
    debug:
      msg: "User {{ item.key }} is {{ item.value.name }} ({{ item.value.telephone }})"
    loop: "{{ lookup('dict', users) }}"
  # with inline dictionary
  - name: show dictionary
    debug:
      msg: "{{item.key}}: {{item.value}}"
    with_dict: {a: 1, b: 2, c: 3}
  # Items from loop can be used in when: statements
  - name: set_fact when alice in key
    set_fact:
      alice_exists: true
    loop: "{{ lookup('dict', users) }}"
    when: "'alice' in item.key"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
