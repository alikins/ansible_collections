# Ansible module: ansible.module_ce_mtu


Manages MTU settings on HUAWEI CloudEngine switches

## Description

Manages MTU settings on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "interface": "{'description': ['Full name of interface, i.e. 40GE1/0/22.']}",
    "jumbo_max": "{'description': ['Maximum frame size. The default value is 9216. The value is an integer and expressed in bytes. The value range is 1536 to 12224 for the CE12800 and 1536 to 12288 for ToR switches.']}",
    "jumbo_min": "{'description': ['Non-jumbo frame size threshod. The default value is 1518. The value is an integer that ranges from 1518 to jumbo_max, in bytes.']}",
    "mtu": "{'description': ['MTU for a specific interface. The value is an integer ranging from 46 to 9600, in bytes.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Mtu test
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

  - name: "Config jumboframe on 40GE1/0/22"
    ce_mtu:
      interface: 40GE1/0/22
      jumbo_max: 9000
      jumbo_min: 8000
      provider: "{{ cli }}"

  - name: "Config mtu on 40GE1/0/22 (routed interface)"
    ce_mtu:
      interface: 40GE1/0/22
      mtu: 1600
      provider: "{{ cli }}"

  - name: "Config mtu on 40GE1/0/23 (switched interface)"
    ce_mtu:
      interface: 40GE1/0/22
      mtu: 9216
      provider: "{{ cli }}"

  - name: "Config mtu and jumboframe on 40GE1/0/22 (routed interface)"
    ce_mtu:
      interface: 40GE1/0/22
      mtu: 1601
      jumbo_max: 9001
      jumbo_min: 8001
      provider: "{{ cli }}"

  - name: "Unconfigure mtu and jumboframe on a given interface"
    ce_mtu:
      state: absent
      interface: 40GE1/0/22
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
