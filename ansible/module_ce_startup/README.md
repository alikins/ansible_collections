# Ansible module: ansible.module_ce_startup


Manages a system startup information on HUAWEI CloudEngine switches

## Description

Manages a system startup information on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Display the startup information.'], 'choices': ['display']}",
    "cfg_file": "{'description': ['Name of the configuration file that is applied for the next startup. The value is a string of 5 to 255 characters.'], 'default': 'present'}",
    "patch_file": "{'description': ['Name of the patch file that is applied for the next startup.']}",
    "slot": "{'description': ['Position of the device.The value is a string of 1 to 32 characters. The possible value of slot is all, slave-board, or the specific slotID.']}",
    "software_file": "{'description': ['File name of the system software that is applied for the next startup. The value is a string of 5 to 255 characters.']}",
}
```

## Examples


``` yaml

- name: startup module test
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

  - name: Display startup information
    ce_startup:
      action: display
      provider: "{{ cli }}"

  - name: Set startup patch file
    ce_startup:
      patch_file: 2.PAT
      slot: all
      provider: "{{ cli }}"

  - name: Set startup software file
    ce_startup:
      software_file: aa.cc
      slot: 1
      provider: "{{ cli }}"

  - name: Set startup cfg file
    ce_startup:
      cfg_file: 2.cfg
      slot: 1
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
