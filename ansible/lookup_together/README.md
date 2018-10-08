# Ansible lookup: ansible.lookup_together


merges lists into synchronized list

## Description

Creates a list with the iterated elements of the supplied lists
To clarify with an example, [ 'a', 'b' ] and [ 1, 2 ] turn into [ ('a',1), ('b', 2) ]
This is basically the same as the 'zip_longest' filter and Python function
Any 'unbalanced' elements will be substituted with 'None'

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['list of lists to merge'], 'required': True}",
}
```

## Examples


``` yaml

- name: item.0 returns from the 'a' list, item.1 returns from the '1' list
  debug:
    msg: "{{ item.0 }} and {{ item.1 }}"
  with_together:
    - ['a', 'b', 'c', 'd']
    - [1, 2, 3, 4]

```

## License

TODO

## Author Information
  - ['Bradley Young <young.bradley@gmail.com>']
