# Ansible module: ansible.module_aos_login


Login to AOS server for session token

## Description

Obtain the AOS server session token by providing the required username and password credentials.  Upon successful authentication, this module will return the session-token that is required by all subsequent AOS module usage. On success the module will automatically populate ansible facts with the variable I(aos_session) This module is not idempotent and do not support check mode.

## Requirements

TODO

## Arguments

``` json
{
    "passwd": "{'description': ['Password to use when connecting to the AOS server.'], 'default': 'admin'}",
    "port": "{'description': ['Port number to use when connecting to the AOS server.'], 'default': 443}",
    "server": "{'description': ['Address of the AOS Server on which you want to open a connection.'], 'required': True}",
    "user": "{'description': ['Login username to use when connecting to the AOS server.'], 'default': 'admin'}",
}
```

## Examples


``` yaml


- name: Create a session with the AOS-server
  aos_login:
    server: "{{ inventory_hostname }}"
    user: admin
    passwd: admin

- name: Use the newly created session (register is not mandatory)
  aos_ip_pool:
    session: "{{ aos_session }}"
    name: my_ip_pool
    state: present

```

## License

TODO

## Author Information
  - ['jeremy@apstra.com (@jeremyschulman)']
