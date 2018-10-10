# Ansible module: ansible.module_win_disk_image


Manage ISO/VHD/VHDX mounts on Windows hosts

## Description

Manages mount behavior for a specified ISO, VHD, or VHDX image on a Windows host. When C(state) is C(present), the image will be mounted under a system-assigned drive letter, which will be returned in the C(mount_path) value of the module result. Requires Windows 8+ or Windows Server 2012+.

## Requirements

TODO

## Arguments

``` json
{
    "image_path": "{'description': ['Path to an ISO, VHD, or VHDX image on the target Windows host (the file cannot reside on a network share)'], 'required': True}",
    "state": "{'description': ['Whether the image should be present as a drive-letter mount or not.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Run installer from mounted ISO, then unmount
- name: Ensure an ISO is mounted
  win_disk_image:
    image_path: C:\install.iso
    state: present
  register: disk_image_out

- name: Run installer from mounted iso
  win_package:
    path: '{{ disk_image_out.mount_paths[0] }}setup\setup.exe'
    product_id: 35a4e767-0161-46b0-979f-e61f282fee21
    state: present

- name: Unmount iso
  win_disk_image:
    image_path: C:\install.iso
    state: absent

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
