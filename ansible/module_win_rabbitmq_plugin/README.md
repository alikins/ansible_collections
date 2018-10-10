# Ansible module: ansible.module_win_rabbitmq_plugin


Manage RabbitMQ plugins

## Description

Manage RabbitMQ plugins.

## Requirements

TODO

## Arguments

``` json
{
    "names": "{'description': ['Comma-separated list of plugin names.'], 'required': True, 'aliases': ['name']}",
    "new_only": "{'description': ['Only enable missing plugins.', 'Does not disable plugins that are not in the names list.'], 'type': 'bool', 'default': False}",
    "prefix": "{'description': ['Specify a custom install prefix to a Rabbit.']}",
    "state": "{'description': ['Specify if plugins are to be enabled or disabled.'], 'choices': ['disabled', 'enabled'], 'default': 'enabled'}",
}
```

## Examples


``` yaml

- name: Enables the rabbitmq_management plugin
  win_rabbitmq_plugin:
    names: rabbitmq_management
    state: enabled

```

## License

TODO

## Author Information
  - ['Artem Zinenko (@ar7z1)']
