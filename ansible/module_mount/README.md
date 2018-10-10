# Ansible module: ansible.module_mount


Control active and configured mount points

## Description

This module controls active and configured mount points in C(/etc/fstab).

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'required': False, 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "boot": "{'description': ['Determines if the filesystem should be mounted on boot.', 'Only applies to Solaris systems.'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "dump": "{'description': ['Dump (see fstab(5)). Note that if set to C(null) and I(state) set to C(present), it will cease to work and duplicate entries will be made with subsequent runs.', 'Has no effect on Solaris systems.'], 'default': 0}",
    "fstab": "{'description': ["File to use instead of C(/etc/fstab). You shouldn't use this option unless you really know what you are doing. This might be useful if you need to configure mountpoints in a chroot environment.  OpenBSD does not allow specifying alternate fstab files with mount so do not use this on OpenBSD with any state that operates on the live filesystem."], 'default': '/etc/fstab (/etc/vfstab on Solaris)'}",
    "fstype": "{'description': ['Filesystem type. Required when I(state) is C(present) or C(mounted).']}",
    "opts": "{'description': ['Mount options (see fstab(5), or vfstab(4) on Solaris).']}",
    "passno": "{'description': ['Passno (see fstab(5)). Note that if set to C(null) and I(state) set to C(present), it will cease to work and duplicate entries will be made with subsequent runs.', 'Deprecated on Solaris systems.'], 'default': 0}",
    "path": "{'description': ['Path to the mount point (e.g. C(/mnt/files)).', 'Before 2.3 this option was only usable as I(dest), I(destfile) and I(name).'], 'required': True, 'aliases': ['name']}",
    "src": "{'description': ['Device to be mounted on I(path). Required when I(state) set to C(present) or C(mounted).']}",
    "state": "{'description': ['If C(mounted), the device will be actively mounted and appropriately configured in I(fstab). If the mount point is not present, the mount point will be created.', 'If C(unmounted), the device will be unmounted without changing I(fstab).', 'C(present) only specifies that the device is to be configured in I(fstab) and does not trigger or require a mount.', "C(absent) specifies that the device mount's entry will be removed from I(fstab) and will also unmount the device and remove the mount point."], 'required': True, 'choices': ['absent', 'mounted', 'present', 'unmounted']}",
}
```

## Examples


``` yaml

# Before 2.3, option 'name' was used instead of 'path'
- name: Mount DVD read-only
  mount:
    path: /mnt/dvd
    src: /dev/sr0
    fstype: iso9660
    opts: ro,noauto
    state: present

- name: Mount up device by label
  mount:
    path: /srv/disk
    src: LABEL=SOME_LABEL
    fstype: ext4
    state: present

- name: Mount up device by UUID
  mount:
    path: /home
    src: UUID=b3e48f45-f933-4c8e-a700-22a159ec9077
    fstype: xfs
    opts: noatime
    state: present

- name: Unmount a mounted volume
  mount:
    path: /tmp/mnt-pnt
    state: unmounted

- name: Mount and bind a volume
  mount:
    path: /system/new_volume/boot
    src: /boot
    opts: bind
    state: mounted
    fstype: none

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Seth Vidal']
  - ['Ansible Core Team', 'Seth Vidal']
