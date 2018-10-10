# Ansible module: ansible.module_ce_ip_interface


Manages L3 attributes for IPv4 and IPv6 interfaces on HUAWEI CloudEngine switches

## Description

Manages Layer 3 attributes for IPv4 and IPv6 interfaces on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "addr": "{'description': ['IPv4 or IPv6 Address.']}",
    "interface": "{'description': ['Full name of interface, i.e. 40GE1/0/22, vlanif10.'], 'required': True}",
    "ipv4_type": "{'description': ['Specifies an address type. The value is an enumerated type. main, primary IP address. sub, secondary IP address.'], 'default': 'main', 'choices': ['main', 'sub']}",
    "mask": "{'description': ['Subnet mask for IPv4 or IPv6 Address in decimal format.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "version": "{'description': ['IP address version.'], 'default': 'v4', 'choices': ['v4', 'v6']}",
}
```

## Examples


``` yaml

- name: ip_interface module test
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
  - name: Ensure ipv4 address is configured on 10GE1/0/22
    ce_ip_interface:
      interface: 10GE1/0/22
      version: v4
      state: present
      addr: 20.20.20.20
      mask: 24
      provider: '{{ cli }}'

  - name: Ensure ipv4 secondary address is configured on 10GE1/0/22
    ce_ip_interface:
      interface: 10GE1/0/22
      version: v4
      state: present
      addr: 30.30.30.30
      mask: 24
      ipv4_type: sub
      provider: '{{ cli }}'

  - name: Ensure ipv6 is enabled on 10GE1/0/22
    ce_ip_interface:
      interface: 10GE1/0/22
      version: v6
      state: present
      provider: '{{ cli }}'

  - name: Ensure ipv6 address is configured on 10GE1/0/22
    ce_ip_interface:
      interface: 10GE1/0/22
      version: v6
      state: present
      addr: 2001::db8:800:200c:cccb
      mask: 64
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
