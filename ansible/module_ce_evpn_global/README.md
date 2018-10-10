# Ansible module: ansible.module_ce_evpn_global


Manages global configuration of EVPN on HUAWEI CloudEngine switches

## Description

Manages global configuration of EVPN on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "evpn_overlay_enable": "{'description': ['Configure EVPN as the VXLAN control plane.'], 'required': True, 'choices': ['enable', 'disable']}",
}
```

## Examples


``` yaml

- name: evpn global module test
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

  - name: Configure EVPN as the VXLAN control plan
    ce_evpn_global:
      evpn_overlay_enable: enable
      provider: "{{ cli }}"

  - name: Undo EVPN as the VXLAN control plan
    ce_evpn_global:
      evpn_overlay_enable: disable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
