# Ansible module: ansible.module_zabbix_host_facts


Gather facts about Zabbix host

## Description

This module allows you to search for Zabbix host entries.

## Requirements

TODO

## Arguments

``` json
{
    "exact_match": "{'description': ['Find the exact match'], 'type': 'bool', 'default': False}",
    "host_ip": "{'description': ['Host interface IP of the host in Zabbix.'], 'required': False}",
    "host_name": "{'description': ['Name of the host in Zabbix.', 'host_name is the unique identifier used and cannot be updated using this module.'], 'required': True}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "remove_duplicate": "{'description': ['Remove duplicate host from host result'], 'type': 'bool', 'default': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Get host info
  local_action:
    module: zabbix_host_facts
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    host_name: ExampleHost
    host_ip: 127.0.0.1
    timeout: 10
    exact_match: no
    remove_duplicate: yes

```

## License

TODO

## Author Information
  - ['(@redwhitemiko)']
