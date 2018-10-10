# Ansible module: ansible.module_win_pester


Run Pester tests on Windows hosts

## Description

Run Pester tests on Windows hosts.
Test files have to be available on the remote host.

## Requirements

TODO

## Arguments

``` json
{
    "path": "{'description': ['Path to a pester test file or a folder where tests can be found.', 'If the path is a folder, the module will consider all ps1 files as Pester tests.'], 'required': True}",
    "version": "{'description': ['Minimum version of the pester module that has to be available on the remote host.']}",
}
```

## Examples


``` yaml

- name: Get facts
  setup:

- name: Add Pester module
  action:
    module_name: "{{ 'win_psmodule' if ansible_powershell_version >= 5 else 'win_chocolatey' }}"
    name: Pester
    state: present

- name: Run the pester test provided in the path parameter.
  win_pester:
    path: C:\Pester

# Run pesters tests files that are present in the specified folder
# ensure that the pester module version available is greater or equal to the version parameter.
- name: Run the pester test present in a folder and check the Pester module version.
  win_pester:
    path: C:\Pester\test01.test.ps1
    version: 4.1.0

```

## License

TODO

## Author Information
  - ['Erwan Quelin (@equelin)']
