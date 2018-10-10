# Ansible module: ansible.module_rabbitmq_plugin


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
    "prefix": "{'description': ['Specify a custom install prefix to a Rabbit.'], 'version_added': '1.3'}",
    "state": "{'description': ['Specify if plugins are to be enabled or disabled.'], 'default': 'enabled', 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Enables the rabbitmq_management plugin
  rabbitmq_plugin:
    names: rabbitmq_management
    state: enabled

```

## License

TODO

## Author Information
  - ['Chris Hoffman (@chrishoffman)']
