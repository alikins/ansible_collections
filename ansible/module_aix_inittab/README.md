# Ansible module: ansible.module_aix_inittab


Manages the inittab on AIX

## Description

Manages the inittab on AIX.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Action what the init has to do with this entry.'], 'required': True, 'choices': ['boot', 'bootwait', 'hold', 'initdefault', False, 'once', 'ondemand', 'powerfail', 'powerwait', 'respawn', 'sysinit', 'wait']}",
    "command": "{'description': ['What command has to run.'], 'required': True}",
    "insertafter": "{'description': ['After which inittabline should the new entry inserted.']}",
    "name": "{'description': ['Name of the inittab entry.'], 'required': True, 'aliases': ['service']}",
    "runlevel": "{'description': ['Runlevel of the entry.'], 'required': True}",
    "state": "{'description': ['Whether the entry should be present or absent in the inittab file.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Add service startmyservice to the inittab, directly after service existingservice.
- name: Add startmyservice to inittab
  aix_inittab:
    name: startmyservice
    runlevel: 4
    action: once
    command: echo hello
    insertafter: existingservice
    state: present
  become: yes

# Change inittab entry startmyservice to runlevel "2" and processaction "wait".
- name: Change startmyservice to inittab
  aix_inittab:
    name: startmyservice
    runlevel: 2
    action: wait
    command: echo hello
    state: present
  become: yes

- name: Remove startmyservice from inittab
  aix_inittab:
    name: startmyservice
    runlevel: 2
    action: wait
    command: echo hello
    state: absent
  become: yes

```

## License

TODO

## Author Information
  - ['Joris Weijters (@molekuul)']
