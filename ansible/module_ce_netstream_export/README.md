# Ansible module: ansible.module_ce_netstream_export


Manages netstream export on HUAWEI CloudEngine switches

## Description

Configure NetStream flow statistics exporting and versions for exported packets on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "as_option": "{'description': ['Specifies the AS number recorded in the statistics as the original or the peer AS number.'], 'choices': ['origin', 'peer']}",
    "bgp_nexthop": "{'description': ['Configures the statistics to carry BGP next hop information. Currently, only V9 supports the exported packets carrying BGP next hop information.'], 'choices': ['enable', 'disable'], 'default': 'disable'}",
    "host_ip": "{'description': ['Specifies destination address which can be IPv6 or IPv4 of the exported NetStream packet.']}",
    "host_port": "{'description': ['Specifies the destination UDP port number of the exported packets. The value is an integer that ranges from 1 to 65535.']}",
    "host_vpn": "{'description': ['Specifies the VPN instance of the exported packets carrying flow statistics. Ensure the VPN instance has been created on the device.']}",
    "source_ip": "{'description': ['Specifies source address which can be IPv6 or IPv4 of the exported NetStream packet.']}",
    "state": "{'description': ['Manage the state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['Specifies NetStream feature.'], 'required': True, 'choices': ['ip', 'vxlan']}",
    "version": "{'description': ['Sets the version of exported packets.'], 'choices': ['5', '9']}",
}
```

## Examples


``` yaml

- name: netstream export module test
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

  - name: Configures the source address for the exported packets carrying IPv4 flow statistics.
    ce_netstream_export:
      type: ip
      source_ip: 192.8.2.2
      provider: "{{ cli }}"

  - name: Configures the source IP address for the exported packets carrying VXLAN flexible flow statistics.
    ce_netstream_export:
      type: vxlan
      source_ip: 192.8.2.3
      provider: "{{ cli }}"

  - name: Configures the destination IP address and destination UDP port number for the exported packets carrying IPv4 flow statistics.
    ce_netstream_export:
      type: ip
      host_ip: 192.8.2.4
      host_port: 25
      host_vpn: test
      provider: "{{ cli }}"

  - name: Configures the destination IP address and destination UDP port number for the exported packets carrying VXLAN flexible flow statistics.
    ce_netstream_export:
      type: vxlan
      host_ip: 192.8.2.5
      host_port: 26
      host_vpn: test
      provider: "{{ cli }}"

  - name: Configures the version number of the exported packets carrying IPv4 flow statistics.
    ce_netstream_export:
      type: ip
      version: 9
      as_option: origin
      bgp_nexthop: enable
      provider: "{{ cli }}"

  - name: Configures the version for the exported packets carrying VXLAN flexible flow statistics.
    ce_netstream_export:
      type: vxlan
      version: 9
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
