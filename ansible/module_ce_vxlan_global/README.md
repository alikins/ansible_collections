# Ansible module: ansible.module_ce_vxlan_global


Manages global attributes of VXLAN and bridge domain on HUAWEI CloudEngine devices

## Description

Manages global attributes of VXLAN and bridge domain on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "bridge_domain_id": "{'description': ['Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215.']}",
    "nvo3_acl_extend": "{'description': ['Enabling or disabling the VXLAN ACL extension function.'], 'choices': ['enable', 'disable']}",
    "nvo3_ecmp_hash": "{'description': ['Load balancing of VXLAN packets through ECMP in optimized mode.'], 'choices': ['enable', 'disable']}",
    "nvo3_eth_trunk_hash": "{'description': ['Eth-Trunk from load balancing VXLAN packets in optimized mode.'], 'choices': ['enable', 'disable']}",
    "nvo3_gw_enhanced": "{'description': ['Configuring the Layer 3 VXLAN Gateway to Work in Non-loopback Mode.'], 'choices': ['l2', 'l3']}",
    "nvo3_prevent_loops": "{'description': ['Loop prevention of VXLAN traffic in non-enhanced mode. When the device works in non-enhanced mode, inter-card forwarding of VXLAN traffic may result in loops.'], 'choices': ['enable', 'disable']}",
    "nvo3_service_extend": "{'description': ['Enabling or disabling the VXLAN service extension function.'], 'choices': ['enable', 'disable']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tunnel_mode_vxlan": "{'description': ['Set the tunnel mode to VXLAN when configuring the VXLAN feature.'], 'choices': ['enable', 'disable']}",
}
```

## Examples


``` yaml

- name: vxlan global module test
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

  - name: Create bridge domain and set tunnel mode to VXLAN
    ce_vxlan_global:
      bridge_domain_id: 100
      nvo3_acl_extend: enable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
