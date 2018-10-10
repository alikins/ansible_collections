# Ansible module: ansible.module_ce_netstream_global


Manages global parameters of NetStream on HUAWEI CloudEngine switches

## Description

Manages global parameters of NetStream on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "index_switch": "{'description': ['Specifies the netstream index-switch.'], 'choices': ['16', '32'], 'default': '16'}",
    "interface": "{'description': ['Netstream global interface.'], 'required': True}",
    "sampler_direction": "{'description': ['Specifies the netstream sampler direction.'], 'choices': ['inbound', 'outbound']}",
    "sampler_interval": "{'description': ['Specifies the netstream sampler interval, length is 1 - 65535.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "statistics_direction": "{'description': ['Specifies the netstream statistic direction.'], 'choices': ['inbound', 'outbound']}",
    "statistics_record": "{'description': ['Specifies the flexible netstream statistic record, length is 1 - 32.']}",
    "type": "{'description': ['Specifies the type of netstream global.'], 'choices': ['ip', 'vxlan'], 'default': 'ip'}",
}
```

## Examples


``` yaml

- name: netstream global module test
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

  - name: Configure a netstream sampler at interface 10ge1/0/2, direction is outbound,interval is 30.
    ce_netstream_global:
      interface: 10ge1/0/2
      type: ip
      sampler_interval: 30
      sampler_direction: outbound
      state: present
      provider: "{{ cli }}"
  - name: Configure a netstream flexible statistic at interface 10ge1/0/2, record is test1, type is ip.
    ce_netstream_global:
      type: ip
      interface: 10ge1/0/2
      statistics_record: test1
      provider: "{{ cli }}"
  - name: Set the vxlan index-switch to 32.
    ce_netstream_global:
      type: vxlan
      interface: all
      index_switch: 32
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['YangYang (@CloudEngine-Ansible)']
