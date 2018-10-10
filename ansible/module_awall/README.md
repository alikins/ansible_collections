# Ansible module: ansible.module_awall


Manage awall policies

## Description

This modules allows for enable/disable/activate of I(awall) policies. Alpine Wall (I(awall)) generates a firewall configuration from the enabled policy files and activates the configuration on the system.

## Requirements

TODO

## Arguments

``` json
{
    "activate": "{'description': ["Activate the new firewall rules. Can be run with other steps or on it's own."], 'type': 'bool', 'default': False}",
    "name": "{'description': ['A policy name, like C(foo), or multiple policies, like C(foo, bar).']}",
    "state": "{'description': ['The policy(ies) will be C(enabled)', 'The policy(ies) will be C(disabled)'], 'default': 'enabled', 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Enable "foo" and "bar" policy
  awall:
    name: foo,bar
    state: enabled

- name: Disable "foo" and "bar" policy and activate new rules
  awall:
    name: foo,bar
    state: disabled
    activate: False

- name: Activate currently enabled firewall rules
  awall:
    activate: True

```

## License

TODO

## Author Information
  - ['Ted Trask (@tdtrask) <ttrask01@yahoo.com>']
