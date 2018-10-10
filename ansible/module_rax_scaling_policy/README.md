# Ansible module: ansible.module_rax_scaling_policy


Manipulate Rackspace Cloud Autoscale Scaling Policy

## Description

Manipulate Rackspace Cloud Autoscale Scaling Policy

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "at": "{'description': ["The UTC time when this policy will be executed. The time must be formatted according to C(yyyy-MM-dd'T'HH:mm:ss.SSS) such as C(2013-05-19T08:07:08Z)"]}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "change": "{'description': ['The change, either as a number of servers or as a percentage, to make in the scaling group. If this is a percentage, you must set I(is_percent) to C(true) also.']}",
    "cooldown": "{'description': ['The period of time, in seconds, that must pass before any scaling can occur after the previous scaling. Must be an integer between 0 and 86400 (24 hrs).']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "cron": "{'description': ['The time when the policy will be executed, as a cron entry. For example, if this is parameter is set to C(1 0 * * *)']}",
    "desired_capacity": "{'description': ['The desired server capacity of the scaling the group; that is, how many servers should be in the scaling group.']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "is_percent": "{'description': ['Whether the value in I(change) is a percent value'], 'default': False}",
    "name": "{'description': ['Name to give the policy'], 'required': True}",
    "policy_type": "{'description': ['The type of policy that will be executed for the current release.'], 'choices': ['webhook', 'schedule'], 'required': True}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "scaling_group": "{'description': ['Name of the scaling group that this policy will be added to'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        at: '2013-05-19T08:07:08Z'
        change: 25
        cooldown: 300
        is_percent: true
        name: ASG Test Policy - at
        policy_type: schedule
        scaling_group: ASG Test
      register: asps_at

    - rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        cron: '1 0 * * *'
        change: 25
        cooldown: 300
        is_percent: true
        name: ASG Test Policy - cron
        policy_type: schedule
        scaling_group: ASG Test
      register: asp_cron

    - rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        cooldown: 300
        desired_capacity: 5
        name: ASG Test Policy - webhook
        policy_type: webhook
        scaling_group: ASG Test
      register: asp_webhook

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
