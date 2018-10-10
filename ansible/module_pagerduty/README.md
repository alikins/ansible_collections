# Ansible module: ansible.module_pagerduty


Create PagerDuty maintenance windows

## Description

This module will let you create PagerDuty maintenance windows

## Requirements

TODO

## Arguments

``` json
{
    "desc": "{'description': ['Short description of maintenance window.'], 'default': 'Created by Ansible'}",
    "hours": "{'description': ['Length of maintenance window in hours.'], 'default': 1}",
    "minutes": "{'description': ['Maintenance window in minutes (this is added to the hours).'], 'default': 0, 'version_added': '1.8'}",
    "name": "{'description': ['PagerDuty unique subdomain. Obsolete. It is not used with PagerDuty REST v2 API.']}",
    "requester_id": "{'description': ['ID of user making the request. Only needed when creating a maintenance_window.'], 'version_added': '1.8'}",
    "service": "{'description': ['A comma separated list of PagerDuty service IDs.'], 'aliases': ['services']}",
    "state": "{'description': ['Create a maintenance window or get a list of ongoing windows.'], 'required': True, 'choices': ['running', 'started', 'ongoing', 'absent']}",
    "token": "{'description': ['A pagerduty token, generated on the pagerduty site. It is used for authorization.'], 'required': True, 'version_added': '1.8'}",
    "user": "{'description': ['PagerDuty user ID. Obsolete. Please, use I(token) for authorization.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.5.1'}",
    "window_id": "{'description': ['ID of maintenance window. Only needed when absent a maintenance_window.'], 'version_added': '2.7'}",
}
```

## Examples


``` yaml

# List ongoing maintenance windows using a token
- pagerduty:
    name: companyabc
    token: xxxxxxxxxxxxxx
    state: ongoing

# Create a 1 hour maintenance window for service FOO123
- pagerduty:
    name: companyabc
    user: example@example.com
    token: yourtoken
    state: running
    service: FOO123

# Create a 5 minute maintenance window for service FOO123
- pagerduty:
    name: companyabc
    token: xxxxxxxxxxxxxx
    hours: 0
    minutes: 5
    state: running
    service: FOO123


# Create a 4 hour maintenance window for service FOO123 with the description "deployment".
- pagerduty:
    name: companyabc
    user: example@example.com
    state: running
    service: FOO123
    hours: 4
    desc: deployment
  register: pd_window

# Delete the previous maintenance window
- pagerduty:
    name: companyabc
    user: example@example.com
    state: absent
    window_id: '{{ pd_window.result.maintenance_window.id }}'

```

## License

TODO

## Author Information
  - ['Andrew Newdigate (@suprememoocow)', 'Dylan Silva (@thaumos)', 'Justin Johns', 'Bruce Pennypacker']
  - ['Andrew Newdigate (@suprememoocow)', 'Dylan Silva (@thaumos)', 'Justin Johns', 'Bruce Pennypacker']
  - ['Andrew Newdigate (@suprememoocow)', 'Dylan Silva (@thaumos)', 'Justin Johns', 'Bruce Pennypacker']
  - ['Andrew Newdigate (@suprememoocow)', 'Dylan Silva (@thaumos)', 'Justin Johns', 'Bruce Pennypacker']
