# Ansible module: ansible.module_ce_snmp_traps


Manages SNMP traps configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP traps configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "feature_name": "{'description': ['Alarm feature name.'], 'choices': ['aaa', 'arp', 'bfd', 'bgp', 'cfg', 'configuration', 'dad', 'devm', 'dhcpsnp', 'dldp', 'driver', 'efm', 'erps', 'error-down', 'fcoe', 'fei', 'fei_comm', 'fm', 'ifnet', 'info', 'ipsg', 'ipv6', 'isis', 'l3vpn', 'lacp', 'lcs', 'ldm', 'ldp', 'ldt', 'lldp', 'mpls_lspm', 'msdp', 'mstp', 'nd', 'netconf', 'nqa', 'nvo3', 'openflow', 'ospf', 'ospfv3', 'pim', 'pim-std', 'qos', 'radius', 'rm', 'rmon', 'securitytrap', 'smlktrap', 'snmp', 'ssh', 'stackmng', 'sysclock', 'sysom', 'system', 'tcp', 'telnet', 'trill', 'trunk', 'tty', 'vbst', 'vfs', 'virtual-perception', 'vrrp', 'vstm', 'all']}",
    "interface_number": "{'description': ['Interface number.']}",
    "interface_type": "{'description': ['Interface type.'], 'choices': ['Ethernet', 'Eth-Trunk', 'Tunnel', 'NULL', 'LoopBack', 'Vlanif', '100GE', '40GE', 'MTunnel', '10GE', 'GE', 'MEth', 'Vbdif', 'Nve']}",
    "port_number": "{'description': ['Source port number.']}",
    "trap_name": "{'description': ['Alarm trap name.']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp traps test
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

  - name: "Config SNMP trap all enable"
    ce_snmp_traps:
      state: present
      feature_name: all
      provider: "{{ cli }}"

  - name: "Config SNMP trap interface"
    ce_snmp_traps:
      state: present
      interface_type: 40GE
      interface_number: 2/0/1
      provider: "{{ cli }}"

  - name: "Config SNMP trap port"
    ce_snmp_traps:
      state: present
      port_number: 2222
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
