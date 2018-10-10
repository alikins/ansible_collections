# Ansible module: ansible.module_ucs_timezone


Configures timezone on Cisco UCS Manager

## Description

Configures timezone on Cisco UCS Manager.
Examples can be used with the L(UCS Platform Emulator,https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['The admin_state setting', 'The enabled admin_state indicates the timezone confguration is utilized by UCS Manager.', 'The disabled admin_state indicates the timezone confguration is ignored by UCS Manager.'], 'choices': ['disabled', 'enabled'], 'default': 'enabled'}",
    "description": "{'description': ['A user-defined description of the timezone.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr'], 'default': ''}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(absent), will unset timezone.', 'If C(present), will set or update timezone.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "timezone": "{'description': ['The timezone name.', 'Time zone names are from the L(tz database,https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)', 'The timezone name is case sensitive.', 'The timezone name can be between 0 and 510 alphanumeric characters.', 'You cannot use spaces or any special characters other than', '"-" (hyphen), "_" (underscore), "/" (backslash).']}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure Time Zone
  ucs_timezone:
    hostname: 172.16.143.150
    username: admin
    password: password
    state: present
    admin_state: enabled
    timezone: America/Los_Angeles
    description: 'Time Zone for Los Angeles'

- name: Unconfigure Time Zone
  ucs_timezone:
    hostname: 172.16.143.150
    username: admin
    password: password
    state: absent
    admin_state: disabled

```

## License

TODO

## Author Information
  - ['John McDonough (@movinalot)', 'CiscoUcs (@CiscoUcs)']
  - ['John McDonough (@movinalot)', 'CiscoUcs (@CiscoUcs)']
