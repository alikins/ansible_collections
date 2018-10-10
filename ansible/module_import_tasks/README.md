# Ansible module: ansible.module_import_tasks


Import a task list

## Description

Imports a list of tasks to be added to the current playbook for subsequent execution.

## Requirements

TODO

## Arguments

``` json
{
    "free-form": "{'description': ['The name of the imported file is specified directly without any other option.', 'Most keywords, including loops and conditionals, only applied to the imported tasks, not to this statement itself. If you need any of those to apply, use M(include_tasks) instead.']}",
}
```

## Examples


``` yaml

- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Include task list in play
      import_tasks: stuff.yaml

    - debug:
        msg: task10

- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Apply conditional to all imported tasks
      import_tasks: stuff.yaml
      when: hostvar is defined

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
