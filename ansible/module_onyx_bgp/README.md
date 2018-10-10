# Ansible module: ansible.module_onyx_bgp


Configures BGP on Mellanox ONYX network devices

## Description

This module provides declarative management of BGP router and neighbors on Mellanox ONYX network devices.

## Requirements

TODO

## Arguments

``` json
{
    "as_number": "{'description': ['Local AS number.'], 'required': True}",
    "neighbors": "{'description': ['List of neighbors. Required if I(state=present).'], 'suboptions': {'remote_as': {'description': ['Remote AS number.'], 'required': True}, 'neighbor': {'description': ['Neighbor IP address.'], 'required': True}}}",
    "networks": "{'description': ['List of advertised networks.']}",
    "router_id": "{'description': ['Router IP address. Required if I(state=present).']}",
    "state": "{'description': ['BGP state.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure bgp
  onyx_bgp:
    as_number: 320
    router_id: 10.3.3.3
    neighbors:
      - remote_as: 321
        neighbor: 10.3.3.4
    state: present
    networks:
      - 172.16.1.0/24

```

## License

TODO

## Author Information
  - ['Samer Deeb (@samerd)']
