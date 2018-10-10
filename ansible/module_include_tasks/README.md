# Ansible module: ansible.module_include_tasks


Dynamically include a task list

## Description

Includes a file with a list of tasks to be executed in the current playbook.

## Requirements

TODO

## Arguments

``` json
{
    "apply": "{'description': ['Accepts a hash of task keywords (e.g. C(tags), C(become)) that will be applied to the tasks within the include.'], 'version_added': '2.7'}",
    "file": "{'description': ['The name of the imported file is specified directly without any other option.', 'Unlike M(import_tasks), most keywords, including loops and conditionals, apply to this statement.'], 'version_added': '2.7'}",
    "free-form": "{'description': ['Supplying a file name via free-form C(- include_tasks: file.yml) of a file to be included is the equivalent\nof specifying an argument of I(file).\n']}",
}
```

## Examples


``` yaml

- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Include task list in play
      include_tasks: stuff.yaml

    - debug:
        msg: task10

- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Include task list in play only if the condition is true
      include_tasks: "{{ hostvar }}.yaml"
      when: hostvar is defined

- name: Apply tags to tasks within included file
  include_tasks:
    file: install.yml
    apply:
      tags:
        - install
  tags:
    - always

- name: Apply tags to tasks within included file when using free-form
  include_tasks: install.yml
  args:
    apply:
      tags:
        - install
  tags:
    - always

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
