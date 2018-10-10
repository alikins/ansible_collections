# Ansible module: ansible.module_ce_switchport


Manages Layer 2 switchport interfaces on HUAWEI CloudEngine switches

## Description

Manages Layer 2 switchport interfaces on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "access_vlan": "{'description': ['If C(mode=access), used as the access VLAN ID, in the range from 1 to 4094.']}",
    "interface": "{'description': ['Full name of the interface, i.e. 40GE1/0/22.'], 'required': True}",
    "mode": "{'description': ['The link type of an interface.'], 'choices': ['access', 'trunk']}",
    "native_vlan": "{'description': ['If C(mode=trunk), used as the trunk native VLAN ID, in the range from 1 to 4094.']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'unconfigured']}",
    "trunk_vlans": "{'description': ['If C(mode=trunk), used as the VLAN range to ADD or REMOVE from the trunk, such as 2-10 or 2,5,10-15, etc.']}",
}
```

## Examples


``` yaml

- name: switchport module test
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
  - name: Ensure 10GE1/0/22 is in its default switchport state
    ce_switchport:
      interface: 10GE1/0/22
      state: unconfigured
      provider: '{{ cli }}'

  - name: Ensure 10GE1/0/22 is configured for access vlan 20
    ce_switchport:
      interface: 10GE1/0/22
      mode: access
      access_vlan: 20
      provider: '{{ cli }}'

  - name: Ensure 10GE1/0/22 only has vlans 5-10 as trunk vlans
    ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      native_vlan: 10
      trunk_vlans: 5-10
      provider: '{{ cli }}'

  - name: Ensure 10GE1/0/22 is a trunk port and ensure 2-50 are being tagged (doesn't mean others aren't also being tagged)
    ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      native_vlan: 10
      trunk_vlans: 2-50
      provider: '{{ cli }}'

  - name: Ensure these VLANs are not being tagged on the trunk
    ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      trunk_vlans: 51-4000
      state: absent
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
