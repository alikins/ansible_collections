# Ansible module: ansible.module_ce_reboot


Reboot a HUAWEI CloudEngine switches

## Description

Reboot a HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "confirm": "{'description': ["Safeguard boolean. Set to true if you're sure you want to reboot."], 'type': 'bool', 'default': False}",
    "save_config": "{'description': ['Flag indicating whether to save the configuration.'], 'required': False, 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: reboot module test
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
  - name: Reboot the device
    ce_reboot:
      confirm: true
      save_config: true
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Gong Jianjun (@CloudEngine-Ansible)']
