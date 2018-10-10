# Ansible module: ansible.module_rax_mon_entity


Create or delete a Rackspace Cloud Monitoring entity

## Description

Create or delete a Rackspace Cloud Monitoring entity, which represents a device to monitor. Entities associate checks and alarms with a target system and provide a convenient, centralized place to store IP addresses. Rackspace monitoring module flow | *rax_mon_entity* -> rax_mon_check -> rax_mon_notification -> rax_mon_notification_plan -> rax_mon_alarm

## Requirements

TODO

## Arguments

``` json
{
    "agent_id": "{'description': ['Rackspace monitoring agent on the target device to which this entity is bound. Necessary to collect C(agent.) rax_mon_checks against this entity.']}",
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "label": "{'description': ['Defines a name for this entity. Must be a non-empty string between 1 and 255 characters long.'], 'required': True}",
    "metadata": "{'description': ['Hash of arbitrary C(name), C(value) pairs that are passed to associated rax_mon_alarms. Names and values must all be between 1 and 255 characters long.']}",
    "named_ip_addresses": "{'description': ['Hash of IP addresses that may be referenced by name by rax_mon_checks added to this entity. Must be a dictionary of with keys that are names between 1 and 64 characters long, and values that are valid IPv4 or IPv6 addresses.']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Ensure that an entity with this C(name) exists or does not exist.'], 'choices': ['present', 'absent']}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Entity example
  gather_facts: False
  hosts: local
  connection: local
  tasks:
  - name: Ensure an entity exists
    rax_mon_entity:
      credentials: ~/.rax_pub
      state: present
      label: my_entity
      named_ip_addresses:
        web_box: 192.0.2.4
        db_box: 192.0.2.5
      meta:
        hurf: durf
    register: the_entity

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
