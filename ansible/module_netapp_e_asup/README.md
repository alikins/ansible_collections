# Ansible module: ansible.module_netapp_e_asup


NetApp E-Series manage auto-support settings

## Description

Allow the auto-support settings to be configured for an individual E-Series storage-system

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ["Enable active/proactive monitoring for ASUP. When a problem is detected by our monitoring systems, it's possible that the bundle did not contain all of the required information at the time of the event. Enabling this option allows NetApp support personnel to manually request transmission or re-transmission of support data in order ot resolve the problem.", 'Only applicable if I(state=enabled).'], 'default': True, 'type': 'bool'}",
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "days": "{'description': ['A list of days of the week that ASUP bundles will be sent. A larger, weekly bundle will be sent on one of the provided days.'], 'choices': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'required': False, 'aliases': ['days_of_week', 'schedule_days']}",
    "end": "{'description': ['An end hour may be specified in a range from 1 to 24 hours.', 'ASUP bundles will be sent daily between the provided start and end time (UTC).', 'I(start) must be less than I(end).'], 'aliases': ['end_time'], 'default': 24}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "start": "{'description': ['A start hour may be specified in a range from 0 to 23 hours.', 'ASUP bundles will be sent daily between the provided start and end time (UTC).', 'I(start) must be less than I(end).'], 'aliases': ['start_time'], 'default': 0}",
    "state": "{'description': ['Enable/disable the E-Series auto-support configuration.', 'When this option is enabled, configuration, logs, and other support-related information will be relayed to NetApp to help better support your system. No personally identifiable information, passwords, etc, will be collected.'], 'default': 'enabled', 'choices': ['enabled', 'disabled'], 'aliases': ['asup', 'auto_support', 'autosupport']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
    "verbose": "{'description': ['Provide the full ASUP configuration in the return.'], 'default': False, 'required': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Enable ASUP and allow pro-active retrieval of bundles
      netapp_e_asup:
        state: enabled
        active: yes
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

    - name: Set the ASUP schedule to only send bundles from 12 AM CST to 3 AM CST.
      netapp_e_asup:
        start: 17
        end: 20
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
