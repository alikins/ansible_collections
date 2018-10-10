# Ansible module: ansible.module_capabilities


Manage Linux capabilities

## Description

This module manipulates files privileges using the Linux capabilities(7) system.

## Requirements

TODO

## Arguments

``` json
{
    "capability": "{'description': ['Desired capability to set (with operator and flags, if state is C(present)) or remove (if state is C(absent))'], 'required': True, 'aliases': ['cap']}",
    "path": "{'description': ['Specifies the path to the file to be managed.'], 'required': True}",
    "state": "{'description': ["Whether the entry should be present or absent in the file's capabilities."], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Set cap_sys_chroot+ep on /foo
  capabilities:
    path: /foo
    capability: cap_sys_chroot+ep
    state: present

- name: Remove cap_net_bind_service from /bar
  capabilities:
    path: /bar
    capability: cap_net_bind_service
    state: absent

```

## License

TODO

## Author Information
  - ['Nate Coraor (@natefoo)']
