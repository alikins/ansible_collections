# Ansible module: ansible.module_dladm_vlan


Manage VLAN interfaces on Solaris/illumos systems

## Description

Create or delete VLAN interfaces on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "link": "{'description': ['VLAN underlying link name.'], 'required': True}",
    "name": "{'description': ['VLAN interface name.'], 'required': True}",
    "state": "{'description': ['Create or delete Solaris/illumos VNIC.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "temporary": "{'description': ['Specifies that the VLAN interface is temporary. Temporary VLANs do not persist across reboots.'], 'required': False, 'default': False}",
    "vlan_id": "{'description': ['VLAN ID value for VLAN interface.'], 'required': False, 'default': False, 'aliases': ['vid']}",
}
```

## Examples


``` yaml

- name: Create 'vlan42' VLAN over 'bnx0' link
  dladm_vlan: name=vlan42 link=bnx0 vlan_id=42 state=present

- name: Remove 'vlan1337' VLAN interface
  dladm_vlan: name=vlan1337 state=absent

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
