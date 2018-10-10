# Ansible module: ansible.module_net_ping


Tests reachability using ping from a network device

## Description

Tests reachability using ping from network device to a remote destination.
For Windows targets, use the M(win_ping) module instead.
For targets running Python, use the M(ping) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "count": "{'description': ['Number of packets to send.'], 'default': 5}",
    "dest": "{'description': ['The IP Address or hostname (resolvable by switch) of the remote node.'], 'required': True}",
    "source": "{'description': ['The source IP Address.']}",
    "state": "{'description': ['Determines if the expected result is success or fail.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "vrf": "{'description': ['The VRF to use for forwarding.'], 'default': 'default'}",
}
```

## Examples


``` yaml

- name: Test reachability to 10.10.10.10 using default vrf
  net_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using prod vrf
  net_ping:
    dest: 10.20.20.20
    vrf: prod

- name: Test unreachability to 10.30.30.30 using default vrf
  net_ping:
    dest: 10.30.30.30
    state: absent

- name: Test reachability to 10.40.40.40 using prod vrf and setting count and source
  net_ping:
    dest: 10.40.40.40
    source: loopback0
    vrf: prod
    count: 20

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
