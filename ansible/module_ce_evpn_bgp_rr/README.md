# Ansible module: ansible.module_ce_evpn_bgp_rr


Manages RR for the VXLAN Network on HUAWEI CloudEngine switches

## Description

Configure an RR in BGP-EVPN address family view on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "as_number": "{'description': ['Specifies the number of the AS, in integer format. The value is an integer that ranges from 1 to 4294967295.'], 'required': True}",
    "bgp_evpn_enable": "{'description': ['Enable or disable the BGP-EVPN address family.'], 'choices': ['enable', 'disable'], 'default': 'enable'}",
    "bgp_instance": "{'description': ['Specifies the name of a BGP instance. The value of instance-name can be an integer 1 or a string of 1 to 31.']}",
    "peer": "{'description': ['Specifies the IPv4 address or the group name of a peer.']}",
    "peer_type": "{'description': ['Specify the peer type.'], 'choices': ['group_name', 'ipv4_address']}",
    "policy_vpn_target": "{'description': ['Enable or disable the VPN-Target filtering.'], 'choices': ['enable', 'disable']}",
    "reflect_client": "{'description': ['Configure the local device as the route reflector and the peer or peer group as the client of the route reflector.'], 'choices': ['enable', 'disable']}",
}
```

## Examples


``` yaml

- name: BGP RR test
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

  - name: "Configure BGP-EVPN address family view and ensure that BGP view has existed."
    ce_evpn_bgp_rr:
      as_number: 20
      bgp_evpn_enable: enable
      provider: "{{ cli }}"

  - name: "Configure reflect client and ensure peer has existed."
    ce_evpn_bgp_rr:
      as_number: 20
      peer_type: ipv4_address
      peer: 192.8.3.3
      reflect_client: enable
      provider: "{{ cli }}"

  - name: "Configure the VPN-Target filtering."
    ce_evpn_bgp_rr:
      as_number: 20
      policy_vpn_target: enable
      provider: "{{ cli }}"

  - name: "Configure an RR in BGP-EVPN address family view."
    ce_evpn_bgp_rr:
      as_number: 20
      bgp_evpn_enable: enable
      peer_type: ipv4_address
      peer: 192.8.3.3
      reflect_client: enable
      policy_vpn_target: disable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
