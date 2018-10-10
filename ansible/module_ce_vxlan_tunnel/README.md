# Ansible module: ansible.module_ce_vxlan_tunnel


Manages VXLAN tunnel configuration on HUAWEI CloudEngine devices

## Description

This module offers the ability to set the VNI and mapped to the BD, and configure an ingress replication list on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "bridge_domain_id": "{'description': ['Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215.']}",
    "nve_mode": "{'description': ['Specifies the working mode of an NVE interface.'], 'choices': ['mode-l2', 'mode-l3']}",
    "nve_name": "{'description': ['Specifies the number of an NVE interface. The value ranges from 1 to 2.']}",
    "peer_list_ip": "{'description': ['Specifies the IP address of a remote VXLAN tunnel endpoints (VTEP). The value is in dotted decimal notation.']}",
    "protocol_type": "{'description': ['The operation type of routing protocol.'], 'choices': ['bgp', 'null']}",
    "source_ip": "{'description': ['Specifies an IP address for a source VTEP. The value is in dotted decimal notation.']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vni_id": "{'description': ['Specifies a VXLAN network identifier (VNI) ID. The value is an integer ranging from 1 to 16000000.']}",
}
```

## Examples


``` yaml

- name: vxlan tunnel module test
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

  - name: Make sure nve_name is exist, ensure vni_id and protocol_type is configured on Nve1 interface.
    ce_vxlan_tunnel:
      nve_name: Nve1
      vni_id: 100
      protocol_type: bgp
      state: present
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
