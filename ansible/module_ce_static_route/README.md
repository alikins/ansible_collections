# Ansible module: ansible.module_ce_static_route


Manages static route configuration on HUAWEI CloudEngine switches

## Description

Manages the static routes on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "aftype": "{'description': ['Destination ip address family type of static route.'], 'required': True, 'choices': ['v4', 'v6']}",
    "description": "{'description': ['Name of the route. Used with the name parameter on the CLI.']}",
    "destvrf": "{'description': ['VPN instance of next hop ip address.']}",
    "mask": "{'description': ['Destination ip mask of static route.'], 'required': True}",
    "next_hop": "{'description': ['Next hop address of static route.']}",
    "nhp_interface": "{'description': ['Next hop interface full name of static route.']}",
    "pref": "{'description': ['Preference or administrative difference of route (range 1-255).']}",
    "prefix": "{'description': ['Destination ip address of static route.'], 'required': True}",
    "state": "{'description': ['Specify desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tag": "{'description': ['Route tag value (numeric).']}",
    "vrf": "{'description': ['VPN instance of destination ip address.']}",
}
```

## Examples


``` yaml

- name: static route module test
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

  - name: Config a ipv4 static route, next hop is an address and that it has the proper description
    ce_static_route:
      prefix: 2.1.1.2
      mask: 24
      next_hop: 3.1.1.2
      description: 'Configured by Ansible'
      aftype: v4
      provider: "{{ cli }}"
  - name: Config a ipv4 static route ,next hop is an interface and that it has the proper description
    ce_static_route:
      prefix: 2.1.1.2
      mask: 24
      next_hop: 10GE1/0/1
      description: 'Configured by Ansible'
      aftype: v4
      provider: "{{ cli }}"
  - name: Config a ipv6 static route, next hop is an address and that it has the proper description
    ce_static_route:
      prefix: fc00:0:0:2001::1
      mask: 64
      next_hop: fc00:0:0:2004::1
      description: 'Configured by Ansible'
      aftype: v6
      provider: "{{ cli }}"
  - name: Config a ipv4 static route, next hop is an interface and that it has the proper description
    ce_static_route:
      prefix: fc00:0:0:2001::1
      mask: 64
      next_hop: 10GE1/0/1
      description: 'Configured by Ansible'
      aftype: v6
      provider: "{{ cli }}"
  - name: Config a VRF and set ipv4 static route, next hop is an address and that it has the proper description
    ce_static_route:
      vrf: vpna
      prefix: 2.1.1.2
      mask: 24
      next_hop: 3.1.1.2
      description: 'Configured by Ansible'
      aftype: v4
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Yang yang (@CloudEngine-Ansible)']
