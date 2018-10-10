# Ansible module: ansible.module_zabbix_template


create/delete/dump zabbix template

## Description

create/delete/dump zabbix template

## Requirements

TODO

## Arguments

``` json
{
    "clear_templates": "{'description': ['List of templates cleared from the template.', 'see templates_clear in https://www.zabbix.com/documentation/3.0/manual/api/reference/template/update'], 'required': False}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "link_templates": "{'description': ['List of templates linked to the template.'], 'required': False}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "macros": "{'description': ['List of templates macro'], 'required': False}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['state present create/update template, absent delete template'], 'required': False, 'choices': ['present', 'absent', 'dump'], 'default': 'present'}",
    "template_groups": "{'description': ['List of template groups to create or delete.'], 'required': False}",
    "template_json": "{'description': ['JSON dump of template to import'], 'required': False}",
    "template_name": "{'description': ['Name of zabbix template'], 'required': True}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

---
# Creates a new zabbix template from linked template
- name: Create Zabbix template using linked template
  local_action:
    module: zabbix_template
    server_url: http://127.0.0.1
    login_user: username
    login_password: password
    template_name: ExampleHost
    template_json: "{'zabbix_export': {}}"
    template_groups:
      - Role
      - Role2
    link_templates:
      - Example template1
      - Example template2
    clear_templates:
      - Example template3
      - Example template4
    macros:
      - macro: '{$EXAMPLE_MACRO1}'
        value: 30000
      - macro: '{$EXAMPLE_MACRO2}'
        value: 3
      - macro: '{$EXAMPLE_MACRO3}'
        value: 'Example'
    state: present

# Create a new template from a json config definition
- name: Import Zabbix json template configuration
  local_action:
    module: zabbix_template
    server_url: http://127.0.0.1
    login_user: username
    login_password: password
    template_name: Apache2
    template_json: "{{ lookup('file', 'zabbix_apache2.json') }}"
    template_groups:
      - Webservers
    state: present

# Import a template from Ansible variable dict
- name: Import Zabbix Template
  zabbix_template:
    login_user: username
    login_password: password
    server_url: http://127.0.0.1
    template_name: Test Template
    template_json:
      zabbix_export:
        version: '3.2'
        templates:
          - name: Template for Testing
            description: 'Testing template import'
            template: Test Template
            groups:
              - name: Templates
            applications:
              - name: Test Application
    template_groups: Templates
    state: present

# Add a macro to a template
- name: Set a macro on the Zabbix template
  local_action:
    module: zabbix_template
    server_url: http://127.0.0.1
    login_user: username
    login_password: password
    template_name: Template
    macros:
      - macro: '{$TEST_MACRO}'
        value: 'Example'
    state: present

# Remove a template
- name: Delete Zabbix template
  local_action:
    module: zabbix_template
    server_url: http://127.0.0.1
    login_user: username
    login_password: password
    template_name: Template
    state: absent

# Export template json definition
- name: Dump Zabbix template
  local_action:
    module: zabbix_template
    server_url: http://127.0.0.1
    login_user: username
    login_password: password
    template_name: Template
    state: dump
  register: template_dump

```

## License

TODO

## Author Information
  - ['@sookido', 'Logan Vig (@logan2211)']
  - ['@sookido', 'Logan Vig (@logan2211)']
