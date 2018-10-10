# Ansible module: ansible.module_ce_vxlan_gateway


Manages gateway for the VXLAN network on HUAWEI CloudEngine devices

## Description

Configuring Centralized All-Active Gateways or Distributed Gateway for the VXLAN Network on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "arp_direct_route": "{'description': ['Enable VLINK direct route on VBDIF interface.'], 'choices': ['enable', 'disable']}",
    "arp_distribute_gateway": "{'description': ['Enable the distributed gateway function on VBDIF interface.'], 'choices': ['enable', 'disable']}",
    "dfs_all_active": "{'description': ['Creates all-active gateways.'], 'choices': ['enable', 'disable']}",
    "dfs_id": "{'description': ['Specifies the ID of a DFS group. The value must be 1.']}",
    "dfs_peer_ip": "{'description': ['Configure the IP address of an all-active gateway peer. The value is in dotted decimal notation.']}",
    "dfs_peer_vpn": "{'description': ['Specifies the name of the VPN instance that is associated with all-active gateway peer. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value C(_public_) is reserved and cannot be used as the VPN instance name.']}",
    "dfs_source_ip": "{'description': ['Specifies the IPv4 address bound to a DFS group. The value is in dotted decimal notation.']}",
    "dfs_source_vpn": "{'description': ['Specifies the name of a VPN instance bound to a DFS group. The value is a string of 1 to 31 case-sensitive characters without spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. The value C(_public_) is reserved and cannot be used as the VPN instance name.']}",
    "dfs_udp_port": "{'description': ['Specifies the UDP port number of the DFS group. The value is an integer that ranges from 1025 to 65535.']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vbdif_bind_vpn": "{'description': ['Specifies the name of the VPN instance that is associated with the interface. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value C(_public_) is reserved and cannot be used as the VPN instance name.']}",
    "vbdif_mac": "{'description': ['Specifies a MAC address for a VBDIF interface. The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number, such as C(00e0) or C(fc01). If an H contains less than four digits, 0s are added ahead. For example,  C(e0) is equal to C(00e0). A MAC address cannot be all 0s or 1s or a multicast MAC address.']}",
    "vbdif_name": "{'description': ['Full name of VBDIF interface, i.e. Vbdif100.']}",
    "vpn_instance": "{'description': ['Specifies the name of a VPN instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value C(_public_) is reserved and cannot be used as the VPN instance name.']}",
    "vpn_vni": "{'description': ['Specifies a VNI ID. Binds a VXLAN network identifier (VNI) to a virtual private network (VPN) instance. The value is an integer ranging from 1 to 16000000.']}",
}
```

## Examples


``` yaml

- name: vxlan gateway module test
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

  - name: Configuring Centralized All-Active Gateways for the VXLAN Network
    ce_vxlan_gateway:
      dfs_id: 1
      dfs_source_ip: 6.6.6.6
      dfs_all_active: enable
      dfs_peer_ip: 7.7.7.7
      provider: "{{ cli }}"
  - name: Bind the VPN instance to a Layer 3 gateway, enable distributed gateway, and configure host route advertisement.
    ce_vxlan_gateway:
      vbdif_name: Vbdif100
      vbdif_bind_vpn: vpn1
      arp_distribute_gateway: enable
      arp_direct_route: enable
      provider: "{{ cli }}"
  - name: Assign a VNI to a VPN instance.
    ce_vxlan_gateway:
      vpn_instance: vpn1
      vpn_vni: 100
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
