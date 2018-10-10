# Ansible module: ansible.module_ce_snmp_contact


Manages SNMP contact configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP contact configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "contact": "{'description': ['Contact information.'], 'required': True}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp contact test
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

  - name: "Config SNMP contact"
    ce_snmp_contact:
      state: present
      contact: call Operator at 010-99999999
      provider: "{{ cli }}"

  - name: "Undo SNMP contact"
    ce_snmp_contact:
      state: absent
      contact: call Operator at 010-99999999
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
