# Ansible module: ansible.module_ce_rollback


Set a checkpoint or rollback to a checkpoint on HUAWEI CloudEngine switches

## Description

This module offers the ability to set a configuration checkpoint file or rollback to a configuration checkpoint file on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The operation of configuration rollback.'], 'required': True, 'choices': ['rollback', 'clear', 'set', 'display', 'commit']}",
    "commit_id": "{'description': ['Specifies the label of the configuration rollback point to which system configurations are expected to roll back. The value is an integer that the system generates automatically.']}",
    "filename": "{'description': ['Specifies a configuration file for configuration rollback. The value is a string of 5 to 64 case-sensitive characters in the format of *.zip, *.cfg, or *.dat, spaces not supported.']}",
    "label": "{'description': ['Specifies a user label for a configuration rollback point. The value is a string of 1 to 256 case-sensitive ASCII characters, spaces not supported. The value must start with a letter and cannot be presented in a single hyphen (-).']}",
    "last": "{'description': ['Specifies the number of configuration rollback points. The value is an integer that ranges from 1 to 80.']}",
    "oldest": "{'description': ['Specifies the number of configuration rollback points. The value is an integer that ranges from 1 to 80.']}",
}
```

## Examples


``` yaml

- name: rollback module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

- name: Ensure commit_id is exist, and specifies the label of the configuration rollback point to
        which system configurations are expected to roll back.
  ce_rollback:
    commit_id: 1000000748
    action: rollback
    provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
