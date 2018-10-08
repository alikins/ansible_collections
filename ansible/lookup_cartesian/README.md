# Ansible lookup: ansible.lookup_cartesian


returns the cartesian product of lists

## Description

Takes the input lists and returns a list that represents the product of the input lists.
It is clearer with an example, it turns [1, 2, 3], [a, b] into [1, a], [1, b], [2, a], [2, b], [3, a], [3, b]. You can see the exact syntax in the examples section.

## Requirements

TODO

## Arguments

``` json
{
    "_raw": "{'description': ['a set of lists'], 'required': True}",
}
```

## Examples


``` yaml

- name: Example of the change in the description
  debug: msg="{{ [1,2,3]|lookup('cartesian', [a, b])}}"

- name: loops over the cartesian product of the supplied lists
  debug: msg="{{item}}"
  with_cartesian:
    - "{{list1}}"
    - "{{list2}}"
    - [1,2,3,4,5,6]

```

## License

TODO

## Author Information
  - ['UNKNOWN']
