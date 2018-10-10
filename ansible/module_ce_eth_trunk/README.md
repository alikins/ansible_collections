# Ansible module: ansible.module_ce_eth_trunk


Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches

## Description

Manages Eth-Trunk specific configuration parameters on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['When true it forces Eth-Trunk members to match what is declared in the members param. This can be used to remove members.'], 'type': 'bool', 'default': False}",
    "hash_type": "{'description': ['Hash algorithm used for load balancing among Eth-Trunk member interfaces.'], 'choices': ['src-dst-ip', 'src-dst-mac', 'enhanced', 'dst-ip', 'dst-mac', 'src-ip', 'src-mac']}",
    "members": "{'description': ['List of interfaces that will be managed in a given Eth-Trunk. The interface name must be full name.']}",
    "min_links": "{'description': ['Specifies the minimum number of Eth-Trunk member links in the Up state. The value is an integer ranging from 1 to the maximum number of interfaces that can be added to a Eth-Trunk interface.']}",
    "mode": "{'description': ['Specifies the working mode of an Eth-Trunk interface.'], 'choices': ['manual', 'lacp-dynamic', 'lacp-static']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trunk_id": "{'description': ['Eth-Trunk interface number. The value is an integer. The value range depends on the assign forward eth-trunk mode command. When 256 is specified, the value ranges from 0 to 255. When 512 is specified, the value ranges from 0 to 511. When 1024 is specified, the value ranges from 0 to 1023.'], 'required': True}",
}
```

## Examples


``` yaml

- name: eth_trunk module test
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
  - name: Ensure Eth-Trunk100 is created, add two members, and set to mode lacp-static
    ce_eth_trunk:
      trunk_id: 100
      members: ['10GE1/0/24','10GE1/0/25']
      mode: 'lacp-static'
      state: present
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
