# Ansible module: ansible.module_net_vrf


Manage VRFs on network devices

## Description

This module provides declarative management of VRFs on network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of VRFs definitions']}",
    "interfaces": "{'description': ['List of interfaces the VRF should be configured on.']}",
    "name": "{'description': ['Name of the VRF.']}",
    "purge": "{'description': ['Purge VRFs not defined in the I(aggregate) parameter.'], 'default': False}",
    "state": "{'description': ['State of the VRF configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Create VRF named MANAGEMENT
  net_vrf:
    name: MANAGEMENT

- name: remove VRF named MANAGEMENT
  net_vrf:
    name: MANAGEMENT
    state: absent

- name: Create aggregate of VRFs with purge
  net_vrf:
    aggregate:
      - { name: test4, rd: "1:204" }
      - { name: test5, rd: "1:205" }
    state: present
    purge: yes

- name: Delete aggregate of VRFs
  net_vrf:
    aggregate:
      - name: test2
      - name: test3
      - name: test4
      - name: test5
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
