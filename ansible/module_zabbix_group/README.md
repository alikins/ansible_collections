# Ansible module: ansible.module_zabbix_group


Zabbix host groups creates/deletes

## Description

Create host groups if they do not exist.
Delete existing host groups if they exist.

## Requirements

TODO

## Arguments

``` json
{
    "host_groups": "{'description': ['List of host groups to create or delete.'], 'required': True, 'aliases': ['host_group']}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['Create or delete host group.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Base create host groups example
- name: Create host groups
  local_action:
    module: zabbix_group
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    state: present
    host_groups:
      - Example group1
      - Example group2

# Limit the Zabbix group creations to one host since Zabbix can return an error when doing concurrent updates
- name: Create host groups
  local_action:
    module: zabbix_group
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    state: present
    host_groups:
      - Example group1
      - Example group2
  when: inventory_hostname==groups['group_name'][0]

```

## License

TODO

## Author Information
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
