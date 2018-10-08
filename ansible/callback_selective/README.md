# Ansible callback: ansible.callback_selective


only print certain tasks

## Description

This callback only prints tasks that have been tagged with `print_action` or that have failed. This allows operators to focus on the tasks that provide value only.
Tasks that are not printed are placed with a '.'.
If you increase verbosity all tasks are printed.

## Requirements

TODO

## Arguments

``` json
{
    "nocolor": "{'default': False, 'description': ['This setting allows suppressing colorizing output'], 'env': [{'name': 'ANSIBLE_NOCOLOR'}, {'name': 'ANSIBLE_SELECTIVE_DONT_COLORIZE'}], 'ini': [{'section': 'defaults', 'key': 'nocolor'}], 'type': 'boolean'}",
}
```

## Examples


``` yaml

  - debug: msg="This will not be printed"
  - debug: msg="But this will"
    tags: [print_action]

```

## License

TODO

## Author Information
  - ['UNKNOWN']
