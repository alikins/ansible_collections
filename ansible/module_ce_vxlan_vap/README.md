# Ansible module: ansible.module_ce_vxlan_vap


Manages VXLAN virtual access point on HUAWEI CloudEngine Devices

## Description

Manages VXLAN Virtual access point on HUAWEI CloudEngine Devices.

## Requirements

TODO

## Arguments

``` json
{
    "bind_vlan_id": "{'description': ['Specifies the VLAN binding to a BD(Bridge Domain). The value is an integer ranging ranging from 1 to 4094.']}",
    "bridge_domain_id": "{'description': ['Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215.']}",
    "ce_vid": "{'description': ["When I(encapsulation) is 'dot1q', specifies a VLAN ID in the outer VLAN tag. When I(encapsulation) is 'qinq', specifies an outer VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. The value is an integer ranging from 1 to 4094."]}",
    "encapsulation": "{'description': ['Specifies an encapsulation type of packets allowed to pass through a Layer 2 sub-interface.'], 'choices': ['dot1q', 'default', 'untag', 'qinq', 'none']}",
    "l2_sub_interface": "{'description': ['Specifies an Sub-Interface full name, i.e. "10GE1/0/41.1". The value is a string of 1 to 63 case-insensitive characters, spaces supported.']}",
    "pe_vid": "{'description': ["When I(encapsulation) is 'qinq', specifies an inner VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. The value is an integer ranging from 1 to 4094."]}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: vxlan vap module test
  hosts: ce128
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

  - name: Create a papping between a VLAN and a BD
    ce_vxlan_vap:
      bridge_domain_id: 100
      bind_vlan_id: 99
      provider: "{{ cli }}"

  - name: Bind a Layer 2 sub-interface to a BD
    ce_vxlan_vap:
      bridge_domain_id: 100
      l2_sub_interface: 10GE2/0/20.1
      provider: "{{ cli }}"

  - name: Configure an encapsulation type on a Layer 2 sub-interface
    ce_vxlan_vap:
      l2_sub_interface: 10GE2/0/20.1
      encapsulation: dot1q
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
