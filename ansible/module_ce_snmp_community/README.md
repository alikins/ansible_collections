# Ansible module: ansible.module_ce_snmp_community


Manages SNMP community configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP community configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "access_right": "{'description': ['Access right read or write.'], 'choices': ['read', 'write']}",
    "acl_number": "{'description': ['Access control list number.']}",
    "community_mib_view": "{'description': ['Mib view name.']}",
    "community_name": "{'description': ['Unique name to identify the community.']}",
    "group_name": "{'description': ['Unique name to identify the SNMPv3 group.']}",
    "notify_view": "{'description': ['Mib view name for notification.']}",
    "read_view": "{'description': ['Mib view name for read.']}",
    "security_level": "{'description': ['Security level indicating whether to use authentication and encryption.'], 'choices': ['noAuthNoPriv', 'authentication', 'privacy']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "write_view": "{'description': ['Mib view name for write.']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp community test
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

  - name: "Config SNMP community"
    ce_snmp_community:
      state: present
      community_name: Wdz123456789
      access_right: write
      provider: "{{ cli }}"

  - name: "Undo SNMP community"
    ce_snmp_community:
      state: absent
      community_name: Wdz123456789
      access_right: write
      provider: "{{ cli }}"

  - name: "Config SNMP group"
    ce_snmp_community:
      state: present
      group_name: wdz_group
      security_level: noAuthNoPriv
      acl_number: 2000
      provider: "{{ cli }}"

  - name: "Undo SNMP group"
    ce_snmp_community:
      state: absent
      group_name: wdz_group
      security_level: noAuthNoPriv
      acl_number: 2000
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
