# Ansible module: ansible.module_lvg


Configure LVM volume groups

## Description

This module creates, removes or resizes volume groups.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['If C(yes), allows to remove volume group with logical volumes.'], 'type': 'bool', 'default': False}",
    "pesize": "{'description': ['The size of the physical extent. pesize must be a power of 2, or multiple of 128KiB. Since version 2.6, pesize can be optionally suffixed by a UNIT (k/K/m/M/g/G), default unit is megabyte.'], 'default': 4}",
    "pv_options": "{'description': ['Additional options to pass to C(pvcreate) when creating the volume group.'], 'version_added': '2.4'}",
    "pvs": "{'description': ['List of comma-separated devices to use as physical devices in this volume group. Required when creating or resizing volume group.', 'The module will take care of running pvcreate if needed.']}",
    "state": "{'description': ['Control if the volume group exists.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "vg": "{'description': ['The name of the volume group.'], 'required': True}",
    "vg_options": "{'description': ['Additional options to pass to C(vgcreate) when creating the volume group.'], 'version_added': '1.6'}",
}
```

## Examples


``` yaml

- name: Create a volume group on top of /dev/sda1 with physical extent size = 32MB
  lvg:
    vg: vg.services
    pvs: /dev/sda1
    pesize: 32

- name: Create a volume group on top of /dev/sdb with physical extent size = 128KiB
  lvg:
    vg: vg.services
    pvs: /dev/sdb
    pesize: 128K

# If, for example, we already have VG vg.services on top of /dev/sdb1,
# this VG will be extended by /dev/sdc5.  Or if vg.services was created on
# top of /dev/sda5, we first extend it with /dev/sdb1 and /dev/sdc5,
# and then reduce by /dev/sda5.
- name: Create or resize a volume group on top of /dev/sdb1 and /dev/sdc5.
  lvg:
    vg: vg.services
    pvs: /dev/sdb1,/dev/sdc5

- name: Remove a volume group with name vg.services
  lvg:
    vg: vg.services
    state: absent

```

## License

TODO

## Author Information
  - ['Alexander Bulimov (@abulimov)']
