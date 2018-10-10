# Ansible module: ansible.module_rabbitmq_policy


Manage the state of policies in RabbitMQ

## Description

Manage the state of a policy in RabbitMQ.

## Requirements

TODO

## Arguments

``` json
{
    "apply_to": "{'description': ['What the policy applies to. Requires RabbitMQ 3.2.0 or later.'], 'default': 'all', 'choices': ['all', 'exchanges', 'queues'], 'version_added': '2.1'}",
    "name": "{'description': ['The name of the policy to manage.'], 'required': True}",
    "node": "{'description': ['Erlang node name of the rabbit we wish to configure.'], 'default': 'rabbit'}",
    "pattern": "{'description': ['A regex of queues to apply the policy to.'], 'required': True}",
    "priority": "{'description': ['The priority of the policy.'], 'default': 0}",
    "state": "{'description': ['The state of the policy.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['A dict or string describing the policy.'], 'required': True}",
    "vhost": "{'description': ['The name of the vhost to apply to.'], 'default': '/'}",
}
```

## Examples


``` yaml

- name: ensure the default vhost contains the HA policy via a dict
  rabbitmq_policy:
    name: HA
    pattern: .*
  args:
    tags:
      ha-mode: all

- name: ensure the default vhost contains the HA policy
  rabbitmq_policy:
    name: HA
    pattern: .*
    tags:
      ha-mode: all

```

## License

TODO

## Author Information
  - ['John Dewey (@retr0h)']
