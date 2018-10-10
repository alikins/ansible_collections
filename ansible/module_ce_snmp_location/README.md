# Ansible module: ansible.module_ce_snmp_location


Manages SNMP location configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP location configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "location": "{'description': ['Location information.'], 'required': True}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp location test
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

  - name: "Config SNMP location"
    ce_snmp_location:
      state: present
      location: nanjing China
      provider: "{{ cli }}"

  - name: "Remove SNMP location"
    ce_snmp_location:
      state: absent
      location: nanjing China
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
