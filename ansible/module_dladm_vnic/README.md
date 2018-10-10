# Ansible module: ansible.module_dladm_vnic


Manage VNICs on Solaris/illumos systems

## Description

Create or delete VNICs on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "link": "{'description': ['VNIC underlying link name.'], 'required': True}",
    "mac": "{'description': ["Sets the VNIC's MAC address. Must be valid unicast MAC address."], 'required': False, 'default': False, 'aliases': ['macaddr']}",
    "name": "{'description': ['VNIC name.'], 'required': True}",
    "state": "{'description': ['Create or delete Solaris/illumos VNIC.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "temporary": "{'description': ['Specifies that the VNIC is temporary. Temporary VNICs do not persist across reboots.'], 'required': False, 'default': False, 'type': 'bool'}",
    "vlan": "{'description': ['Enable VLAN tagging for this VNIC. The VLAN tag will have id I(vlan).'], 'required': False, 'default': False, 'aliases': ['vlan_id']}",
}
```

## Examples


``` yaml

# Create 'vnic0' VNIC over 'bnx0' link
- dladm_vnic:
    name: vnic0
    link: bnx0
    state: present

# Create VNIC with specified MAC and VLAN tag over 'aggr0'
- dladm_vnic:
    name: vnic1
    link: aggr0
    mac: '00:00:5E:00:53:23'
    vlan: 4

# Remove 'vnic0' VNIC
- dladm_vnic:
    name: vnic0
    link: bnx0
    state: absent

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
