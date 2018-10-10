# Ansible module: ansible.module_win_group


Add and remove local groups

## Description

Add and remove local groups.
For non-Windows targets, please use the M(group) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the group.']}",
    "name": "{'description': ['Name of the group.'], 'required': True}",
    "state": "{'description': ['Create or remove the group.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Create a new group
  win_group:
    name: deploy
    description: Deploy Group
    state: present

- name: Remove a group
  win_group:
    name: deploy
    state: absent

```

## License

TODO

## Author Information
  - ['Chris Hoffman (@chrishoffman)']
