# Ansible module: ansible.module_ce_acl


Manages base ACL configuration on HUAWEI CloudEngine switches

## Description

Manages base ACL configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "acl_description": "{'description': ['ACL description. The value is a string of 1 to 127 characters.']}",
    "acl_name": "{'description': ['ACL number or name. For a numbered rule group, the value ranging from 2000 to 2999 indicates a basic ACL. For a named rule group, the value is a string of 1 to 32 case-sensitive characters starting with a letter, spaces not supported.'], 'required': True}",
    "acl_num": "{'description': ['ACL number. The value is an integer ranging from 2000 to 2999.']}",
    "acl_step": "{'description': ['ACL step. The value is an integer ranging from 1 to 20. The default value is 5.']}",
    "frag_type": "{'description': ['Type of packet fragmentation.'], 'choices': ['fragment', 'clear_fragment']}",
    "log_flag": "{'description': ['Flag of logging matched data packets.'], 'type': 'bool', 'default': False}",
    "rule_action": "{'description': ['Matching mode of basic ACL rules.'], 'choices': ['permit', 'deny']}",
    "rule_description": "{'description': ['Description about an ACL rule. The value is a string of 1 to 127 characters.']}",
    "rule_id": "{'description': ['ID of a basic ACL rule in configuration mode. The value is an integer ranging from 0 to 4294967294.']}",
    "rule_name": "{'description': ['Name of a basic ACL rule. The value is a string of 1 to 32 characters. The value is case-insensitive, and cannot contain spaces or begin with an underscore (_).']}",
    "source_ip": "{'description': ['Source IP address. The value is a string of 0 to 255 characters.The default value is 0.0.0.0. The value is in dotted decimal notation.']}",
    "src_mask": "{'description': ['Mask of a source IP address. The value is an integer ranging from 1 to 32.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'delete_acl']}",
    "time_range": "{'description': ['Name of a time range in which an ACL rule takes effect. The value is a string of 1 to 32 characters. The value is case-insensitive, and cannot contain spaces. The name must start with an uppercase or lowercase letter. In addition, the word "all" cannot be specified as a time range name.']}",
    "vrf_name": "{'description': ['VPN instance name. The value is a string of 1 to 31 characters.The default value is _public_.']}",
}
```

## Examples


``` yaml


- name: CloudEngine acl test
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

  - name: "Config ACL"
    ce_acl:
      state: present
      acl_name: 2200
      provider: "{{ cli }}"

  - name: "Undo ACL"
    ce_acl:
      state: delete_acl
      acl_name: 2200
      provider: "{{ cli }}"

  - name: "Config ACL base rule"
    ce_acl:
      state: present
      acl_name: 2200
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      time_range: wdz_acl_time
      provider: "{{ cli }}"

  - name: "undo ACL base rule"
    ce_acl:
      state: absent
      acl_name: 2200
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      time_range: wdz_acl_time
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
