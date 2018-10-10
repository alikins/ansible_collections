# Ansible module: ansible.module_group


Add or remove groups

## Description

Manage presence of groups on a host.
For Windows targets, use the M(win_group) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "gid": "{'description': ['Optional I(GID) to set for the group.']}",
    "local": "{'version_added': '2.6', 'required': False, 'default': 'no', 'description': ['Forces the use of "local" command alternatives on platforms that implement it. This is useful in environments that use centralized authentification when you want to manipulate the local groups. I.E. it uses `lgroupadd` instead of `useradd`.', 'This requires that these commands exist on the targeted host, otherwise it will be a fatal error.']}",
    "name": "{'description': ['Name of the group to manage.'], 'required': True}",
    "state": "{'description': ['Whether the group should be present or not on the remote host.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "system": "{'description': ['If I(yes), indicates that the group created is a system group.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Ensure group "somegroup" exists
  group:
    name: somegroup
    state: present

```

## License

TODO

## Author Information
  - ['Stephen Fromm (@sfromm)']
