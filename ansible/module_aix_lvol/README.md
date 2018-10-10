# Ansible module: ansible.module_aix_lvol


Configure AIX LVM logical volumes

## Description

This module creates, removes or resizes AIX logical volumes. Inspired by lvol module.

## Requirements

TODO

## Arguments

``` json
{
    "copies": "{'description': ['The number of copies of the logical volume. Maximum copies are 3.'], 'default': '1'}",
    "lv": "{'description': ['The name of the logical volume.'], 'required': True}",
    "lv_type": "{'description': ['The type of the logical volume.'], 'default': 'jfs2'}",
    "opts": "{'description': ['Free-form options to be passed to the mklv command.']}",
    "policy": "{'choices': ['maximum', 'minimum'], 'default': 'maximum', 'description': ['Sets the interphysical volume allocation policy. C(maximum) allocates logical partitions across the maximum number of physical volumes. C(minimum) allocates logical partitions across the minimum number of physical volumes.']}",
    "pvs": "{'description': ['Comma separated list of physical volumes e.g. C(hdisk1,hdisk2).']}",
    "size": "{'description': ['The size of the logical volume with one of the [MGT] units.']}",
    "state": "{'choices': ['absent', 'present'], 'default': 'present', 'description': ['Control if the logical volume exists. If C(present) and the volume does not already exist then the C(size) option is required.']}",
    "vg": "{'description': ['The volume group this logical volume is part of.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a logical volume of 512M
  aix_lvol:
    vg: testvg
    lv: testlv
    size: 512M

- name: Create a logical volume of 512M with disks hdisk1 and hdisk2
  aix_lvol:
    vg: testvg
    lv: test2lv
    size: 512M
    pvs: hdisk1,hdisk2

- name: Create a logical volume of 512M mirrored
  aix_lvol:
    vg: testvg
    lv: test3lv
    size: 512M
    copies: 2

- name: Create a logical volume of 1G with a minimum placement policy
  aix_lvol:
    vg: rootvg
    lv: test4lv
    size: 1G
    policy: minimum

- name: Create a logical volume with special options like mirror pool
  aix_lvol:
    vg: testvg
    lv: testlv
    size: 512M
    opts: -p copy1=poolA -p copy2=poolB

- name: Extend the logical volume to 1200M
  aix_lvol:
    vg: testvg
    lv: test4lv
    size: 1200M

- name: Remove the logical volume
  aix_lvol:
    vg: testvg
    lv: testlv
    state: absent

```

## License

TODO

## Author Information
  - ['Alain Dejoux (@adejoux)']
