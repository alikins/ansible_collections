# Ansible module: ansible.module_win_feature


Installs and uninstalls Windows Features on Windows Server

## Description

Installs or uninstalls Windows Roles or Features on Windows Server. This module uses the Add/Remove-WindowsFeature Cmdlets on Windows 2008 R2 and Install/Uninstall-WindowsFeature Cmdlets on Windows 2012, which are not available on client os machines.

## Requirements

TODO

## Arguments

``` json
{
    "include_management_tools": "{'description': ['Adds the corresponding management tools to the specified feature.', 'Not supported in Windows 2008 R2 and will be ignored.'], 'type': 'bool', 'default': False}",
    "include_sub_features": "{'description': ['Adds all subfeatures of the specified feature.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Names of roles or features to install as a single feature or a comma-separated list of features.'], 'required': True, 'type': 'list'}",
    "source": "{'description': ['Specify a source to install the feature from.', 'Not supported in Windows 2008 R2 and will be ignored.', 'Can either be C({driveletter}:\\sources\\sxs) or C(\\\\{IP}\\share\\sources\\sxs).'], 'version_added': '2.1'}",
    "state": "{'description': ['State of the features or roles on the system.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Install IIS (Web-Server only)
  win_feature:
    name: Web-Server
    state: present

- name: Install IIS (Web-Server and Web-Common-Http)
  win_feature:
    name:
    - Web-Server
    - Web-Common-Http
    state: present

- name: Install NET-Framework-Core from file
  win_feature:
    name: NET-Framework-Core
    source: C:\Temp\iso\sources\sxs
    state: present

- name: Install IIS Web-Server with sub features and management tools
  win_feature:
    name: Web-Server
    state: present
    include_sub_features: yes
    include_management_tools: yes
  register: win_feature

- name: reboot if installing Web-Server feature requires it
  win_reboot:
  when: win_feature.reboot_required

```

## License

TODO

## Author Information
  - ['Paul Durivage (@angstwad)', 'Trond Hindenes (@trondhindenes)']
  - ['Paul Durivage (@angstwad)', 'Trond Hindenes (@trondhindenes)']
