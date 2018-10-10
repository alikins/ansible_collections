# Ansible module: ansible.module_ce_evpn_bd_vni


Manages EVPN VXLAN Network Identifier (VNI) on HUAWEI CloudEngine switches

## Description

Manages Ethernet Virtual Private Network (EVPN) VXLAN Network Identifier (VNI) configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "bridge_domain_id": "{'description': ['Specify an existed bridge domain (BD).The value is an integer ranging from 1 to 16777215.'], 'required': True}",
    "evpn": "{'description': ['Create or delete an EVPN instance for a VXLAN in BD view.'], 'choices': ['enable', 'disable'], 'default': 'enable'}",
    "route_distinguisher": "{'description': ['Configures a route distinguisher (RD) for a BD EVPN instance. The format of an RD can be as follows', '1) 2-byte AS number:4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0:0.', '2) Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535.', '3) 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535.', '4) A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0.0:0.', '5) 32-bit IP address:2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535.', "6) 'auto' specifies the RD that is automatically generated."]}",
    "state": "{'description': ['Manage the state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vpn_target_both": "{'description': ['Add VPN targets to both the import and export VPN target lists of a BD EVPN instance. The format is the same as route_distinguisher.']}",
    "vpn_target_export": "{'description': ['Add VPN targets to the export VPN target list of a BD EVPN instance. The format is the same as route_distinguisher.']}",
    "vpn_target_import": "{'description': ['Add VPN targets to the import VPN target list of a BD EVPN instance. The format is the same as route_distinguisher.'], 'required': True}",
}
```

## Examples


``` yaml

- name: EVPN BD VNI test
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

  - name: "Configure an EVPN instance for a VXLAN in BD view"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      evpn: enable
      provider: "{{ cli }}"

  - name: "Configure a route distinguisher (RD) for a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      route_distinguisher: '22:22'
      provider: "{{ cli }}"

  - name: "Configure VPN targets to both the import and export VPN target lists of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_both: 22:100,22:101
      provider: "{{ cli }}"

  - name: "Configure VPN targets to the import VPN target list of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_import: 22:22,22:23
      provider: "{{ cli }}"

  - name: "Configure VPN targets to the export VPN target list of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_export: 22:38,22:39
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to both the import and export VPN target lists of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_both: '22:100'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to the import VPN target list of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_import: '22:22'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to the export VPN target list of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_export: '22:38'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure a route distinguisher (RD) of a BD EVPN instance"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      route_distinguisher: '22:22'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure an EVPN instance for a VXLAN in BD view"
    ce_evpn_bd_vni:
      bridge_domain_id: 20
      evpn: disable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
