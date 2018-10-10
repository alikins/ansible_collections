# Ansible module: ansible.module_win_hotfix


Install and uninstalls Windows hotfixes

## Description

Install, uninstall a Windows hotfix.

## Requirements

TODO

## Arguments

``` json
{
    "hotfix_identifier": "{'description': ['The name of the hotfix as shown in DISM, see examples for details.', 'This or C(hotfix_kb) MUST be set when C(state=absent).', 'If C(state=present) then the hotfix at C(source) will be validated against this value, if it does not match an error will occur.', "You can get the identifier by running 'Get-WindowsPackage -Online -PackagePath path-to-cab-in-msu' after expanding the msu file."]}",
    "hotfix_kb": "{'description': ['The name of the KB the hotfix relates to, see examples for details.', 'This of C(hotfix_identifier) MUST be set when C(state=absent).', 'If C(state=present) then the hotfix at C(source) will be validated against this value, if it does not match an error will occur.', "Because DISM uses the identifier as a key and doesn't refer to a KB in all cases it is recommended to use C(hotfix_identifier) instead."]}",
    "source": "{'description': ['The path to the downloaded hotfix .msu file.', 'This MUST be set if C(state=present) and MUST be a .msu hotfix file.'], 'type': 'path'}",
    "state": "{'description': ['Whether to install or uninstall the hotfix.', 'When C(present), C(source) MUST be set.', 'When C(absent), C(hotfix_identifier) or C(hotfix_kb) MUST be set.'], 'default': 'present', 'choices': ['absent', 'present']}",
}
```

## Examples


``` yaml

- name: install Windows ADK with DISM for Server 2008 R2
  win_chocolatey:
    name: windows-adk
    version: 8.100.26866.0
    state: present
    install_args: /features OptionId.DeploymentTools

- name: install hotfix without validating the KB and Identifier
  win_hotfix:
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- win_reboot:
  when: hotfix_install.reboot_required

- name: install hotfix validating KB
  win_hotfix:
    hotfix_kb: KB3172729
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- win_reboot:
  when: hotfix_install.reboot_required

- name: install hotfix validating Identifier
  win_hotfix:
    hotfix_identifier: Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- win_reboot:
  when: hotfix_install.reboot_required

- name: uninstall hotfix with Identifier
  win_hotfix:
    hotfix_identifier: Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0
    state: absent
  register: hotfix_uninstall

- win_reboot:
  when: hotfix_uninstall.reboot_required

- name: uninstall hotfix with KB (not recommended)
  win_hotfix:
    hotfix_kb: KB3172729
    state: absent
  register: hotfix_uninstall

- win_reboot:
  when: hotfix_uninstall.reboot_required

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
