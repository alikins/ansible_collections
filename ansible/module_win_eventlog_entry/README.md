# Ansible module: ansible.module_win_eventlog_entry


Write entries to Windows event logs

## Description

Write log entries to a given event log from a specified source.

## Requirements

TODO

## Arguments

``` json
{
    "category": "{'description': ['A numeric task category associated with the category message file for the log source.'], 'type': 'int'}",
    "entry_type": "{'description': ['Indicates the entry being written to the log is of a specific type.'], 'choices': ['Error', 'FailureAudit', 'Information', 'SuccessAudit', 'Warning']}",
    "event_id": "{'description': ['The numeric event identifier for the entry.', 'Value must be between 0 and 65535.'], 'required': True, 'type': 'int'}",
    "log": "{'description': ['Name of the event log to write an entry to.'], 'required': True}",
    "message": "{'description': ['The message for the given log entry.'], 'required': True}",
    "raw_data": "{'description': ['Binary data associated with the log entry.', 'Value must be a comma-separated array of 8-bit unsigned integers (0 to 255).']}",
    "source": "{'description': ['Name of the log source to indicate where the entry is from.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Write an entry to a Windows event log
  win_eventlog_entry:
    log: MyNewLog
    source: NewLogSource1
    event_id: 1234
    message: This is a test log entry.

- name: Write another entry to a different Windows event log
  win_eventlog_entry:
    log: AnotherLog
    source: MyAppSource
    event_id: 5000
    message: An error has occurred.
    entry_type: Error
    category: 5
    raw_data: 10,20

```

## License

TODO

## Author Information
  - ['Andrew Saraceni (@andrewsaraceni)']
