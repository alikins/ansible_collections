# Ansible module: ansible.module_rabbitmq_vhost


Manage the state of a virtual host in RabbitMQ

## Description

Manage the state of a virtual host in RabbitMQ

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the vhost to manage'], 'required': True, 'aliases': ['vhost']}",
    "node": "{'description': ['erlang node name of the rabbit we wish to configure'], 'default': 'rabbit'}",
    "state": "{'description': ['The state of vhost'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tracing": "{'description': ['Enable/disable tracing for a vhost'], 'type': 'bool', 'default': False, 'aliases': ['trace']}",
}
```

## Examples


``` yaml

# Ensure that the vhost /test exists.
- rabbitmq_vhost:
    name: /test
    state: present

```

## License

TODO

## Author Information
  - ['"Chris Hoffman (@choffman)"']
