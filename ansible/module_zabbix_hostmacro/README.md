# Ansible module: ansible.module_zabbix_hostmacro


Zabbix host macro creates/updates/deletes

## Description

manages Zabbix host macros, it can create, update or delete them.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Only updates an existing macro if set to C(yes).'], 'default': True, 'type': 'bool', 'version_added': 2.5}",
    "host_name": "{'description': ['Name of the host.'], 'required': True}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "macro_name": "{'description': ['Name of the host macro.'], 'required': True}",
    "macro_value": "{'description': ['Value of the host macro.'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['State of the macro.', 'On C(present), it will create if macro does not exist or update the macro if the associated data is different.', 'On C(absent) will remove a macro if it exists.'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Create a new host macro or update an existing macro's value
  local_action:
    module: zabbix_hostmacro
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    host_name: ExampleHost
    macro_name: Example macro
    macro_value: Example value
    state: present

```

## License

TODO

## Author Information
  - ['(@cave)', 'Dean Hailin Song']
  - ['(@cave)', 'Dean Hailin Song']
