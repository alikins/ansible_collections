# Ansible module: ansible.module_sensu_subscription


Manage Sensu subscriptions

## Description

Manage which I(sensu channels) a machine should subscribe to

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['Create a backup file (if yes), including the timestamp information so you', 'can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'required': False, 'default': False}",
    "name": "{'description': ['The name of the channel'], 'required': True}",
    "path": "{'description': ['Path to the subscriptions json file'], 'required': False, 'default': '/etc/sensu/conf.d/subscriptions.json'}",
    "state": "{'description': ['Whether the machine should subscribe or unsubscribe from the channel'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
}
```

## Examples


``` yaml

# Subscribe to the nginx channel
- name: subscribe to nginx checks
  sensu_subscription: name=nginx

# Unsubscribe from the common checks channel
- name: unsubscribe from common checks
  sensu_subscription: name=common state=absent

```

## License

TODO

## Author Information
  - ['Anders Ingemann (@andsens)']
