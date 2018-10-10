# Ansible module: ansible.module_bcf_switch


Create and remove a bcf switch

## Description

Create and remove a Big Cloud Fabric switch.

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ["Big Cloud Fabric access token. If this isn't set then the environment variable C(BIGSWITCH_ACCESS_TOKEN) is used."]}",
    "controller": "{'description': ['The controller IP address.'], 'required': True}",
    "fabric_role": "{'description': ['Fabric role of the switch.'], 'choices': ['spine', 'leaf'], 'required': True}",
    "leaf_group": "{'description': ['The leaf group of the switch if the switch is a leaf.'], 'required': False}",
    "mac": "{'description': ['The MAC address of the switch.'], 'required': True}",
    "name": "{'description': ['The name of the switch.'], 'required': True}",
    "state": "{'description': ['Whether the switch should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['If C(false), SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: bcf leaf switch
  bcf_switch:
    name: Rack1Leaf1
    fabric_role: leaf
    leaf_group: R1
    mac: 00:00:00:02:00:02
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false

```

## License

TODO

## Author Information
  - ['Ted (@tedelhourani)']
