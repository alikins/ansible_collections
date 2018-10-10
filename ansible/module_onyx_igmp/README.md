# Ansible module: ansible.module_onyx_igmp


Configures IGMP globl parameters

## Description

This module provides declarative management of IGMP protocol params on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "default_version": "{'description': ['Configure the default operating version of the IGMP snooping'], 'choices': ['V2', 'V3']}",
    "last_member_query_interval": "{'description': ['Configure the last member query interval, range 1-25']}",
    "mrouter_timeout": "{'description': ['Configure the mrouter timeout, range 60-600']}",
    "port_purge_timeout": "{'description': ['Configure the host port purge timeout, range 130-1225']}",
    "proxy_reporting": "{'description': ['Configure ip igmp snooping proxy and enable reporting mode'], 'choices': ['enabled', 'disabled']}",
    "report_suppression_interval": "{'description': ['Configure the report suppression interval, range 1-25']}",
    "state": "{'description': ['IGMP state.'], 'required': True, 'choices': ['enabled', 'disabled']}",
    "unregistered_multicast": "{'description': ['Configure the unregistered multicast mode Flood unregistered multicast Forward unregistered multicast to mrouter ports'], 'choices': ['flood', 'forward-to-mrouter-ports']}",
}
```

## Examples


``` yaml

- name: configure igmp
  onyx_igmp:
    state: enabled
    unregistered_multicast: flood

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
