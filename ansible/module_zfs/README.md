# Ansible module: ansible.module_zfs


Manage zfs

## Description

Manages ZFS file systems, volumes, clones and snapshots

## Requirements

TODO

## Arguments

``` json
{
    "extra_zfs_properties": "{'description': ['A dictionary of zfs properties to be set.', 'See the zfs(8) man page for more information.'], 'version_added': '2.5'}",
    "key_value": "{'description': ['(**DEPRECATED**) This will be removed in Ansible-2.9.  Set these values in the', 'C(extra_zfs_properties) option instead.', 'The C(zfs) module takes key=value pairs for zfs properties to be set.', 'See the zfs(8) man page for more information.']}",
    "name": "{'description': ['File system, snapshot or volume name e.g. C(rpool/myfs).'], 'required': True}",
    "origin": "{'description': ['Snapshot from which to create a clone.']}",
    "state": "{'description': ['Whether to create (C(present)), or remove (C(absent)) a file system, snapshot or volume. All parents/children will be created/destroyed as needed to reach the desired state.'], 'choices': ['absent', 'present'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a new file system called myfs in pool rpool with the setuid property turned off
  zfs:
    name: rpool/myfs
    state: present
    extra_zfs_properties:
      setuid: off

- name: Create a new volume called myvol in pool rpool.
  zfs:
    name: rpool/myvol
    state: present
    extra_zfs_properties:
      volsize: 10M

- name: Create a snapshot of rpool/myfs file system.
  zfs:
    name: rpool/myfs@mysnapshot
    state: present

- name: Create a new file system called myfs2 with snapdir enabled
  zfs:
    name: rpool/myfs2
    state: present
    extra_zfs_properties:
      snapdir: enabled

- name: Create a new file system by cloning a snapshot
  zfs:
    name: rpool/cloned_fs
    state: present
    origin: rpool/myfs@mysnapshot

- name: Destroy a filesystem
  zfs:
    name: rpool/myfs
    state: absent

```

## License

TODO

## Author Information
  - ['Johan Wiren (@johanwiren)']
