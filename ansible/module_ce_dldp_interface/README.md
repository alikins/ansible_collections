# Ansible module: ansible.module_ce_dldp_interface


Manages interface DLDP configuration on HUAWEI CloudEngine switches

## Description

Manages interface DLDP configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "enable": "{'description': ['Set interface DLDP enable state.'], 'choices': ['enable', 'disable']}",
    "interface": "{'description': ['Must be fully qualified interface name, i.e. GE1/0/1, 10GE1/0/1, 40GE1/0/22, 100GE1/0/1.'], 'required': True}",
    "local_mac": "{'description': ['Set the source MAC address for DLDP packets sent in the DLDP-compatible mode. The value of MAC address is in H-H-H format. H contains 1 to 4 hexadecimal digits.']}",
    "mode_enable": "{'description': ['Set DLDP compatible-mode enable state.'], 'choices': ['enable', 'disable']}",
    "reset": "{'description': ['Specify whether reseting interface DLDP state.'], 'choices': ['enable', 'disable']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: DLDP interface test
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

  - name: "Configure interface DLDP enable state and ensure global dldp enable is turned on"
    ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      provider: "{{ cli }}"

  - name: "Configuire interface DLDP compatible-mode enable state  and ensure interface DLDP state is already enabled"
    ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      mode_enable: enable
      provider: "{{ cli }}"

  - name: "Configuire the source MAC address for DLDP packets sent in the DLDP-compatible mode  and
           ensure interface DLDP state and compatible-mode enable state  is already enabled"
    ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      mode_enable: enable
      local_mac: aa-aa-aa
      provider: "{{ cli }}"

  - name: "Reset DLDP state of specified interface and ensure interface DLDP state is already enabled"
    ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      reset: enable
      provider: "{{ cli }}"

  - name: "Unconfigure interface DLDP local mac addreess when C(state=absent)"
    ce_dldp_interface:
      interface: 40GE2/0/1
      state: absent
      local_mac: aa-aa-aa
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhou Zhijin (@CloudEngine-Ansible)']
