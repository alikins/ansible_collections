# Ansible lookup: ansible.lookup_inventory_hostnames


list of inventory hosts matching a host pattern

## Description

This lookup understands 'host patterns' as used by the `hosts:` keyword in plays and can return a list of matching hosts from inventory

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: show all the hosts matching the pattern, i.e. all but the group www
  debug:
    msg: "{{ item }}"
  with_inventory_hostnames:
    - all:!www

```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>', 'Steven Dossett <sdossett@panath.com>']
  - ['Michael DeHaan <michael.dehaan@gmail.com>', 'Steven Dossett <sdossett@panath.com>']
