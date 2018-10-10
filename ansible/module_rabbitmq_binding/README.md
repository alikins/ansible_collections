# Ansible module: ansible.module_rabbitmq_binding


This module manages rabbitMQ bindings

## Description

This module uses rabbitMQ REST APIs to create / delete bindings.

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['extra arguments for exchange. If defined this argument is a key/value dictionary.'], 'default': {}}",
    "destination": "{'description': ['destination exchange or queue for the binding.'], 'required': True, 'aliases': ['dst', 'dest']}",
    "destination_type": "{'description': ['Either queue or exchange.'], 'required': True, 'choices': ['queue', 'exchange'], 'aliases': ['type', 'dest_type']}",
    "login_host": "{'description': ['rabbitMQ host for the connection.'], 'default': 'localhost'}",
    "login_password": "{'description': ['rabbitMQ password for the connection.'], 'default': False}",
    "login_port": "{'description': ['rabbitMQ management API port.'], 'default': 15672}",
    "login_user": "{'description': ['rabbitMQ user for the connection.'], 'default': 'guest'}",
    "name": "{'description': ['source exchange to create binding on.'], 'required': True, 'aliases': ['src', 'source']}",
    "routing_key": "{'description': ['routing key for the binding.'], 'default': '#'}",
    "state": "{'description': ['Whether the bindings should be present or absent.', 'Only present implemented at the momemt.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vhost": "{'description': ['rabbitMQ virtual host.'], 'default': '/'}",
}
```

## Examples


``` yaml

# Bind myQueue to directExchange with routing key info
- rabbitmq_binding:
    name: directExchange
    destination: myQueue
    type: queue
    routing_key: info

# Bind directExchange to topicExchange with routing key *.info
- rabbitmq_binding:
    name: topicExchange
    destination: topicExchange
    type: exchange
    routing_key: '*.info'

```

## License

TODO

## Author Information
  - ['Manuel Sousa (@manuel-sousa)']
