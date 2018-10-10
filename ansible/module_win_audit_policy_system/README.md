# Ansible module: ansible.module_win_audit_policy_system


Used to make changes to the system wide Audit Policy

## Description

Used to make changes to the system wide Audit Policy.
It is recommended to take a backup of the policies before adjusting them for the first time.
See this page for in depth information U(https://technet.microsoft.com/en-us/library/cc766468.aspx).

## Requirements

TODO

## Arguments

``` json
{
    "audit_type": "{'description': ['The type of event you would like to audit for.', 'Accepts a list. See examples.'], 'required': True, 'type': 'list', 'choices': ['failure', 'none', 'success']}",
    "category": "{'description': ['Single string value for the category you would like to adjust the policy on.', 'Cannot be used with I(subcategory). You must define one or the other.', 'Changing this setting causes all subcategories to be adjusted to the defined I(audit_type).']}",
    "subcategory": "{'description': ['Single string value for the subcategory you would like to adjust the policy on.', 'Cannot be used with I(category). You must define one or the other.']}",
}
```

## Examples


``` yaml

- name: enable failure auditing for the subcategory "File System"
  win_audit_policy_system:
    subcategory: File System
    audit_type: failure

- name: enable all auditing types for the category "Account logon events"
  win_audit_policy_system:
    category: Account logon events
    audit_type: success, failure

- name: disable auditing for the subcategory "File System"
  win_audit_policy_system:
    subcategory: File System
    audit_type: none

```

## License

TODO

## Author Information
  - ['Noah Sparks (@nwsparks)']
