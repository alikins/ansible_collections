# Ansible callback: ansible.callback_profile_tasks


adds time information to tasks

## Description

Ansible callback plugin for timing individual tasks and overall execution time.
Mashup of 2 excellent original works: https://github.com/jlafon/ansible-profile, https://github.com/junaid18183/ansible_home/blob/master/ansible_plugins/callback_plugins/timestamp.py.old
Format: C(<task start timestamp> (<length of previous task>) <current elapsed playbook execution time>)
It also lists the top/bottom time consuming tasks in the summary (configurable)
Before 2.4 only the environment variables were available for configuration.

## Requirements

TODO

## Arguments

``` json
{
    "output_limit": "{'description': ['Number of tasks to display in the summary'], 'default': 20, 'env': [{'name': 'PROFILE_TASKS_TASK_OUTPUT_LIMIT'}], 'ini': [{'section': 'callback_profile_tasks', 'key': 'task_output_limit'}]}",
    "sort_order": "{'description': ['Adjust the sorting output of summary tasks'], 'choices': ['descending', 'ascending', 'none'], 'default': 'descending', 'env': [{'name': 'PROFILE_TASKS_SORT_ORDER'}], 'ini': [{'section': 'callback_profile_tasks', 'key': 'sort_order'}]}",
}
```

## Examples


``` yaml

#
#    TASK: [ensure messaging security group exists] ********************************
#    Thursday 11 June 2017  22:50:53 +0100 (0:00:00.721)       0:00:05.322 *********
#    ok: [localhost]
#
#    TASK: [ensure db security group exists] ***************************************
#    Thursday 11 June 2017  22:50:54 +0100 (0:00:00.558)       0:00:05.880 *********
#    changed: [localhost]
#  '

```

## License

TODO

## Author Information
  - ['UNKNOWN']
