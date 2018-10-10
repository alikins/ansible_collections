# Ansible module: ansible.module_at


Schedule the execution of a command or script file via the at command

## Description

Use this module to schedule a command or script file to run once in the future.
All jobs are executed in the 'a' queue.

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['A command to be executed in the future.']}",
    "count": "{'description': ['The count of units in the future to execute the command or script file.'], 'required': True}",
    "script_file": "{'description': ['An existing script file to be executed in the future.']}",
    "state": "{'description': ['The state dictates if the command or script file should be evaluated as present(added) or absent(deleted).'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "unique": "{'description': ['If a matching job is present a new job will not be added.'], 'type': 'bool', 'default': False}",
    "units": "{'description': ['The type of units in the future to execute the command or script file.'], 'choices': ['minutes', 'hours', 'days', 'weeks'], 'required': True}",
}
```

## Examples


``` yaml

- name: Schedule a command to execute in 20 minutes as root.
  at:
    command: ls -d / >/dev/null
    count: 20
    units: minutes

- name: Match a command to an existing job and delete the job.
  at:
    command: ls -d / >/dev/null
    state: absent

- name: Schedule a command to execute in 20 minutes making sure it is unique in the queue.
  at:
    command: ls -d / >/dev/null
    count: 20
    units: minutes
    unique: yes

```

## License

TODO

## Author Information
  - ['Richard Isaacson (@risaacson)']
