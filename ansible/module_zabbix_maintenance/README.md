# Ansible module: ansible.module_zabbix_maintenance


Create Zabbix maintenance windows

## Description

This module will let you create Zabbix maintenance windows.

## Requirements

TODO

## Arguments

``` json
{
    "collect_data": "{'description': ['Type of maintenance. With data collection, or without.'], 'type': 'bool', 'default': True}",
    "desc": "{'description': ['Short description of maintenance window.'], 'required': True, 'default': 'Created by Ansible'}",
    "host_groups": "{'description': ['Host groups to manage maintenance window for. Separate multiple groups with commas. C(host_group) is an alias for C(host_groups). B(Required) option when C(state) is I(present) and no C(host_names) specified.'], 'aliases': ['host_group']}",
    "host_names": "{'description': ['Hosts to manage maintenance window for. Separate multiple hosts with commas. C(host_name) is an alias for C(host_names). B(Required) option when C(state) is I(present) and no C(host_groups) specified.'], 'aliases': ['host_name']}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "minutes": "{'description': ['Length of maintenance window in minutes.'], 'default': 10}",
    "name": "{'description': ['Unique name of maintenance window.'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['Create or remove a maintenance window. Maintenance window to remove is identified by name.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Create a named maintenance window for host www1 for 90 minutes
  zabbix_maintenance:
    name: Update of www1
    host_name: www1.example.com
    state: present
    minutes: 90
    server_url: https://monitoring.example.com
    login_user: ansible
    login_password: pAsSwOrD

- name: Create a named maintenance window for host www1 and host groups Office and Dev
  zabbix_maintenance:
    name: Update of www1
    host_name: www1.example.com
    host_groups:
      - Office
      - Dev
    state: present
    server_url: https://monitoring.example.com
    login_user: ansible
    login_password: pAsSwOrD

- name: Create a named maintenance window for hosts www1 and db1, without data collection.
  zabbix_maintenance:
    name: update
    host_names:
      - www1.example.com
      - db1.example.com
    state: present
    collect_data: False
    server_url: https://monitoring.example.com
    login_user: ansible
    login_password: pAsSwOrD

- name: Remove maintenance window by name
  zabbix_maintenance:
    name: Test1
    state: absent
    server_url: https://monitoring.example.com
    login_user: ansible
    login_password: pAsSwOrD

```

## License

TODO

## Author Information
  - ['Alexander Bulimov (@abulimov)']
