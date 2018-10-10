# Ansible module: ansible.module_ce_vrf_af


Manages VPN instance address family on HUAWEI CloudEngine switches

## Description

Manages VPN instance address family of HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "evpn": "{'description': ['Is extend vpn or normal vpn.'], 'type': 'bool', 'default': False}",
    "route_distinguisher": "{'description': ['VPN instance route distinguisher,the RD used to distinguish same route prefix from different vpn. The RD must be setted before setting vpn_target_value.']}",
    "state": "{'description': ['Manage the state of the af.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vpn_target_state": "{'description': ['Manage the state of the vpn target.'], 'choices': ['present', 'absent']}",
    "vpn_target_type": "{'description': ['VPN instance vpn target type.'], 'choices': ['export_extcommunity', 'import_extcommunity']}",
    "vpn_target_value": "{'description': ['VPN instance target value. Such as X.X.X.X:number<0-65535> or number<0-65535>:number<0-4294967295> or number<0-65535>.number<0-65535>:number<0-65535> or number<65536-4294967295>:number<0-65535> but not support 0:0 and 0.0:0.']}",
    "vrf": "{'description': ['VPN instance.'], 'required': True}",
    "vrf_aftype": "{'description': ['VPN instance address family.'], 'choices': ['v4', 'v6'], 'default': 'v4'}",
}
```

## Examples


``` yaml

- name: vrf af module test
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

  - name: Config vpna, set address family is ipv4
    ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      state: present
      provider: "{{ cli }}"
  - name: Config vpna, delete address family is ipv4
    ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      state: absent
      provider: "{{ cli }}"
  - name: Config vpna, set address family is ipv4,rd=1:1,set vpn_target_type=export_extcommunity,vpn_target_value=2:2
    ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      route_distinguisher: 1:1
      vpn_target_type: export_extcommunity
      vpn_target_value: 2:2
      vpn_target_state: present
      state: present
      provider: "{{ cli }}"
  - name: Config vpna, set address family is ipv4,rd=1:1,delete vpn_target_type=export_extcommunity,vpn_target_value=2:2
    ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      route_distinguisher: 1:1
      vpn_target_type: export_extcommunity
      vpn_target_value: 2:2
      vpn_target_state: absent
      state: present
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Yang yang (@CloudEngine-Ansible)']
