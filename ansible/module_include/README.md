# Ansible module: ansible.module_include


Include a play or task list

## Description

Includes a file with a list of plays or tasks to be executed in the current playbook.
Files with a list of plays can only be included at the top level. Lists of tasks can only be included where tasks normally run (in play).
Before Ansible version 2.0, all includes were 'static' and were executed when the play was compiled.
Static includes are not subject to most directives. For example, loops or conditionals are applied instead to each inherited task.
Since Ansible 2.0, task includes are dynamic and behave more like real tasks. This means they can be looped, skipped and use variables from any source. Ansible tries to auto detect this, but you can use the `static` directive (which was added in Ansible 2.1) to bypass autodetection.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "free-form": "{'description': ['This module allows you to specify the name of the file directly without any other options.']}",
}
```

## Examples


``` yaml

- hosts: localhost
  tasks:
    - debug:
        msg: play1

- name: Include a play after another play
  include: otherplays.yaml


- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Include task list in play
      include: stuff.yaml

    - debug:
        msg: task10

- hosts: all
  tasks:
    - debug:
        msg: task1

    - name: Include task list in play only if the condition is true
      include: "{{ hostvar }}.yaml"
      static: no
      when: hostvar is defined

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
