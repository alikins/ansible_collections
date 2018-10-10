# Ansible module: ansible.module_ce_vxlan_arp


Manages ARP attributes of VXLAN on HUAWEI CloudEngine devices

## Description

Manages ARP attributes of VXLAN on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "arp_collect_host": "{'description': ['Enables EVN BGP or BGP EVPN to collect host information.'], 'choices': ['enable', 'disable']}",
    "arp_suppress": "{'description': ['Enables ARP broadcast suppression in a BD.'], 'choices': ['enable', 'disable']}",
    "bridge_domain_id": "{'description': ['Specifies a BD(bridge domain) ID. The value is an integer ranging from 1 to 16777215.']}",
    "evn_bgp": "{'description': ['Enables EVN BGP.'], 'choices': ['enable', 'disable']}",
    "evn_peer_ip": "{'description': ['Specifies the IP address of an EVN BGP peer. The value is in dotted decimal notation.']}",
    "evn_reflect_client": "{'description': ['Configures the local device as the route reflector (RR) and its peer as the client.'], 'choices': ['enable', 'disable']}",
    "evn_server": "{'description': ['Configures the local device as the router reflector (RR) on the EVN network.'], 'choices': ['enable', 'disable']}",
    "evn_source_ip": "{'description': ['Specifies the source address of an EVN BGP peer. The value is in dotted decimal notation.']}",
    "host_collect_protocol": "{'description': ['Enables EVN BGP or BGP EVPN to advertise host information.'], 'choices': ['bgp', 'none']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vbdif_name": "{'description': ['Full name of VBDIF interface, i.e. Vbdif100.']}",
}
```

## Examples


``` yaml

- name: vxlan arp module test
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

  - name: Configure EVN BGP on Layer 2 and Layer 3 VXLAN gateways to establish EVN BGP peer relationships.
    ce_vxlan_arp:
      evn_bgp: enable
      evn_source_ip: 6.6.6.6
      evn_peer_ip: 7.7.7.7
      provider: "{{ cli }}"
  - name: Configure a Layer 3 VXLAN gateway as a BGP RR.
    ce_vxlan_arp:
      evn_bgp: enable
      evn_server: enable
      provider: "{{ cli }}"
  - name: Enable EVN BGP on a Layer 3 VXLAN gateway to collect host information.
    ce_vxlan_arp:
      vbdif_name: Vbdif100
      arp_collect_host: enable
      provider: "{{ cli }}"
  - name: Enable Layer 2 and Layer 3 VXLAN gateways to use EVN BGP to advertise host information.
    ce_vxlan_arp:
      host_collect_protocol: bgp
      provider: "{{ cli }}"
  - name: Enable ARP broadcast suppression on a Layer 2 VXLAN gateway.
    ce_vxlan_arp:
      bridge_domain_id: 100
      arp_suppress: enable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
