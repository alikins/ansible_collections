# Ansible module: ansible.module_jira


create and modify issues in a JIRA instance

## Description

Create and modify issues in a JIRA instance.

## Requirements

TODO

## Arguments

``` json
{
    "assignee": "{'required': False, 'description': ['Sets the assignee on create or transition operations. Note not all transitions will allow this.']}",
    "comment": "{'required': False, 'description': ['The comment text to add.']}",
    "description": "{'required': False, 'description': ['The issue description, where appropriate.']}",
    "fields": "{'required': False, 'description': ['This is a free-form data structure that can contain arbitrary data. This is passed directly to the JIRA REST API (possibly after merging with other required data, as when passed to create). See examples for more information, and the JIRA REST API for the structure required for various fields.']}",
    "inwardissue": "{'required': False, 'version_added': 2.3, 'description': ['Set issue from which link will be created.']}",
    "issue": "{'required': False, 'description': ['An existing issue key to operate on.']}",
    "issuetype": "{'required': False, 'description': ['The issue type, for issue creation.']}",
    "linktype": "{'required': False, 'version_added': 2.3, 'description': ["Set type of link, when action 'link' selected."]}",
    "operation": "{'required': True, 'aliases': ['command'], 'choices': ['create', 'comment', 'edit', 'fetch', 'transition', 'link'], 'description': ['The operation to perform.']}",
    "outwardissue": "{'required': False, 'version_added': 2.3, 'description': ['Set issue to which link will be created.']}",
    "password": "{'required': True, 'description': ['The password to log-in with.']}",
    "project": "{'required': False, 'description': ['The project for this operation. Required for issue creation.']}",
    "status": "{'required': False, 'description': ['The desired status; only relevant for the transition operation.']}",
    "summary": "{'required': False, 'description': ['The issue summary, where appropriate.']}",
    "timeout": "{'required': False, 'version_added': 2.3, 'description': ['Set timeout, in seconds, on requests to JIRA API.'], 'default': 10}",
    "uri": "{'required': True, 'description': ['Base URI for the JIRA instance.']}",
    "username": "{'required': True, 'description': ['The username to log-in with.']}",
    "validate_certs": "{'required': False, 'version_added': 2.5, 'description': ["Require valid SSL certificates (set to `false` if you'd like to use self-signed certificates)"], 'default': True}",
}
```

## Examples


``` yaml

# Create a new issue and add a comment to it:
- name: Create an issue
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: create
    summary: Example Issue
    description: Created using Ansible
    issuetype: Task
  register: issue

- name: Comment on issue
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: comment
    comment: A comment added by Ansible

# Assign an existing issue using edit
- name: Assign an issue using free-form fields
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key}}'
    operation: edit
    assignee: ssmith

# Create an issue with an existing assignee
- name: Create an assigned issue
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: create
    summary: Assigned issue
    description: Created and assigned using Ansible
    issuetype: Task
    assignee: ssmith

# Edit an issue
- name: Set the labels on an issue using free-form fields
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: edit
  args:
    fields:
        labels:
          - autocreated
          - ansible

# Retrieve metadata for an issue and use it to create an account
- name: Get an issue
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    project: ANS
    operation: fetch
    issue: ANS-63
  register: issue

- name: Create a unix account for the reporter
  become: true
  user:
    name: '{{ issue.meta.fields.creator.name }}'
    comment: '{{ issue.meta.fields.creator.displayName }}'

# You can get list of valid linktypes at /rest/api/2/issueLinkType
# url of your jira installation.
- name: Create link from HSP-1 to MKY-1
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    operation: link
    linktype: Relates
    inwardissue: HSP-1
    outwardissue: MKY-1

# Transition an issue by target status
- name: Close the issue
  jira:
    uri: '{{ server }}'
    username: '{{ user }}'
    password: '{{ pass }}'
    issue: '{{ issue.meta.key }}'
    operation: transition
    status: Done

```

## License

TODO

## Author Information
  - ['Steve Smith (@tarka)']
