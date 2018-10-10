# Ansible module: ansible.module_foreman


Manage Foreman Resources

## Description

Allows the management of Foreman resources inside your Foreman server.

## Requirements

TODO

## Arguments

``` json
{
    "entity": "{'description': ['The Foreman resource that the action will be performed on (e.g. organization, host).'], 'required': True}",
    "params": "{'description': ['Parameters associated to the entity resource to set or edit in dictionary format (e.g. name, description).'], 'required': True}",
    "password": "{'description': ['Password for user accessing Foreman server.'], 'required': True}",
    "server_url": "{'description': ['URL of Foreman server.'], 'required': True}",
    "username": "{'description': ['Username on Foreman server.'], 'required': True}",
    "verify_ssl": "{'description': ['Whether to verify an SSL connection to Foreman server.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Create CI Organization
  foreman:
    username: admin
    password: admin
    server_url: https://fakeserver.com
    entity: organization
    params:
      name: My Cool New Organization
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Eric D Helms (@ehelms)']
