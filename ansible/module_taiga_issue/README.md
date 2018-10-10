# Ansible module: ansible.module_taiga_issue


Creates/deletes an issue in a Taiga Project Management Platform

## Description

Creates/deletes an issue in a Taiga Project Management Platform (U(https://taiga.io)).
An issue is identified by the combination of project, issue subject and issue type.
This module implements the creation or deletion of issues (not the update).

## Requirements

TODO

## Arguments

``` json
{
    "attachment": "{'description': ['Path to a file to be attached to the issue.']}",
    "attachment_description": "{'description': ['A string describing the file to be attached to the issue.'], 'default': ''}",
    "description": "{'description': ['The issue description.'], 'default': ''}",
    "issue_type": "{'description': ['The issue type. Must exist previously.'], 'required': True}",
    "priority": "{'description': ['The issue priority. Must exist previously.'], 'default': 'Normal'}",
    "project": "{'description': ['Name of the project containing the issue. Must exist previously.'], 'required': True}",
    "severity": "{'description': ['The issue severity. Must exist previously.'], 'default': 'Normal'}",
    "state": "{'description': ['Whether the issue should be present or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "status": "{'description': ['The issue status. Must exist previously.'], 'default': 'New'}",
    "subject": "{'description': ['The issue subject.'], 'required': True}",
    "tags": "{'description': ['A lists of tags to be assigned to the issue.'], 'default': []}",
    "taiga_host": "{'description': ['The hostname of the Taiga instance.'], 'default': 'https://api.taiga.io'}",
}
```

## Examples


``` yaml

# Create an issue in the my hosted Taiga environment and attach an error log
- taiga_issue:
    taiga_host: https://mytaigahost.example.com
    project: myproject
    subject: An error has been found
    issue_type: Bug
    priority: High
    status: New
    severity: Important
    description: An error has been found. Please check the attached error log for details.
    attachment: /path/to/error.log
    attachment_description: Error log file
    tags:
      - Error
      - Needs manual check
    state: present

# Deletes the previously created issue
- taiga_issue:
    taiga_host: https://mytaigahost.example.com
    project: myproject
    subject: An error has been found
    issue_type: Bug
    state: absent

```

## License

TODO

## Author Information
  - ['Alejandro Guirao (@lekum)']
