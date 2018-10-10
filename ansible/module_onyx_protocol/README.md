# Ansible module: ansible.module_onyx_protocol


Enables/Disables protocols on Mellanox ONYX network devices

## Description

This module provides a mechanism for enabling and disabling protocols Mellanox on ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "bgp": "{'description': ['BGP protocol'], 'choices': ['enabled', 'disabled']}",
    "dcb_pfc": "{'description': ['DCB priority flow control'], 'choices': ['enabled', 'disabled']}",
    "igmp_snooping": "{'description': ['IP IGMP snooping'], 'choices': ['enabled', 'disabled']}",
    "ip_l3": "{'description': ['IP L3 support'], 'choices': ['enabled', 'disabled']}",
    "ip_routing": "{'description': ['IP routing support'], 'choices': ['enabled', 'disabled']}",
    "lacp": "{'description': ['LACP protocol'], 'choices': ['enabled', 'disabled']}",
    "lldp": "{'description': ['LLDP protocol'], 'choices': ['enabled', 'disabled']}",
    "magp": "{'description': ['MAGP protocol'], 'choices': ['enabled', 'disabled']}",
    "mlag": "{'description': ['MLAG protocol'], 'choices': ['enabled', 'disabled']}",
    "ospf": "{'description': ['OSPF protocol'], 'choices': ['enabled', 'disabled']}",
    "spanning_tree": "{'description': ['Spanning Tree support'], 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: enable protocols for MLAG
  onyx_protocol:
    lacp: enabled
    spanning_tree: disabled
    ip_routing: enabled
    mlag: enabled
    dcb_pfc: enabled

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
