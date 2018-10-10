# Ansible module: ansible.module_netapp_e_auditlog


NetApp E-Series manage audit-log configuration

## Description

This module allows an e-series storage system owner to set audit-log configuration parameters.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "force": "{'description': ['Forces the audit-log configuration to delete log history when log messages fullness cause immediate warning or full condition.', 'Warning! This will cause any existing audit-log messages to be deleted.', 'This is only applicable for I(full_policy=preventSystemAccess).'], 'type': 'bool', 'default': False}",
    "full_policy": "{'description': ['Specifies what audit-log should do once the number of entries approach the record limit.'], 'choices': ['overWrite', 'preventSystemAccess'], 'default': 'overWrite'}",
    "log_level": "{'description': ['Filters the log messages according to the specified log level selection.'], 'choices': ['all', 'writeOnly'], 'default': 'writeOnly'}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging.'], 'required': False}",
    "max_records": "{'description': ['The maximum number log messages audit-log will retain.', 'Max records must be between and including 100 and 50000.'], 'default': 50000}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "threshold": "{'description': ['This is the memory full percent threshold that audit-log will start issuing warning messages.', 'Percent range must be between and including 60 and 90.'], 'default': 90}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Define audit-log to prevent system access if records exceed 50000 with warnings occurring at 60% capacity.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
     validate_certs: no
     max_records: 50000
     log_level: all
     full_policy: preventSystemAccess
     threshold: 60
     log_path: /path/to/log_file.log
- name: Define audit-log utilize the default values.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
- name: Force audit-log configuration when full or warning conditions occur while enacting preventSystemAccess policy.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
     max_records: 5000
     log_level: all
     full_policy: preventSystemAccess
     threshold: 60
     force: yes

```

## License

TODO

## Author Information
  - ['Nathan Swartz (@ndswartz)']
