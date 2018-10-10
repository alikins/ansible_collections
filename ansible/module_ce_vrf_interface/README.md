# Ansible module: ansible.module_ce_vrf_interface


Manages interface specific VPN configuration on HUAWEI CloudEngine switches

## Description

Manages interface specific VPN configuration of HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "state": "{'description': ['Manage the state of the resource.'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "vpn_interface": "{'description': ['An interface that can binding VPN instance, i.e. 40GE1/0/22, Vlanif10. Must be fully qualified interface name. Interface types, such as 10GE, 40GE, 100GE, LoopBack, MEth, Tunnel, Vlanif....'], 'required': True}",
    "vrf": "{'description': ['VPN instance, the length of vrf name is 1 ~ 31, i.e. "test", but can not be C(_public_).'], 'required': True}",
}
```

## Examples


``` yaml

- name: VRF interface test
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

  - name: "Configure a VPN instance for the interface"
    ce_vrf_interface:
      vpn_interface: 40GE1/0/2
      vrf: test
      state: present
      provider: "{{ cli }}"

  - name: "Disable the association between a VPN instance and an interface"
    ce_vrf_interface:
      vpn_interface: 40GE1/0/2
      vrf: test
      state: absent
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
