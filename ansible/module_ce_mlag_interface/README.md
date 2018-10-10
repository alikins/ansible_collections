# Ansible module: ansible.module_ce_mlag_interface


Manages MLAG interfaces on HUAWEI CloudEngine switches

## Description

Manages MLAG interface attributes on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "dfs_group_id": "{'description': ['ID of a DFS group.The value is 1.'], 'default': 'present'}",
    "eth_trunk_id": "{'description': ['Name of the local M-LAG interface. The value is ranging from 0 to 511.']}",
    "interface": "{'description': ['Name of the interface that enters the Error-Down state when the peer-link fails. The value is a string of 1 to 63 characters.']}",
    "mlag_error_down": "{'description': ['Configure the interface on the slave device to enter the Error-Down state.'], 'choices': ['enable', 'disable']}",
    "mlag_id": "{'description': ['ID of the M-LAG. The value is an integer that ranges from 1 to 2048.']}",
    "mlag_priority_id": "{'description': ['M-LAG global LACP system priority. The value is an integer ranging from 0 to 65535. The default value is 32768.']}",
    "mlag_system_id": "{'description': ['M-LAG global LACP system MAC address. The value is a string of 0 to 255 characters. The default value is the MAC address of the Ethernet port of MPU.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: mlag interface module test
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

  - name: Set interface mlag error down
    ce_mlag_interface:
      interface: 10GE2/0/1
      mlag_error_down: enable
      provider: "{{ cli }}"
  - name: Create mlag
    ce_mlag_interface:
      eth_trunk_id: 1
      dfs_group_id: 1
      mlag_id: 4
      provider: "{{ cli }}"
  - name: Set mlag global attribute
    ce_mlag_interface:
      mlag_system_id: 0020-1409-0407
      mlag_priority_id: 5
      provider: "{{ cli }}"
  - name: Set mlag interface attribute
    ce_mlag_interface:
      eth_trunk_id: 1
      mlag_system_id: 0020-1409-0400
      mlag_priority_id: 3
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
