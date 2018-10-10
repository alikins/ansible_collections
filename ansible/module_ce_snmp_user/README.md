# Ansible module: ansible.module_ce_snmp_user


Manages SNMP user configuration on HUAWEI CloudEngine switches

## Description

Manages SNMP user configurations on CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "aaa_local_user": "{'description': ['Unique name to identify the local user.']}",
    "acl_number": "{'description': ['Access control list number.']}",
    "auth_key": "{'description': ['The authentication password. Password length, 8-255 characters.']}",
    "auth_protocol": "{'description': ['Authentication protocol.'], 'choices': ['noAuth', 'md5', 'sha']}",
    "priv_key": "{'description': ['The encryption password. Password length 8-255 characters.']}",
    "priv_protocol": "{'description': ['Encryption protocol.'], 'choices': ['noPriv', 'des56', '3des168', 'aes128', 'aes192', 'aes256']}",
    "remote_engine_id": "{'description': ['Remote engine id of the USM user.']}",
    "user_group": "{'description': ['Name of the group where user belongs to.']}",
    "usm_user_name": "{'description': ['Unique name to identify the USM user.']}",
}
```

## Examples


``` yaml


- name: CloudEngine snmp user test
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

  - name: "Config SNMP usm user"
    ce_snmp_user:
      state: present
      usm_user_name: wdz_snmp
      remote_engine_id: 800007DB03389222111200
      acl_number: 2000
      user_group: wdz_group
      provider: "{{ cli }}"

  - name: "Undo SNMP usm user"
    ce_snmp_user:
      state: absent
      usm_user_name: wdz_snmp
      remote_engine_id: 800007DB03389222111200
      acl_number: 2000
      user_group: wdz_group
      provider: "{{ cli }}"

  - name: "Config SNMP local user"
    ce_snmp_user:
      state: present
      aaa_local_user: wdz_user
      auth_protocol: md5
      auth_key: huawei123
      priv_protocol: des56
      priv_key: huawei123
      provider: "{{ cli }}"

  - name: "Config SNMP local user"
    ce_snmp_user:
      state: absent
      aaa_local_user: wdz_user
      auth_protocol: md5
      auth_key: huawei123
      priv_protocol: des56
      priv_key: huawei123
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
