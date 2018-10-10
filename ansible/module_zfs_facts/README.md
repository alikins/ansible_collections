# Ansible module: ansible.module_zfs_facts


Gather facts about ZFS datasets

## Description

Gather facts from ZFS dataset properties.

## Requirements

TODO

## Arguments

``` json
{
    "depth": "{'description': ['Specifiies recurion depth.']}",
    "name": "{'description': ['ZFS dataset name.'], 'required': True, 'aliases': ['ds', 'dataset']}",
    "parsable": "{'description': ['Specifies if property values should be displayed in machine friendly format.'], 'type': 'bool', 'default': False}",
    "properties": "{'description': ['Specifies which dataset properties should be queried in comma-separated format. For more information about dataset properties, check zfs(1M) man page.'], 'default': 'all', 'aliases': ['props']}",
    "recurse": "{'description': ['Specifies if properties for any children should be recursively displayed.'], 'type': 'bool', 'default': False}",
    "type": "{'description': ['Specifies which datasets types to display. Multiple values have to be provided in comma-separated form.'], 'choices': ['all', 'filesystem', 'volume', 'snapshot', 'bookmark'], 'default': 'all'}",
}
```

## Examples


``` yaml

- name: Gather facts about ZFS dataset rpool/export/home
  zfs_facts:
    dataset: rpool/export/home

- name: Report space usage on ZFS filesystems under data/home
  zfs_facts:
    name: data/home
    recurse: yes
    type: filesystem

- debug:
    msg: 'ZFS dataset {{ item.name }} consumes {{ item.used }} of disk space.'
  with_items: '{{ ansible_zfs_datasets }}'

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
