# Ansible module: ansible.module_win_route


Add or remove a static route

## Description

Add or remove a static route.

## Requirements

TODO

## Arguments

``` json
{
    "destination": "{'description': ['Destination IP address in CIDR format (ip address/prefix length)'], 'required': True}",
    "gateway": "{'description': ['The gateway used by the static route.', 'If C(gateway) is not provided it will be set to C(0.0.0.0).']}",
    "metric": "{'description': ['Metric used by the static route.'], 'type': 'int', 'default': 1}",
    "state": "{'description': ['If C(absent), it removes a network static route.', 'If C(present), it adds a network static route.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

---
- name: Add a network static route
  win_route:
    destination: 192.168.2.10/32
    gateway: 192.168.1.1
    metric: 1
    state: present

- name: Remove a network static route
  win_route:
    destination: 192.168.2.10/32
    state: absent

```

## License

TODO

## Author Information
  - ['Daniele Lazzari']
