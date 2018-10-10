# Ansible module: ansible.module_win_file


Creates, touches or removes files or directories

## Description

Creates (empty) files, updates file modification stamps of existing files, and can create or remove directories.
Unlike M(file), does not modify ownership, permissions or manipulate links.
For non-Windows targets, use the M(file) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Path to the file being managed.'], 'required': True, 'type': 'path', 'aliases': ['dest', 'name']}",
    "state": "{'description': ['If C(directory), all immediate subdirectories will be created if they do not exist.', 'If C(file), the file will NOT be created if it does not exist, see the M(copy) or M(template) module if you want that behavior.  If C(absent), directories will be recursively deleted, and files will be removed.', 'If C(touch), an empty file will be created if the C(path) does not exist, while an existing file or directory will receive updated file access and modification times (similar to the way C(touch) works from the command line).'], 'choices': ['absent', 'directory', 'file', 'touch']}",
}
```

## Examples


``` yaml

- name: Touch a file (creates if not present, updates modification time if present)
  win_file:
    path: C:\Temp\foo.conf
    state: touch

- name: Remove a file, if present
  win_file:
    path: C:\Temp\foo.conf
    state: absent

- name: Create directory structure
  win_file:
    path: C:\Temp\folder\subfolder
    state: directory

- name: Remove directory structure
  win_file:
    path: C:\Temp
    state: absent

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
