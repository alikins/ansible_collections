# Ansible module: ansible.module_import_playbook


Import a playbook

## Description

Includes a file with a list of plays to be executed.
Files with a list of plays can only be included at the top level. You cannot use this action inside a play.

## Requirements

TODO

## Arguments

``` json
{
    "free-form": "{'description': ['The name of the imported playbook is specified directly without any other option.']}",
}
```

## Examples


``` yaml

- hosts: localhost
  tasks:
    - debug:
        msg: play1

- name: Include a play after another play
  import_playbook: otherplays.yaml


- name: This DOES NOT WORK
  hosts: all
  tasks:
    - debug:
        msg: task1

    - name: This fails because I'm inside a play already
      import_playbook: stuff.yaml

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
