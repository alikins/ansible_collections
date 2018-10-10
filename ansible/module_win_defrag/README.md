# Ansible module: ansible.module_win_defrag


Consolidate fragmented files on local volumes

## Description

Locates and consolidates fragmented files on local volumes to improve system performance.
More information regarding C(win_defrag) is available from: U(https://technet.microsoft.com/en-us/library/cc731650(v=ws.11).aspx)

## Requirements

TODO

## Arguments

``` json
{
    "exclude_volumes": "{'description': ['A list of drive letters or mount point paths to exclude from defragmentation.'], 'type': 'list'}",
    "freespace_consolidation": "{'description': ['Perform free space consolidation on the specified volumes.']}",
    "include_volumes": "{'description': ['A list of drive letters or mount point paths of the volumes to be defragmented.', 'If this parameter is omitted, all volumes (not excluded) will be fragmented.'], 'type': 'list'}",
    "parallel": "{'description': ['Run the operation on each volume in parallel in the background.'], 'type': 'bool', 'default': False}",
    "priority": "{'description': ['Run the operation at low or normal priority.'], 'choices': ['low', 'normal'], 'default': 'low'}",
}
```

## Examples


``` yaml

- name: Defragment all local volumes (in parallel)
  win_defrag:
    parallel: yes

- name: 'Defragment all local volumes, except C: and D:'
  win_defrag:
    exclude_volumes: [ C, D ]

- name: 'Defragment volume D: with normal priority'
  win_defrag:
    include_volumes: D
    priority: normal

- name: Consolidate free space (useful when reducing volumes)
  win_defrag:
    freespace_consolidation: yes

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
