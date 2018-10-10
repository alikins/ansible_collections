# Ansible module: ansible.module_win_tempfile


Creates temporary files and directories

## Description

Creates temporary files and directories.
For non-Windows targets, please use the M(tempfile) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Location where temporary file or directory should be created.', 'If path is not specified default system temporary directory (%TEMP%) will be used.'], 'type': 'path', 'default': '%TEMP%'}",
    "prefix": "{'description': ['Prefix of file/directory name created by module.'], 'default': 'ansible.'}",
    "state": "{'description': ['Whether to create file or directory.'], 'choices': ['directory', 'file'], 'default': 'file'}",
    "suffix": "{'description': ['Suffix of file/directory name created by module.'], 'default': ''}",
}
```

## Examples


``` yaml

- name: Create temporary build directory
  win_tempfile:
    state: directory
    suffix: build

- name: Create temporary file
  win_tempfile:
    state: file
    suffix: temp

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
