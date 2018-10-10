# Ansible module: ansible.module_win_reg_stat


Get information about Windows registry keys

## Description

Like M(win_file), M(win_reg_stat) will return whether the key/property exists.
It also returns the sub keys and properties of the key specified.
If specifying a property name through I(property), it will return the information specific for that property.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The registry property name to get information for, the return json will not include the sub_keys and properties entries for the I(key) specified.'], 'aliases': ['entry', 'value', 'property']}",
    "path": "{'description': ['The full registry key path including the hive to search for.'], 'required': True, 'aliases': ['key']}",
}
```

## Examples


``` yaml

- name: Obtain information about a registry key using short form
  win_reg_stat:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
  register: current_version

- name: Obtain information about a registry key property
  win_reg_stat:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
    name: CommonFilesDir
  register: common_files_dir

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
