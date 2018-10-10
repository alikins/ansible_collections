# Ansible module: ansible.module_ce_acl_interface


Manages applying ACLs to interfaces on HUAWEI CloudEngine switches

## Description

Manages applying ACLs to interfaces on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "acl_name": "{'description': ['ACL number or name. For a numbered rule group, the value ranging from 2000 to 4999. For a named rule group, the value is a string of 1 to 32 case-sensitive characters starting with a letter, spaces not supported.'], 'required': True}",
    "direction": "{'description': ['Direction ACL to be applied in on the interface.'], 'required': True, 'choices': ['inbound', 'outbound']}",
    "interface": "{'description': ['Interface name. Only support interface full name, such as "40GE2/0/1".'], 'required': True}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: CloudEngine acl interface test
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

  - name: "Apply acl to interface"
    ce_acl_interface:
      state: present
      acl_name: 2000
      interface: 40GE1/0/1
      direction: outbound
      provider: "{{ cli }}"

  - name: "Undo acl from interface"
    ce_acl_interface:
      state: absent
      acl_name: 2000
      interface: 40GE1/0/1
      direction: outbound
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
