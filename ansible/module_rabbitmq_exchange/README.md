# Ansible module: ansible.module_rabbitmq_exchange


This module manages rabbitMQ exchanges

## Description

This module uses rabbitMQ Rest API to create/delete exchanges

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['extra arguments for exchange. If defined this argument is a key/value dictionary'], 'required': False, 'default': {}}",
    "auto_delete": "{'description': ['if the exchange should delete itself after all queues/exchanges unbound from it'], 'required': False, 'type': 'bool', 'default': False}",
    "durable": "{'description': ['whether exchange is durable or not'], 'required': False, 'type': 'bool', 'default': True}",
    "exchange_type": "{'description': ['type for the exchange'], 'required': False, 'choices': ['fanout', 'direct', 'headers', 'topic'], 'aliases': ['type'], 'default': 'direct'}",
    "internal": "{'description': ['exchange is available only for other exchanges'], 'required': False, 'type': 'bool', 'default': False}",
    "login_host": "{'description': ['rabbitMQ host for connection'], 'required': False, 'default': 'localhost'}",
    "login_password": "{'description': ['rabbitMQ password for connection'], 'required': False, 'default': False}",
    "login_port": "{'description': ['rabbitMQ management api port'], 'required': False, 'default': 15672}",
    "login_user": "{'description': ['rabbitMQ user for connection'], 'required': False, 'default': 'guest'}",
    "name": "{'description': ['Name of the exchange to create'], 'required': True}",
    "state": "{'description': ['Whether the exchange should be present or absent', 'Only present implemented atm'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
    "vhost": "{'description': ['rabbitMQ virtual host'], 'required': False, 'default': '/'}",
}
```

## Examples


``` yaml

# Create direct exchange
- rabbitmq_exchange:
    name: directExchange

# Create topic exchange on vhost
- rabbitmq_exchange:
    name: topicExchange
    type: topic
    vhost: myVhost

```

## License

TODO

## Author Information
  - ['Manuel Sousa (@manuel-sousa)']
