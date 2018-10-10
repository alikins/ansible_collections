# Ansible module: ansible.module_ce_vlan


Manages VLAN resources and attributes on Huawei CloudEngine switches

## Description

Manages VLAN configurations on Huawei CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Specify VLAN description, in the range from 1 to 80.']}",
    "name": "{'description': ['Name of VLAN, in the range from 1 to 31.']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vlan_id": "{'description': ['Single VLAN ID, in the range from 1 to 4094.']}",
    "vlan_range": "{'description': ['Range of VLANs such as C(2-10) or C(2,5,10-15), etc.']}",
}
```

## Examples


``` yaml

- name: vlan module test
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

  - name: Ensure a range of VLANs are not present on the switch
    ce_vlan:
      vlan_range: "2-10,20,50,55-60,100-150"
      state: absent
      provider: "{{ cli }}"

  - name: Ensure VLAN 50 exists with the name WEB
    ce_vlan:
      vlan_id: 50
      name: WEB
      state: absent
      provider: "{{ cli }}"

  - name: Ensure VLAN is NOT on the device
    ce_vlan:
      vlan_id: 50
      state: absent
      provider: "{{ cli }}"


```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
