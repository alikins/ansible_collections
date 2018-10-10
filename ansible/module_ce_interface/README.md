# Ansible module: ansible.module_ce_interface


Manages physical attributes of interfaces on HUAWEI CloudEngine switches

## Description

Manages physical attributes of interfaces on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['Specifies the interface management status. The value is an enumerated type. up, An interface is in the administrative Up state. down, An interface is in the administrative Down state.'], 'choices': ['up', 'down']}",
    "description": "{'description': ['Specifies an interface description. The value is a string of 1 to 242 case-sensitive characters, spaces supported but question marks (?) not supported.']}",
    "interface": "{'description': ['Full name of interface, i.e. 40GE1/0/10, Tunnel1.']}",
    "interface_type": "{'description': ['Interface type to be configured from the device.'], 'choices': ['ge', '10ge', '25ge', '4x10ge', '40ge', '100ge', 'vlanif', 'loopback', 'meth', 'eth-trunk', 'nve', 'tunnel', 'ethernet', 'fcoe-port', 'fabric-port', 'stack-port', 'null']}",
    "l2sub": "{'description': ['Specifies whether the interface is a Layer 2 sub-interface.'], 'type': 'bool', 'default': False}",
    "mode": "{'description': ['Manage Layer 2 or Layer 3 state of the interface.'], 'choices': ['layer2', 'layer3']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'default']}",
}
```

## Examples


``` yaml

- name: interface module test
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
  - name: Ensure an interface is a Layer 3 port and that it has the proper description
    ce_interface:
      interface: 10GE1/0/22
      description: 'Configured by Ansible'
      mode: layer3
      provider: '{{ cli }}'

  - name: Admin down an interface
    ce_interface:
      interface: 10GE1/0/22
      admin_state: down
      provider: '{{ cli }}'

  - name: Remove all tunnel interfaces
    ce_interface:
      interface_type: tunnel
      state: absent
      provider: '{{ cli }}'

  - name: Remove all logical interfaces
    ce_interface:
      interface_type: '{{ item }}'
      state: absent
      provider: '{{ cli }}'
    with_items:
      - loopback
      - eth-trunk
      - nve

  - name: Admin up all 10GE interfaces
    ce_interface:
      interface_type: 10GE
      admin_state: up
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
