# Ansible module: ansible.module_zabbix_group_facts


Gather facts about Zabbix hostgroup

## Description

This module allows you to search for Zabbix hostgroup entries.

## Requirements

TODO

## Arguments

``` json
{
    "hostgroup_name": "{'description': ['Name of the hostgroup in Zabbix.', 'hostgroup is the unique identifier used and cannot be updated using this module.'], 'required': True}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Get hostgroup info
  local_action:
    module: zabbix_group_facts
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    hostgroup_name:
      - ExampleHostgroup
    timeout: 10

```

## License

TODO

## Author Information
  - ['(@redwhitemiko)']
