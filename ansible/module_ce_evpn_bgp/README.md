# Ansible module: ansible.module_ce_evpn_bgp


Manages BGP EVPN configuration on HUAWEI CloudEngine switches

## Description

This module offers the ability to configure a BGP EVPN peer relationship on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "advertise_l2vpn_evpn": "{'description': ['Enable or disable a device to advertise IP routes imported to a VPN instance to its EVPN instance.'], 'choices': ['enable', 'disable']}",
    "advertise_router_type": "{'description': ['Configures a device to advertise routes to its BGP EVPN peers.'], 'choices': ['arp', 'irb']}",
    "as_number": "{'description': ['Specifies integral AS number. The value is an integer ranging from 1 to 4294967295.']}",
    "bgp_instance": "{'description': ['Name of a BGP instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported.'], 'required': True}",
    "peer_address": "{'description': ['Specifies the IPv4 address of a BGP EVPN peer. The value is in dotted decimal notation.']}",
    "peer_enable": "{'description': ['Enable or disable a BGP device to exchange routes with a specified peer or peer group in the address family view.'], 'choices': ['true', 'false']}",
    "peer_group_name": "{'description': ['Specify the name of a peer group that BGP peers need to join. The value is a string of 1 to 47 case-sensitive characters, spaces not supported.']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpn_name": "{'description': ['Associates a specified VPN instance with the IPv4 address family. The value is a string of 1 to 31 case-sensitive characters, spaces not supported.']}",
}
```

## Examples


``` yaml

- name: evpn bgp module test
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

  - name: Enable peer address.
    ce_evpn_bgp:
      bgp_instance: 100
      peer_address: 1.1.1.1
      as_number: 100
      peer_enable: true
      provider: "{{ cli }}"

  - name: Enable peer group arp.
    ce_evpn_bgp:
      bgp_instance: 100
      peer_group_name: aaa
      advertise_router_type: arp
      provider: "{{ cli }}"

  - name: Enable advertise l2vpn evpn.
    ce_evpn_bgp:
      bgp_instance: 100
      vpn_name: aaa
      advertise_l2vpn_evpn: enable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
