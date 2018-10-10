# Ansible module: ansible.module_iso_extract


Extract files from an ISO image

## Description

This module has two possible ways of operation.
If 7zip is installed on the system, this module extracts files from an ISO into a temporary directory and copies files to a given destination, if needed.
If the user has mount-capabilities (CAP_SYS_ADMIN on Linux) this module mounts the ISO image to a temporary location, and copies files to a given destination, if needed.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['The destination directory to extract files to.'], 'required': True}",
    "executable": "{'description': ['The path to the C(7z) executable to use for extracting files from the ISO.'], 'default': '7z', 'version_added': '2.4'}",
    "files": "{'description': ['A list of files to extract from the image.', 'Extracting directories does not work.'], 'required': True}",
    "force": "{'description': ['If C(yes), which will replace the remote file when contents are different than the source.', 'If C(no), the file will only be extracted and copied if the destination does not already exist.'], 'type': 'bool', 'default': True, 'aliases': ['thirsty'], 'version_added': '2.4'}",
    "image": "{'description': ['The ISO image to extract files from.'], 'required': True, 'aliases': ['path', 'src']}",
}
```

## Examples


``` yaml

- name: Extract kernel and ramdisk from a LiveCD
  iso_extract:
    image: /tmp/rear-test.iso
    dest: /tmp/virt-rear/
    files:
    - isolinux/kernel
    - isolinux/initrd.cgz

```

## License

TODO

## Author Information
  - ['Jeroen Hoekx (@jhoekx)', 'Matt Robinson (@ribbons)', 'Dag Wieers (@dagwieers)']
  - ['Jeroen Hoekx (@jhoekx)', 'Matt Robinson (@ribbons)', 'Dag Wieers (@dagwieers)']
  - ['Jeroen Hoekx (@jhoekx)', 'Matt Robinson (@ribbons)', 'Dag Wieers (@dagwieers)']
