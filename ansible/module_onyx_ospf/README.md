# Ansible module: ansible.module_onyx_ospf


Manage OSPF protocol on Mellanox ONYX network devices

## Description

This module provides declarative management and configuration of OSPF protocol on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "interfaces": "{'description': ['List of interfaces and areas. Required if I(state=present).'], 'suboptions': {'name': {'description': ['Intrface name.'], 'required': True}, 'area': {'description': ['OSPF area.'], 'required': True}}}",
    "ospf": "{'description': ['OSPF instance number 1-65535'], 'required': True}",
    "router_id": "{'description': ['OSPF router ID. Required if I(state=present).']}",
    "state": "{'description': ['OSPF state.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: add ospf router to interface
  onyx_ospf:
    ospf: 2
    router_id: 192.168.8.2
    interfaces:
      - name: Eth1/1
      - area: 0.0.0.0

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
