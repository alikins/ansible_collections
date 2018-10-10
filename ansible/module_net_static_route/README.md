# Ansible module: ansible.module_net_static_route


Manage static IP routes on network appliances (routers, switches et. al.)

## Description

This module provides declarative management of static IP routes on network appliances (routers, switches et. al.).

## Requirements

TODO

## Arguments

``` json
{
    "admin_distance": "{'description': ['Admin distance of the static route.']}",
    "aggregate": "{'description': ['List of static route definitions']}",
    "mask": "{'description': ['Network prefix mask of the static route.'], 'required': True}",
    "next_hop": "{'description': ['Next hop IP of the static route.'], 'required': True}",
    "prefix": "{'description': ['Network prefix of the static route.'], 'required': True}",
    "purge": "{'description': ['Purge static routes not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the static route configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure static route
  net_static_route:
    prefix: 192.168.2.0
    mask: 255.255.255.0
    next_hop: 10.0.0.1

- name: remove configuration
  net_static_route:
    prefix: 192.168.2.0
    mask: 255.255.255.0
    next_hop: 10.0.0.1
    state: absent

- name: configure aggregates of static routes
  net_static_route:
    aggregate:
      - { prefix: 192.168.2.0, mask 255.255.255.0, next_hop: 10.0.0.1 }
      - { prefix: 192.168.3.0, mask 255.255.255.0, next_hop: 10.0.2.1 }

- name: Remove static route collections
  net_static_route:
    aggregate:
      - { prefix: 172.24.1.0/24, next_hop: 192.168.42.64 }
      - { prefix: 172.24.3.0/24, next_hop: 192.168.42.64 }
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
