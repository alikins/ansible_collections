# Ansible module: ansible.module_tempfile


Creates temporary files and directories

## Description

The C(tempfile) module creates temporary files and directories. C(mktemp) command takes different parameters on various systems, this module helps to avoid troubles related to that. Files/directories created by module are accessible only by creator. In case you need to make them world-accessible you need to use M(file) module.
For Windows targets, use the M(win_tempfile) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Location where temporary file or directory should be created. If path is not specified default system temporary directory will be used.']}",
    "prefix": "{'description': ['Prefix of file/directory name created by module.'], 'default': 'ansible.'}",
    "state": "{'description': ['Whether to create file or directory.'], 'choices': ['directory', 'file'], 'default': 'file'}",
    "suffix": "{'description': ['Suffix of file/directory name created by module.'], 'default': ''}",
}
```

## Examples


``` yaml

- name: create temporary build directory
  tempfile:
    state: directory
    suffix: build

- name: create temporary file
  tempfile:
    state: file
    suffix: temp

```

## License

TODO

## Author Information
  - ['Krzysztof Magosa']
