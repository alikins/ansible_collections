# Ansible module: ansible.module_ce_snmp_target_host


Manages SNMP target host configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP target host configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Network Address.']}",
    "connect_port": "{'description': ['Udp port used by SNMP agent to connect the Network management.']}",
    "host_name": "{'description': ['Unique name to identify target host entry.']}",
    "interface_name": "{'description': ['Name of the interface to send the trap message.']}",
    "is_public_net": "{'description': ['To enable or disable Public Net-manager for target Host.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "notify_type": "{'description': ['To configure notify type as trap or inform.'], 'choices': ['trap', 'inform']}",
    "recv_port": "{'description': ['UDP Port number used by network management to receive alarm messages.']}",
    "security_level": "{'description': ['Security level indicating whether to use authentication and encryption.'], 'choices': ['noAuthNoPriv', 'authentication', 'privacy']}",
    "security_model": "{'description': ['Security Model.'], 'choices': ['v1', 'v2c', 'v3']}",
    "security_name": "{'description': ['Security Name.']}",
    "security_name_v3": "{'description': ['Security Name V3.']}",
    "version": "{'description': ['Version(s) Supported by SNMP Engine.'], 'choices': ['none', 'v1', 'v2c', 'v3', 'v1v2c', 'v1v3', 'v2cv3', 'all']}",
    "vpn_name": "{'description': ['VPN instance Name.']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp target host test
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

  - name: "Config SNMP version"
    ce_snmp_target_host:
      state: present
      version: v2cv3
      provider: "{{ cli }}"

  - name: "Config SNMP target host"
    ce_snmp_target_host:
      state: present
      host_name: test1
      address: 1.1.1.1
      notify_type: trap
      vpn_name: js
      security_model: v2c
      security_name: wdz
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
