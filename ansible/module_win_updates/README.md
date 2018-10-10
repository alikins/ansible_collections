# Ansible module: ansible.module_win_updates


Download and install Windows updates

## Description

Searches, downloads, and installs Windows updates synchronously by automating the Windows Update client.

## Requirements

TODO

## Arguments

``` json
{
    "blacklist": "{'description': ['A list of update titles or KB numbers that can be used to specify which updates are to be excluded from installation.', 'If an available update does match one of the entries, then it is skipped and not installed.', 'Each entry can either be the KB article or Update title as a regex according to the PowerShell regex rules.'], 'type': 'list', 'version_added': '2.5'}",
    "category_names": "{'description': ['A scalar or list of categories to install updates from'], 'type': 'list', 'default': ['CriticalUpdates', 'SecurityUpdates', 'UpdateRollups'], 'choices': ['Application', 'Connectors', 'CriticalUpdates', 'DefinitionUpdates', 'DeveloperKits', 'FeaturePacks', 'Guidance', 'SecurityUpdates', 'ServicePacks', 'Tools', 'UpdateRollups', 'Updates']}",
    "log_path": "{'description': ['If set, C(win_updates) will append update progress to the specified file. The directory must already exist.'], 'type': 'path'}",
    "reboot": "{'description': ['Ansible will automatically reboot the remote host if it is required and continue to install updates after the reboot.', 'This can be used instead of using a M(win_reboot) task after this one and ensures all updates for that category is installed in one go.', 'Async does not work when C(reboot=True).'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "reboot_timeout": "{'description': ['The time in seconds to wait until the host is back online from a reboot.', 'This is only used if C(reboot=True) and a reboot is required.'], 'default': 1200, 'version_added': '2.5'}",
    "state": "{'description': ['Controls whether found updates are returned as a list or actually installed.', 'This module also supports Ansible check mode, which has the same effect as setting state=searched'], 'choices': ['installed', 'searched'], 'default': 'installed'}",
    "use_scheduled_task": "{'description': ['Will not auto elevate the remote process with I(become) and use a scheduled task instead.', 'Set this to C(yes) when using this module with async on Server 2008, 2008 R2, or Windows 7, or on Server 2008 that is not authenticated with basic or credssp.', 'Can also be set to C(yes) on newer hosts where become does not work due to further privilege restrictions from the OS defaults.'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "whitelist": "{'description': ['A list of update titles or KB numbers that can be used to specify which updates are to be searched or installed.', 'If an available update does not match one of the entries, then it is skipped and not installed.', 'Each entry can either be the KB article or Update title as a regex according to the PowerShell regex rules.', 'The whitelist is only validated on updates that were found based on I(category_names). It will not force the module to install an update if it was not in the category specified.'], 'type': 'list', 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Install all security, critical, and rollup updates without a scheduled task
  win_updates:
    category_names:
      - SecurityUpdates
      - CriticalUpdates
      - UpdateRollups

- name: Install only security updates as a scheduled task for Server 2008
  win_updates:
    category_names: SecurityUpdates
    use_scheduled_task: yes

- name: Search-only, return list of found updates (if any), log to C:\ansible_wu.txt
  win_updates:
    category_names: SecurityUpdates
    state: searched
    log_path: C:\ansible_wu.txt

- name: Install all security updates with automatic reboots
  win_updates:
    category_names:
    - SecurityUpdates
    reboot: yes

- name: Install only particular updates based on the KB numbers
  win_updates:
    category_name:
    - SecurityUpdates
    whitelist:
    - KB4056892
    - KB4073117

- name: Exlude updates based on the update title
  win_updates:
    category_name:
    - SecurityUpdates
    - CriticalUpdates
    blacklist:
    - Windows Malicious Software Removal Tool for Windows
    - \d{4}-\d{2} Cumulative Update for Windows Server 2016

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
