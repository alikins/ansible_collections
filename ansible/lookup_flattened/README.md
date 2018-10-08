# Ansible lookup: ansible.lookup_flattened


return single list completely flattened

## Description

given one or more lists, this lookup will flatten any list elements found recursively until only 1 list is left.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['lists to flatten'], 'required': True}",
}
```

## Examples


``` yaml

- name: "'unnest' all elements into single list"
  debug: msg="all in one list {{lookup('flattened', [1,2,3,[5,6]], [a,b,c], [[5,6,1,3], [34,a,b,c]])}}"

```

## License

TODO

## Author Information
  - ['Serge van Ginderachter <serge@vanginderachter.be>']
