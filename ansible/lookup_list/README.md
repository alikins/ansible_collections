# Ansible lookup: ansible.lookup_list


simply returns what it is given

## Description

this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: unlike with_items you will get 3 items from this loop, the 2nd one being a list
  debug: var=item
  with_list:
    - 1
    - [2,3]
    - 4

```

## License

TODO

## Author Information
  - ['Ansible core team']
