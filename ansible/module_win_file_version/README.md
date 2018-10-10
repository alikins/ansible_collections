# Ansible module: ansible.module_win_file_version


Get DLL or EXE file build version

## Description

Get DLL or EXE file build version.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['File to get version.', 'Always provide absolute path.'], 'required': True, 'type': 'path'}",
}
```

## Examples


``` yaml

- name: Get acm instance version
  win_file_version:
    path: C:\Windows\System32\cmd.exe
  register: exe_file_version

- debug:
    msg: '{{ exe_file_version }}'

```

## License

TODO

## Author Information
  - ['Sam Liu (@SamLiu79)']
