# Ansible module: ansible.module_ce_link_status


Get interface link status on HUAWEI CloudEngine switches

## Description

Get interface link status on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "interface": "{'description': ['For the interface parameter, you can enter C(all) to display information about all interface, an interface type such as C(40GE) to display information about interfaces of the specified type, or full name of an interface such as C(40GE1/0/22) or C(vlanif10) to display information about the specific interface.'], 'required': True}",
}
```

## Examples


``` yaml


- name: Link status test
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

  - name: Get specified interface link status information
    ce_link_status:
      interface: 40GE1/0/1
      provider: "{{ cli }}"

  - name: Get specified interface type link status information
    ce_link_status:
      interface: 40GE
      provider: "{{ cli }}"

  - name: Get all interface link status information
    ce_link_status:
      interface: all
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
