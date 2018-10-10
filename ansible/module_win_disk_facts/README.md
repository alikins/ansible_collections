# Ansible module: ansible.module_win_disk_facts


Show the attached disks and disk information of the target host

## Description

With the module you can retrieve and output detailed information about the attached disks of the target and its volumes and partitions if existent.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: Get disk facts
  win_disk_facts:

- name: Output first disk size
  debug:
    var: ansible_facts.disks[0].size

- name: Convert first system disk into various formats
  debug:
    msg: '{{ disksize_gib }} vs {{ disksize_gib_human }}'
  vars:
    # Get first system disk
    disk: '{{ ansible_facts.disks|selectattr("system_disk")|first }}'

    # Show disk size in Gibibytes
    disksize_gib_human: '{{ disk.size|filesizeformat(True) }}'   # returns "223.6 GiB" (human readable)
    disksize_gib: '{{ (disk.size/1024|pow(3))|round|int }} GiB'  # returns "224 GiB" (value in GiB)

    # Show disk size in Gigabytes
    disksize_gb_human: '{{ disk.size|filesizeformat }}'        # returns "240.1 GB" (human readable)
    disksize_gb: '{{ (disk.size/1000|pow(3))|round|int }} GB'  # returns "240 GB" (value in GB)

- name: Output second disk serial number
  debug:
    var: ansible_facts.disks[0].serial_number

```

## License

TODO

## Author Information
  - ['Marc Tschapek (@marqelme)']
