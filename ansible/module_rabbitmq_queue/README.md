# Ansible module: ansible.module_rabbitmq_queue


This module manages rabbitMQ queues

## Description

This module uses rabbitMQ Rest API to create/delete queues

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['extra arguments for queue. If defined this argument is a key/value dictionary'], 'default': {}}",
    "auto_delete": "{'description': ['if the queue should delete itself after all queues/queues unbound from it'], 'type': 'bool', 'default': False}",
    "auto_expires": "{'description': ['How long a queue can be unused before it is automatically deleted (milliseconds)'], 'default': 'forever'}",
    "dead_letter_exchange": "{'description': ['Optional name of an exchange to which messages will be republished if they', 'are rejected or expire']}",
    "dead_letter_routing_key": "{'description': ['Optional replacement routing key to use when a message is dead-lettered.', 'Original routing key will be used if unset']}",
    "durable": "{'description': ['whether queue is durable or not'], 'type': 'bool', 'default': True}",
    "login_host": "{'description': ['rabbitMQ host for connection'], 'default': 'localhost'}",
    "login_password": "{'description': ['rabbitMQ password for connection'], 'type': 'bool', 'default': False}",
    "login_port": "{'description': ['rabbitMQ management api port'], 'default': 15672}",
    "login_user": "{'description': ['rabbitMQ user for connection'], 'default': 'guest'}",
    "max_length": "{'description': ['How many messages can the queue contain before it starts rejecting'], 'default': 'no limit'}",
    "max_priority": "{'description': ['Maximum number of priority levels for the queue to support.', 'If not set, the queue will not support message priorities.', 'Larger numbers indicate higher priority.'], 'version_added': '2.4'}",
    "message_ttl": "{'description': ['How long a message can live in queue before it is discarded (milliseconds)'], 'default': 'forever'}",
    "name": "{'description': ['Name of the queue to create'], 'required': True}",
    "state": "{'description': ['Whether the queue should be present or absent', 'Only present implemented atm'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vhost": "{'description': ['rabbitMQ virtual host'], 'default': '/'}",
}
```

## Examples


``` yaml

# Create a queue
- rabbitmq_queue:
    name: myQueue

# Create a queue on remote host
- rabbitmq_queue:
    name: myRemoteQueue
    login_user: user
    login_password: secret
    login_host: remote.example.org

```

## License

TODO

## Author Information
  - ['Manuel Sousa (@manuel-sousa)']
