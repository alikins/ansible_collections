# Ansible module: ansible.module_ce_bfd_session


Manages BFD session configuration on HUAWEI CloudEngine devices

## Description

Manages BFD session configuration, creates a BFD session or deletes a specified BFD session on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "addr_type": "{'description': ['Specifies the peer IP address type.'], 'choices': ['ipv4']}",
    "create_type": "{'description': ['BFD session creation mode, the currently created BFD session only supports static or static auto-negotiation mode.'], 'choices': ['static', 'auto']}",
    "dest_addr": "{'description': ['Specifies the peer IP address bound to the BFD session.']}",
    "out_if_name": "{'description': ['Specifies the type and number of the interface bound to the BFD session.']}",
    "session_name": "{'description': ['Specifies the name of a BFD session. The value is a string of 1 to 15 case-sensitive characters without spaces.'], 'required': True}",
    "src_addr": "{'description': ['Indicates the source IP address carried in BFD packets.']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "use_default_ip": "{'description': ['Indicates the default multicast IP address that is bound to a BFD session. By default, BFD uses the multicast IP address 224.0.0.184. You can set the multicast IP address by running the default-ip-address command. The value is a bool type.'], 'type': 'bool', 'default': False}",
    "vrf_name": "{'description': ['Specifies the name of a Virtual Private Network (VPN) instance that is bound to a BFD session. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value _public_ is reserved and cannot be used as the VPN instance name.']}",
}
```

## Examples


``` yaml

- name: bfd session module test
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
  - name: Configuring Single-hop BFD for Detecting Faults on a Layer 2 Link
    ce_bfd_session:
      session_name: bfd_l2link
      use_default_ip: true
      out_if_name: 10GE1/0/1
      provider: '{{ cli }}'

  - name: Configuring Single-Hop BFD on a VLANIF Interface
    ce_bfd_session:
      session_name: bfd_vlanif
      dest_addr: 10.1.1.6
      out_if_name: Vlanif100
      provider: '{{ cli }}'

  - name: Configuring Multi-Hop BFD
    ce_bfd_session:
      session_name: bfd_multi_hop
      dest_addr: 10.1.1.1
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
