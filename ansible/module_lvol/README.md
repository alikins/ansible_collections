# Ansible module: ansible.module_lvol


Configure LVM logical volumes

## Description

This module creates, removes or resizes logical volumes.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Whether the volume is activate and visible to the host.'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "force": "{'description': ['Shrink or remove operations of volumes requires this switch. Ensures that that filesystems get never corrupted/destroyed by mistake.'], 'type': 'bool', 'default': False, 'version_added': '1.5'}",
    "lv": "{'description': ['The name of the logical volume.']}",
    "opts": "{'description': ['Free-form options to be passed to the lvcreate command.'], 'version_added': '2.0'}",
    "pvs": "{'description': ['Comma separated list of physical volumes (e.g. /dev/sda,/dev/sdb).'], 'version_added': '2.2'}",
    "resizefs": "{'description': ['Resize the underlying filesystem together with the logical volume.'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "shrink": "{'description': ['Shrink if current size is higher than size requested.'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "size": "{'description': ['The size of the logical volume, according to lvcreate(8) --size, by default in megabytes or optionally with one of [bBsSkKmMgGtTpPeE] units; or according to lvcreate(8) --extents as a percentage of [VG|PVS|FREE]; Float values must begin with a digit. Resizing using percentage values was not supported prior to 2.1.']}",
    "snapshot": "{'description': ['The name of the snapshot volume'], 'version_added': '2.1'}",
    "state": "{'description': ['Control if the logical volume exists. If C(present) and the volume does not already exist then the C(size) option is required.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "thinpool": "{'description': ['The thin pool volume name. When you want to create a thin provisioned volume, specify a thin pool volume name.'], 'version_added': '2.5'}",
    "vg": "{'description': ['The volume group this logical volume is part of.']}",
}
```

## Examples


``` yaml

- name: Create a logical volume of 512m
  lvol:
    vg: firefly
    lv: test
    size: 512

- name: Create a logical volume of 512m with disks /dev/sda and /dev/sdb
  lvol:
    vg: firefly
    lv: test
    size: 512
    pvs: /dev/sda,/dev/sdb

- name: Create cache pool logical volume
  lvol:
    vg: firefly
    lv: lvcache
    size: 512m
    opts: --type cache-pool

- name: Create a logical volume of 512g.
  lvol:
    vg: firefly
    lv: test
    size: 512g

- name: Create a logical volume the size of all remaining space in the volume group
  lvol:
    vg: firefly
    lv: test
    size: 100%FREE

- name: Create a logical volume with special options
  lvol:
    vg: firefly
    lv: test
    size: 512g
    opts: -r 16

- name: Extend the logical volume to 1024m.
  lvol:
    vg: firefly
    lv: test
    size: 1024

- name: Extend the logical volume to consume all remaining space in the volume group
  lvol:
    vg: firefly
    lv: test
    size: +100%FREE

- name: Extend the logical volume to take all remaining space of the PVs and resize the underlying filesystem
  lvol:
    vg: firefly
    lv: test
    size: 100%PVS
    resizefs: true

- name: Resize the logical volume to % of VG
  lvol:
    vg: firefly
    lv: test
    size: 80%VG
    force: yes

- name: Reduce the logical volume to 512m
  lvol:
    vg: firefly
    lv: test
    size: 512
    force: yes

- name: Set the logical volume to 512m and do not try to shrink if size is lower than current one
  lvol:
    vg: firefly
    lv: test
    size: 512
    shrink: no

- name: Remove the logical volume.
  lvol:
    vg: firefly
    lv: test
    state: absent
    force: yes

- name: Create a snapshot volume of the test logical volume.
  lvol:
    vg: firefly
    lv: test
    snapshot: snap1
    size: 100m

- name: Deactivate a logical volume
  lvol:
    vg: firefly
    lv: test
    active: false

- name: Create a deactivated logical volume
  lvol:
    vg: firefly
    lv: test
    size: 512g
    active: false

- name: Create a thin pool of 512g
  lvol:
    vg: firefly
    thinpool: testpool
    size: 512g

- name: Create a thin volume of 128g
  lvol:
    vg: firefly
    lv: test
    thinpool: testpool
    size: 128g

```

## License

TODO

## Author Information
  - ['Jeroen Hoekx (@jhoekx)', 'Alexander Bulimov (@abulimov)']
  - ['Jeroen Hoekx (@jhoekx)', 'Alexander Bulimov (@abulimov)']
