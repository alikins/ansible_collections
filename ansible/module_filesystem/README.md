# Ansible module: ansible.module_filesystem


Makes a filesystem

## Description

This module creates a filesystem.

## Requirements

TODO

## Arguments

``` json
{
    "dev": "{'description': ['Target path to device or image file.'], 'required': True, 'aliases': ['device']}",
    "force": "{'description': ['If C(yes), allows to create new filesystem on devices that already has filesystem.'], 'type': 'bool', 'default': False}",
    "fstype": "{'choices': ['btrfs', 'ext2', 'ext3', 'ext4', 'ext4dev', 'f2fs', 'lvm', 'ocfs2', 'reiserfs', 'xfs', 'vfat'], 'description': ['Filesystem type to be created.', 'reiserfs support was added in 2.2.', 'lvm support was added in 2.5.', 'since 2.5, I(dev) can be an image file.', 'vfat support was added in 2.5', 'ocfs2 support was added in 2.6', 'f2fs support was added in 2.7'], 'required': True, 'aliases': ['type']}",
    "opts": "{'description': ['List of options to be passed to mkfs command.']}",
    "resizefs": "{'description': ['If C(yes), if the block device and filesytem size differ, grow the filesystem into the space.', 'Supported for C(ext2), C(ext3), C(ext4), C(ext4dev), C(f2fs), C(lvm), C(xfs) and C(vfat) filesystems.', 'XFS Will only grow if mounted.', 'vFAT will likely fail if fatresize < 1.04.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Create a ext2 filesystem on /dev/sdb1
  filesystem:
    fstype: ext2
    dev: /dev/sdb1

- name: Create a ext4 filesystem on /dev/sdb1 and check disk blocks
  filesystem:
    fstype: ext4
    dev: /dev/sdb1
    opts: -cc

```

## License

TODO

## Author Information
  - ['Alexander Bulimov (@abulimov)']
