# Ansible module: ansible.module_parted


Configure block device partitions

## Description

This module allows configuring block device partition using the C(parted) command line tool. For a full description of the fields and the options check the GNU parted manual.

## Requirements

TODO

## Arguments

``` json
{
    "align": "{'description': ['Set alignment for newly created partitions.'], 'choices': ['none', 'cylinder', 'minimal', 'optimal'], 'default': 'optimal'}",
    "device": "{'description': ['The block device (disk) where to operate.'], 'required': True}",
    "flags": "{'description': ['A list of the flags that has to be set on the partition.']}",
    "label": "{'description': ['Creates a new disk label.'], 'choices': ['aix', 'amiga', 'bsd', 'dvh', 'gpt', 'loop', 'mac', 'msdos', 'pc98', 'sun'], 'default': 'msdos'}",
    "name": "{'description': ['Sets the name for the partition number (GPT, Mac, MIPS and PC98 only).']}",
    "number": "{'description': ['The number of the partition to work with or the number of the partition that will be created. Required when performing any action on the disk, except fetching information.']}",
    "part_end": "{'description': ['Where the partition will end as offset from the beginning of the disk, that is, the "distance" from the start of the disk. The distance can be specified with all the units supported by parted (except compat) and it is case sensitive. E.g. C(10GiB), C(15%).'], 'default': '100%'}",
    "part_start": "{'description': ['Where the partition will start as offset from the beginning of the disk, that is, the "distance" from the start of the disk. The distance can be specified with all the units supported by parted (except compat) and it is case sensitive. E.g. C(10GiB), C(15%).'], 'default': '0%'}",
    "part_type": "{'description': ["Is one of 'primary', 'extended' or 'logical' and may be specified only with 'msdos' or 'dvh' partition tables. A name must be specified for a 'gpt' partition table. Neither part-type nor name may be used with a 'sun' partition table."], 'choices': ['primary', 'extended', 'logical'], 'default': 'primary'}",
    "state": "{'description': ['If to create or delete a partition. If set to C(info) the module will only return the device information.'], 'choices': ['present', 'absent', 'info'], 'default': 'info'}",
    "unit": "{'description': ['Selects the current default unit that Parted will use to display locations and capacities on the disk and to interpret those given by the user if they are not suffixed by an unit. When fetching information about a disk, it is always recommended to specify a unit.'], 'choices': ['s', 'B', 'KB', 'KiB', 'MB', 'MiB', 'GB', 'GiB', 'TB', 'TiB', '%', 'cyl', 'chs', 'compact'], 'default': 'KiB'}",
}
```

## Examples


``` yaml

# Create a new primary partition
- parted:
    device: /dev/sdb
    number: 1
    state: present

# Remove partition number 1
- parted:
    device: /dev/sdb
    number: 1
    state: absent

# Create a new primary partition with a size of 1GiB
- parted:
    device: /dev/sdb
    number: 1
    state: present
    part_end: 1GiB

# Create a new primary partition for LVM
- parted:
    device: /dev/sdb
    number: 2
    flags: [ lvm ]
    state: present
    part_start: 1GiB

# Read device information (always use unit when probing)
- parted: device=/dev/sdb unit=MiB
  register: sdb_info

# Remove all partitions from disk
- parted:
    device: /dev/sdb
    number: "{{ item.num }}"
    state: absent
  with_items:
   - "{{ sdb_info.partitions }}"

```

## License

TODO

## Author Information
  - ['Fabrizio Colonna (@ColOfAbRiX)']
