# Ansible lookup: ansible.lookup_lastpass


fetch data from lastpass

## Description

use the lpass command line utility to fetch specific fields from lastpass

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['key from which you want to retrieve the field'], 'required': True}",
    "field": "{'description': ['field to return from lastpass'], 'default': 'password'}",
}
```

## Examples


``` yaml

- name: get 'custom_field' from lastpass entry 'entry-name'
  debug:
    msg: "{{ lookup('lastpass', 'entry-name', field='custom_field') }}"

```

## License

TODO

## Author Information
  - ['Andrew Zenk <azenk@umn.edu>']
