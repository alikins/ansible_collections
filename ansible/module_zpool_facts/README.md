# Ansible module: ansible.module_zpool_facts


Gather facts about ZFS pools

## Description

Gather facts from ZFS pool properties.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['ZFS pool name.'], 'aliases': ['pool', 'zpool'], 'required': False}",
    "parsable": "{'description': ['Specifies if property values should be displayed in machine friendly format.'], 'type': 'bool', 'default': False, 'required': False}",
    "properties": "{'description': ['Specifies which dataset properties should be queried in comma-separated format. For more information about dataset properties, check zpool(1M) man page.'], 'aliases': ['props'], 'default': 'all', 'required': False}",
}
```

## Examples


``` yaml

# Gather facts about ZFS pool rpool
- zpool_facts: pool=rpool

# Gather space usage about all imported ZFS pools
- zpool_facts: properties='free,size'

- debug: msg='ZFS pool {{ item.name }} has {{ item.free }} free space out of {{ item.size }}.'
  with_items: '{{ ansible_zfs_pools }}'

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
