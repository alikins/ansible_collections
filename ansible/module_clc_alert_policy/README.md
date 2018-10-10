# Ansible module: ansible.module_clc_alert_policy


Create or Delete Alert Policies at CenturyLink Cloud

## Description

An Ansible module to Create or Delete Alert Policies at CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "alert_recipients": "{'description': ["A list of recipient email ids to notify the alert. This is required for state 'present'"]}",
    "alias": "{'description': ['The alias of your CLC Account'], 'required': True}",
    "duration": "{'description': ["The length of time in minutes that the condition must exceed the threshold. This is required for state 'present'"]}",
    "id": "{'description': ['The alert policy id. This is mutually exclusive with name']}",
    "metric": "{'description': ["The metric on which to measure the condition that will trigger the alert. This is required for state 'present'"], 'choices': ['cpu', 'memory', 'disk']}",
    "name": "{'description': ['The name of the alert policy. This is mutually exclusive with id']}",
    "state": "{'description': ['Whether to create or delete the policy.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "threshold": "{'description': ["The threshold that will trigger the alert when the metric equals or exceeds it. This is required for state 'present' This number represents a percentage and must be a value between 5.0 - 95.0 that is a multiple of 5.0"]}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

---
- name: Create Alert Policy Example
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create an Alert Policy for disk above 80% for 5 minutes
      clc_alert_policy:
        alias: wfad
        name: 'alert for disk > 80%'
        alert_recipients:
            - test1@centurylink.com
            - test2@centurylink.com
        metric: 'disk'
        duration: '00:05:00'
        threshold: 80
        state: present
      register: policy

    - name: debug
      debug: var=policy

---
- name: Delete Alert Policy Example
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Delete an Alert Policy
      clc_alert_policy:
        alias: wfad
        name: 'alert for disk > 80%'
        state: absent
      register: policy

    - name: debug
      debug: var=policy

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
