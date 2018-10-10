# Ansible module: ansible.module_win_eventlog


Manage Windows event logs

## Description

Allows the addition, clearing and removal of local Windows event logs, and the creation and removal of sources from a given event log.  Also allows the specification of settings per log and source.

## Requirements

TODO

## Arguments

``` json
{
    "category_file": "{'description': ['For one or more sources specified, the path to a custom category resource file.'], 'type': 'path'}",
    "maximum_size": "{'description': ['The maximum size of the event log.', 'Value must be between 64KB and 4GB, and divisible by 64KB.', 'Size can be specified in KB, MB or GB (e.g. 128KB, 16MB, 2.5GB).']}",
    "message_file": "{'description': ['For one or more sources specified, the path to a custom event message resource file.'], 'type': 'path'}",
    "name": "{'description': ['Name of the event log to manage.'], 'required': True}",
    "overflow_action": "{'description': ['The action for the log to take once it reaches its maximum size.', 'For C(OverwriteOlder), new log entries overwrite those older than the C(retention_days) value.', 'For C(OverwriteAsNeeded), each new entry overwrites the oldest entry.', 'For C(DoNotOverwrite), all existing entries are kept and new entries are not retained.'], 'choices': ['OverwriteOlder', 'OverwriteAsNeeded', 'DoNotOverwrite']}",
    "parameter_file": "{'description': ['For one or more sources specified, the path to a custom parameter resource file.'], 'type': 'path'}",
    "retention_days": "{'description': ['The minimum number of days event entries must remain in the log.', 'This option is only used when C(overflow_action) is C(OverwriteOlder).'], 'type': 'int'}",
    "sources": "{'description': ['A list of one or more sources to ensure are present/absent in the log.', 'When C(category_file), C(message_file) and/or C(parameter_file) are specified, these values are applied across all sources.'], 'type': 'list'}",
    "state": "{'description': ['Desired state of the log and/or sources.', 'When C(sources) is populated, state is checked for sources.', 'When C(sources) is not populated, state is checked for the specified log itself.', 'If C(state) is C(clear), event log entries are cleared for the target log.'], 'choices': ['absent', 'clear', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add a new event log with two custom sources
  win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource1
      - NewLogSource2
    state: present

- name: Change the category and message resource files used for NewLogSource1
  win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource1
    category_file: C:\NewApp\CustomCategories.dll
    message_file: C:\NewApp\CustomMessages.dll
    state: present

- name: Change the maximum size and overflow action for MyNewLog
  win_eventlog:
    name: MyNewLog
    maximum_size: 16MB
    overflow_action: DoNotOverwrite
    state: present

- name: Clear event entries for MyNewLog
  win_eventlog:
    name: MyNewLog
    state: clear

- name: Remove NewLogSource2 from MyNewLog
  win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource2
    state: absent

- name: Remove MyNewLog and all remaining sources
  win_eventlog:
    name: MyNewLog
    state: absent

```

## License

TODO

## Author Information
  - ['Andrew Saraceni (@andrewsaraceni)']
