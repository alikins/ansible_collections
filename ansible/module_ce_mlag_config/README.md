# Ansible module: ansible.module_ce_mlag_config


Manages MLAG configuration on HUAWEI CloudEngine switches

## Description

Manages MLAG configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "dfs_group_id": "{'description': ['ID of a DFS group. The value is 1.'], 'default': 'present'}",
    "eth_trunk_id": "{'description': ['Name of the peer-link interface. The value is in the range from 0 to 511.']}",
    "ip_address": "{'description': ['IP address bound to the DFS group. The value is in dotted decimal notation.']}",
    "nickname": "{'description': ['The nickname bound to a DFS group. The value is an integer that ranges from 1 to 65471.']}",
    "peer_link_id": "{'description': ['Number of the peer-link interface. The value is 1.']}",
    "priority_id": "{'description': ['Priority of a DFS group. The value is an integer that ranges from 1 to 254. The default value is 100.']}",
    "pseudo_nickname": "{'description': ['A pseudo nickname of a DFS group. The value is an integer that ranges from 1 to 65471.']}",
    "pseudo_priority": "{'description': ['The priority of a pseudo nickname. The value is an integer that ranges from 128 to 255. The default value is 192. A larger value indicates a higher priority.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpn_instance_name": "{'description': ['Name of the VPN instance bound to the DFS group. The value is a string of 1 to 31 case-sensitive characters without spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. The value _public_ is reserved and cannot be used as the VPN instance name.']}",
}
```

## Examples


``` yaml

- name: mlag config module test
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

  - name: Create DFS Group id
    ce_mlag_config:
      dfs_group_id: 1
      provider: "{{ cli }}"
  - name: Set dfs-group priority
    ce_mlag_config:
      dfs_group_id: 1
      priority_id: 3
      state: present
      provider: "{{ cli }}"
  - name: Set pseudo nickname
    ce_mlag_config:
      dfs_group_id: 1
      pseudo_nickname: 3
      pseudo_priority: 130
      state: present
      provider: "{{ cli }}"
  - name: Set ip
    ce_mlag_config:
      dfs_group_id: 1
      ip_address: 11.1.1.2
      vpn_instance_name: 6
      provider: "{{ cli }}"
  - name: Set peer link
    ce_mlag_config:
      eth_trunk_id: 3
      peer_link_id: 2
      state: present
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
