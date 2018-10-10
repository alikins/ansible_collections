# Ansible module: ansible.module_ce_info_center_debug


Manages information center debug configuration on HUAWEI CloudEngine switches

## Description

Manages information center debug configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "channel_id": "{'description': ['Number of a channel. The value is an integer ranging from 0 to 9. The default value is 0.']}",
    "debug_enable": "{'description': ['Whether a device is enabled to output debugging information.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "debug_level": "{'description': ['Debug level permitted to output.'], 'choices': ['emergencies', 'alert', 'critical', 'error', 'warning', 'notification', 'informational', 'debugging']}",
    "debug_time_stamp": "{'description': ['Timestamp type of debugging information.'], 'choices': ['date_boot', 'date_second', 'date_tenthsecond', 'date_millisecond', 'shortdate_second', 'shortdate_tenthsecond', 'shortdate_millisecond', 'formatdate_second', 'formatdate_tenthsecond', 'formatdate_millisecond']}",
    "module_name": "{'description': ['Module name of the rule. The value is a string of 1 to 31 case-insensitive characters. The default value is default. Please use lower-case letter, such as [aaa, acl, arp, bfd].']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: CloudEngine info center debug test
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

  - name: "Config debug time stamp"
    ce_info_center_debug:
      state: present
      debug_time_stamp: date_boot
      provider: "{{ cli }}"

  - name: "Undo debug time stamp"
    ce_info_center_debug:
      state: absent
      debug_time_stamp: date_boot
      provider: "{{ cli }}"

  - name: "Config debug module log level"
    ce_info_center_debug:
      state: present
      module_name: aaa
      channel_id: 1
      debug_enable: true
      debug_level: error
      provider: "{{ cli }}"

  - name: "Undo debug module log level"
    ce_info_center_debug:
      state: absent
      module_name: aaa
      channel_id: 1
      debug_enable: true
      debug_level: error
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
