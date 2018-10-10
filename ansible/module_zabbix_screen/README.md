# Ansible module: ansible.module_zabbix_screen


Zabbix screen creates/updates/deletes

## Description

This module allows you to create, modify and delete Zabbix screens and associated graph data.

## Requirements

TODO

## Arguments

``` json
{
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "screens": "{'description': ['List of screens to be created/updated/deleted(see example).', "If the screen(s) already been added, the screen(s) name won't be updated.", 'When creating or updating screen(s), C(screen_name), C(host_group) are required.', 'When deleting screen(s), the C(screen_name) is required.', 'Option C(graphs_in_row) will limit columns of screen and make multiple rows (default 3)', 'The available states are: C(present) (default) and C(absent). If the screen(s) already exists, and the state is not C(absent), the screen(s) will just be updated as needed.\n'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Create/update a screen.
- name: Create a new screen or update an existing screen's items 5 in a row
  local_action:
    module: zabbix_screen
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    screens:
      - screen_name: ExampleScreen1
        host_group: Example group1
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
        graphs_in_row: 5

# Create/update multi-screen
- name: Create two of new screens or update the existing screens' items
  local_action:
    module: zabbix_screen
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    screens:
      - screen_name: ExampleScreen1
        host_group: Example group1
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
      - screen_name: ExampleScreen2
        host_group: Example group2
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100

# Limit the Zabbix screen creations to one host since Zabbix can return an error when doing concurrent updates
- name: Create a new screen or update an existing screen's items
  local_action:
    module: zabbix_screen
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    state: present
    screens:
      - screen_name: ExampleScreen
        host_group: Example group
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
  when: inventory_hostname==groups['group_name'][0]

```

## License

TODO

## Author Information
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)']
