# Ansible module: ansible.module_rabbitmq_parameter


Adds or removes parameters to RabbitMQ

## Description

Manage dynamic, cluster-wide parameters for RabbitMQ

## Requirements

TODO

## Arguments

``` json
{
    "component": "{'description': ['Name of the component of which the parameter is being set'], 'required': True}",
    "name": "{'description': ['Name of the parameter being set'], 'required': True}",
    "node": "{'description': ['erlang node name of the rabbit we wish to configure'], 'default': 'rabbit'}",
    "state": "{'description': ['Specify if user is to be added or removed'], 'default': 'present', 'choices': ['present', 'absent']}",
    "value": "{'description': ['Value of the parameter, as a JSON term']}",
    "vhost": "{'description': ['vhost to apply access privileges.'], 'default': '/'}",
}
```

## Examples


``` yaml

# Set the federation parameter 'local_username' to a value of 'guest' (in quotes)
- rabbitmq_parameter:
    component: federation
    name: local-username
    value: '"guest"'
    state: present

```

## License

TODO

## Author Information
  - ['"Chris Hoffman (@chrishoffman)"']
