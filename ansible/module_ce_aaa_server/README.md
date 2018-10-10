# Ansible module: ansible.module_ce_aaa_server


Manages AAA server global configuration on HUAWEI CloudEngine switches

## Description

Manages AAA server global configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "accounting_mode": "{'description': ['Accounting Mode.'], 'choices': ['invalid', 'hwtacacs', 'radius', 'none']}",
    "acct_scheme_name": "{'description': ['Accounting scheme name. The value is a string of 1 to 32 characters.']}",
    "authen_scheme_name": "{'description': ['Name of an authentication scheme. The value is a string of 1 to 32 characters.']}",
    "author_scheme_name": "{'description': ['Name of an authorization scheme. The value is a string of 1 to 32 characters.']}",
    "domain_name": "{'description': ['Name of a domain. The value is a string of 1 to 64 characters.']}",
    "first_authen_mode": "{'description': ['Preferred authentication mode.'], 'choices': ['invalid', 'local', 'hwtacacs', 'radius', 'none']}",
    "first_author_mode": "{'description': ['Preferred authorization mode.'], 'choices': ['invalid', 'local', 'hwtacacs', 'if-authenticated', 'none']}",
    "hwtacas_template": "{'description': ['Name of a HWTACACS template. The value is a string of 1 to 32 case-insensitive characters.']}",
    "local_user_group": "{'description': ['Name of the user group where the user belongs. The user inherits all the rights of the user group. The value is a string of 1 to 32 characters.']}",
    "radius_server_group": "{'description': ["RADIUS server group's name. The value is a string of 1 to 32 case-insensitive characters."]}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: AAA server test
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

  - name: "Radius authentication Server Basic settings"
    ce_aaa_server:
      state: present
      authen_scheme_name: test1
      first_authen_mode: radius
      radius_server_group: test2
      provider: "{{ cli }}"

  - name: "Undo radius authentication Server Basic settings"
    ce_aaa_server:
      state: absent
      authen_scheme_name: test1
      first_authen_mode: radius
      radius_server_group: test2
      provider: "{{ cli }}"

  - name: "Hwtacacs accounting Server Basic settings"
    ce_aaa_server:
      state: present
      acct_scheme_name: test1
      accounting_mode: hwtacacs
      hwtacas_template: test2
      provider: "{{ cli }}"

  - name: "Undo hwtacacs accounting Server Basic settings"
    ce_aaa_server:
      state: absent
      acct_scheme_name: test1
      accounting_mode: hwtacacs
      hwtacas_template: test2
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
