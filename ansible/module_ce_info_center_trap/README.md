# Ansible module: ansible.module_ce_info_center_trap


Manages information center trap configuration on HUAWEI CloudEngine switches

## Description

Manages information center trap configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "channel_id": "{'description': ['Number of a channel. The value is an integer ranging from 0 to 9. The default value is 0.']}",
    "module_name": "{'description': ['Module name of the rule. The value is a string of 1 to 31 case-insensitive characters. The default value is default. Please use lower-case letter, such as [aaa, acl, arp, bfd].']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trap_buff_enable": "{'description': ['Whether a trap buffer is enabled to output information.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "trap_buff_size": "{'description': ['Size of a trap buffer. The value is an integer ranging from 0 to 1024. The default value is 256.']}",
    "trap_enable": "{'description': ['Whether a device is enabled to output alarms.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "trap_level": "{'description': ['Trap level permitted to output.'], 'choices': ['emergencies', 'alert', 'critical', 'error', 'warning', 'notification', 'informational', 'debugging']}",
    "trap_time_stamp": "{'description': ['Timestamp format of alarm information.'], 'choices': ['date_boot', 'date_second', 'date_tenthsecond', 'date_millisecond', 'shortdate_second', 'shortdate_tenthsecond', 'shortdate_millisecond', 'formatdate_second', 'formatdate_tenthsecond', 'formatdate_millisecond']}",
}
```

## Examples


``` yaml


- name: CloudEngine info center trap test
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

  - name: "Config trap buffer"
    ce_info_center_trap:
      state: present
      trap_buff_enable: true
      trap_buff_size: 768
      provider: "{{ cli }}"

  - name: "Undo trap buffer"
    ce_info_center_trap:
      state: absent
      trap_buff_enable: true
      trap_buff_size: 768
      provider: "{{ cli }}"

  - name: "Config trap module log level"
    ce_info_center_trap:
      state: present
      module_name: aaa
      channel_id: 1
      trap_enable: true
      trap_level: error
      provider: "{{ cli }}"

  - name: "Undo trap module log level"
    ce_info_center_trap:
      state: absent
      module_name: aaa
      channel_id: 1
      trap_enable: true
      trap_level: error
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
