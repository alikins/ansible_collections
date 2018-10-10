# Ansible module: ansible.module_clc_server_snapshot


Create, Delete and Restore server snapshots in CenturyLink Cloud

## Description

An Ansible module to Create, Delete and Restore server snapshots in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "expiration_days": "{'description': ['The number of days to keep the server snapshot before it expires.'], 'default': 7, 'required': False}",
    "server_ids": "{'description': ['The list of CLC server Ids.'], 'required': True}",
    "state": "{'description': ['The state to insure that the provided resources are in.'], 'default': 'present', 'required': False, 'choices': ['present', 'absent', 'restore']}",
    "wait": "{'description': ['Whether to wait for the provisioning tasks to finish before returning.'], 'default': True, 'required': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Create server snapshot
  clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    expiration_days: 10
    wait: True
    state: present

- name: Restore server snapshot
  clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    wait: True
    state: restore

- name: Delete server snapshot
  clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    wait: True
    state: absent

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
