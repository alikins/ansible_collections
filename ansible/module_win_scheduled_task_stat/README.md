# Ansible module: ansible.module_win_scheduled_task_stat


Get information about Windows Scheduled Tasks

## Description

Will return whether the folder and task exists.
Returns the names of tasks in the folder specified.
If C(name) is set and exists, will return information on the task itself.
Use M(win_scheduled_task) to configure a scheduled task.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the scheduled task to get information for.']}",
    "path": "{'description': ['The folder path where the task lives.'], 'default': '\\'}",
}
```

## Examples


``` yaml

- name: get information about a folder
  win_scheduled_task_stat:
    path: \folder name
  register: task_folder_stat

- name: get information about a task in the root folder
  win_scheduled_task_stat:
    name: task name
  register: task_stat

- name: get information about a task in a custom folder
  win_scheduled_task_stat:
    path: \folder name
    name: task name
  register: task_stat

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
