# Ansible module: ansible.module_sensu_silence


Manage Sensu silence entries

## Description

Create and clear (delete) a silence entries via the Sensu API for subscriptions and checks.

## Requirements

TODO

## Arguments

``` json
{
    "check": "{'description': ['Specifies the check which the silence entry applies to.']}",
    "creator": "{'description': ['Specifies the entity responsible for this entry.']}",
    "expire": "{'description': ['If specified, the silence entry will be automatically cleared after this number of seconds.']}",
    "expire_on_resolve": "{'description': ['If specified as true, the silence entry will be automatically cleared once the condition it is silencing is resolved.'], 'type': 'bool'}",
    "reason": "{'description': ['If specified, this free-form string is used to provide context or rationale for the reason this silence entry was created.']}",
    "state": "{'description': ['Specifies to create or clear (delete) a silence entry via the Sensu API'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription": "{'description': ['Specifies the subscription which the silence entry applies to.', 'To create a silence entry for a client prepend C(client:) to client name. Example - C(client:server1.example.dev)'], 'required': True, 'default': []}",
    "url": "{'description': ['Specifies the URL of the Sensu monitoring host server.'], 'required': False, 'default': 'http://127.0.01:4567'}",
}
```

## Examples


``` yaml

# Silence ALL checks for a given client
- name: Silence server1.example.dev
  sensu_silence:
    subscription: client:server1.example.dev
    creator: "{{ ansible_user_id }}"
    reason: Performing maintenance

# Silence specific check for a client
- name: Silence CPU_Usage check for server1.example.dev
  sensu_silence:
    subscription: client:server1.example.dev
    check: CPU_Usage
    creator: "{{ ansible_user_id }}"
    reason: Investigation alert issue

# Silence multiple clients from a dict
  silence:
    server1.example.dev:
      reason: 'Deployment in progress'
    server2.example.dev:
      reason: 'Deployment in progress'

- name: Silence several clients from a dict
  sensu_silence:
    subscription: "client:{{ item.key }}"
    reason: "{{ item.value.reason }}"
    creator: "{{ ansible_user_id }}"
  with_dict: "{{ silence }}"

```

## License

TODO

## Author Information
  - ['Steven Bambling (@smbambling)']
