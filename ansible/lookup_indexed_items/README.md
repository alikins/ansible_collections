# Ansible lookup: ansible.lookup_indexed_items


rewrites lists to return 'indexed items'

## Description

use this lookup if you want to loop over an array and also get the numeric index of where you are in the array as you go
any list given will be transformed with each resulting element having the it's previous position in item.0 and its value in item.1

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

- name: indexed loop demo
  debug:
    msg: "at array position {{ item.0 }} there is a value {{ item.1 }}"
  with_indexed_items:
    - "{{ some_list }}"

```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>']
