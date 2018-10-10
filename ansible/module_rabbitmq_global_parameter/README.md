# Ansible module: ansible.module_rabbitmq_global_parameter


Adds or removes global parameters to RabbitMQ

## Description

Manage dynamic, cluster-wide global parameters for RabbitMQ

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the global parameter being set'], 'required': True, 'default': None}",
    "node": "{'description': ['erlang node name of the rabbit we wish to configure'], 'required': False, 'default': 'rabbit'}",
    "state": "{'description': ['Specify if user is to be added or removed'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "value": "{'description': ['Value of the global parameter, as a JSON term'], 'required': False, 'default': None}",
}
```

## Examples


``` yaml

# Set the global parameter 'cluster_name' to a value of 'mq-cluster' (in quotes)
- rabbitmq_global_parameter:
    name: cluster_name
    value: "{{ 'mq-cluster' | to_json }}"
    state: present

```

## License

TODO

## Author Information
  - ['Juergen Kirschbaum (@jgkirschbaum)']
