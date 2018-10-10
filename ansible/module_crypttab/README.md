# Ansible module: ansible.module_crypttab


Encrypted Linux block devices

## Description

Control Linux encrypted block devices that are set up during system boot in C(/etc/crypttab).

## Requirements

TODO

## Arguments

``` json
{
    "backing_device": "{'description': ['Path to the underlying block device or file, or the UUID of a block-device prefixed with I(UUID=).']}",
    "name": "{'description': ['Name of the encrypted block device as it appears in the C(/etc/crypttab) file, or optionally prefixed with C(/dev/mapper/), as it appears in the filesystem. I(/dev/mapper/) will be stripped from I(name).'], 'required': True}",
    "opts": "{'description': ['A comma-delimited list of options. See C(crypttab(5) ) for details.']}",
    "password": "{'description': ['Encryption password, the path to a file containing the password, or C(none) or C(-) if the password should be entered at boot.'], 'default': 'none'}",
    "path": "{'description': ['Path to file to use instead of C(/etc/crypttab). This might be useful in a chroot environment.'], 'default': '/etc/crypttab'}",
    "state": "{'description': ["Use I(present) to add a line to C(/etc/crypttab) or update it's definition if already present. Use I(absent) to remove a line with matching I(name). Use I(opts_present) to add options to those already present; options with different values will be updated. Use I(opts_absent) to remove options from the existing set."], 'required': True, 'choices': ['absent', 'opts_absent', 'opts_present', 'present']}",
}
```

## Examples


``` yaml

- name: Set the options explicitly a device which must already exist
  crypttab:
    name: luks-home
    state: present
    opts: discard,cipher=aes-cbc-essiv:sha256

- name: Add the 'discard' option to any existing options for all devices
  crypttab:
    name: '{{ item.device }}'
    state: opts_present
    opts: discard
  with_items: '{{ ansible_mounts }}'
  when: "'/dev/mapper/luks-' in {{ item.device }}"

```

## License

TODO

## Author Information
  - ['Steve (@groks)']
