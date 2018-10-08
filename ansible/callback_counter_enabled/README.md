# Ansible callback: ansible.callback_counter_enabled


adds counters to the output items (tasks and hosts/task)

## Description

Use this callback when you need a kind of progress bar on a large environments.
You will know how many tasks has the playbook to run, and wich one is actually running.
You will know how many hosts may run a task, and wich of them is actually running.

## Requirements

TODO

## Arguments

``` json
{
    "display_failed_stderr": "{'name': 'Use STDERR for failed tasks', 'description': ['Toggle to control whether failed tasks are displayed to STDERR (vs. STDOUT)'], 'default': False, 'env': [{'name': 'ANSIBLE_DISPLAY_FAILED_STDERR'}], 'ini': [{'key': 'display_failed_stderr', 'section': 'defaults'}], 'type': 'boolean', 'version_added': '2.7'}",
    "display_ok_hosts": "{'name': "Show 'ok' hosts", 'description': ["Toggle to control displaying 'ok' task/host results in a task"], 'default': True, 'env': [{'name': 'ANSIBLE_DISPLAY_OK_HOSTS'}], 'ini': [{'key': 'display_ok_hosts', 'section': 'defaults'}], 'type': 'boolean', 'version_added': '2.7'}",
    "display_skipped_hosts": "{'name': 'Show skipped hosts', 'description': ['Toggle to control displaying skipped task/host results in a task'], 'default': True, 'env': [{'name': 'DISPLAY_SKIPPED_HOSTS'}], 'ini': [{'key': 'display_skipped_hosts', 'section': 'defaults'}], 'type': 'boolean'}",
    "show_custom_stats": "{'name': 'Show custom stats', 'description': ['This adds the custom stats set via the set_stats plugin to the play recap'], 'default': False, 'env': [{'name': 'ANSIBLE_SHOW_CUSTOM_STATS'}], 'ini': [{'key': 'show_custom_stats', 'section': 'defaults'}], 'type': 'bool'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
