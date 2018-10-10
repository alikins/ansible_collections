# Ansible module: ansible.module_ce_dldp


Manages global DLDP configuration on HUAWEI CloudEngine switches

## Description

Manages global DLDP configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "auth_mode": "{'description': ['Specifies authentication algorithm of DLDP.'], 'choices': ['md5', 'simple', 'sha', 'hmac-sha256', 'none']}",
    "auth_pwd": "{'description': ['Specifies authentication password. The value is a string of 1 to 16 case-sensitive plaintexts or 24/32/48/108/128 case-sensitive encrypted characters. The string excludes a question mark (?).']}",
    "enable": "{'description': ['Set global DLDP enable state.'], 'choices': ['enable', 'disable']}",
    "reset": "{'description': ['Specify whether reset DLDP state of disabled interfaces.'], 'choices': ['enable', 'disable']}",
    "time_internal": "{'description': ['Specifies the interval for sending Advertisement packets. The value is an integer ranging from 1 to 100, in seconds. The default interval for sending Advertisement packets is 5 seconds.']}",
    "work_mode": "{'description': ['Set global DLDP work-mode.'], 'choices': ['enhance', 'normal']}",
}
```

## Examples


``` yaml

- name: DLDP test
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

  - name: "Configure global DLDP enable state"
    ce_dldp:
      enable: enable
      provider: "{{ cli }}"

  - name: "Configure DLDP work-mode and ensure global DLDP state is already enabled"
    ce_dldp:
      enable: enable
      work_mode: normal
      provider: "{{ cli }}"

  - name: "Configure advertisement message time interval in seconds and ensure global DLDP state is already enabled"
    ce_dldp:
      enable: enable
      time_interval: 6
      provider: "{{ cli }}"

  - name: "Configure a DLDP authentication mode and ensure global DLDP state is already enabled"
    ce_dldp:
      enable: enable
      auth_mode: md5
      auth_pwd: abc
      provider: "{{ cli }}"

  - name: "Reset DLDP state of disabled interfaces and ensure global DLDP state is already enabled"
    ce_dldp:
      enable: enable
      reset: enable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
