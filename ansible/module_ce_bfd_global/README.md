# Ansible module: ansible.module_ce_bfd_global


Manages BFD global configuration on HUAWEI CloudEngine devices

## Description

Manages BFD global configuration on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "bfd_enable": "{'description': ['Enables the global Bidirectional Forwarding Detection (BFD) function.'], 'choices': ['enable', 'disable']}",
    "damp_init_wait_time": "{'description': ['Specifies an initial flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 2000.']}",
    "damp_max_wait_time": "{'description': ['Specifies a maximum flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 15000.']}",
    "damp_second_wait_time": "{'description': ['Specifies a secondary flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 5000.']}",
    "default_ip": "{'description': ['Specifies the default multicast IP address. The value ranges from 224.0.0.107 to 224.0.0.250.']}",
    "delay_up_time": "{'description': ['Specifies the delay before a BFD session becomes Up. The value is an integer ranging from 1 to 600, in seconds. The default value is 0, indicating that a BFD session immediately becomes Up.']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tos_exp_dynamic": "{'description': ['Indicates the priority of BFD control packets for dynamic BFD sessions. The value is an integer ranging from 0 to 7. The default priority is 7, which is the highest priority of BFD control packets.']}",
    "tos_exp_static": "{'description': ['Indicates the priority of BFD control packets for static BFD sessions. The value is an integer ranging from 0 to 7. The default priority is 7, which is the highest priority of BFD control packets.']}",
}
```

## Examples


``` yaml

- name: bfd global module test
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
  - name: Enable the global BFD function
    ce_bfd_global:
      bfd_enable: enable
      provider: '{{ cli }}'

  - name: Set the default multicast IP address to 224.0.0.150
    ce_bfd_global:
      bfd_enable: enable
      default_ip: 224.0.0.150
      state: present
      provider: '{{ cli }}'

  - name: Set the priority of BFD control packets for dynamic and static BFD sessions
    ce_bfd_global:
      bfd_enable: enable
      tos_exp_dynamic: 5
      tos_exp_static: 6
      state: present
      provider: '{{ cli }}'

  - name: Disable the global BFD function
    ce_bfd_global:
      bfd_enable: disable
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
