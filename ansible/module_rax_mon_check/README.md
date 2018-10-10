# Ansible module: ansible.module_rax_mon_check


Create or delete a Rackspace Cloud Monitoring check for an existing entity

## Description

Create or delete a Rackspace Cloud Monitoring check associated with an existing rax_mon_entity. A check is a specific test or measurement that is performed, possibly from different monitoring zones, on the systems you monitor. Rackspace monitoring module flow | rax_mon_entity -> *rax_mon_check* -> rax_mon_notification -> rax_mon_notification_plan -> rax_mon_alarm

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "check_type": "{'description': ['The type of check to create. C(remote.) checks may be created on any rax_mon_entity. C(agent.) checks may only be created on rax_mon_entities that have a non-null C(agent_id).'], 'choices': ['remote.dns', 'remote.ftp-banner', 'remote.http', 'remote.imap-banner', 'remote.mssql-banner', 'remote.mysql-banner', 'remote.ping', 'remote.pop3-banner', 'remote.postgresql-banner', 'remote.smtp-banner', 'remote.smtp', 'remote.ssh', 'remote.tcp', 'remote.telnet-banner', 'agent.filesystem', 'agent.memory', 'agent.load_average', 'agent.cpu', 'agent.disk', 'agent.network', 'agent.plugin'], 'required': True}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "details": "{'description': ['Additional details specific to the check type. Must be a hash of strings between 1 and 255 characters long, or an array or object containing 0 to 256 items.']}",
    "disabled": "{'description': ['If "yes", ensure the check is created, but don\'t actually use it yet.'], 'type': 'bool'}",
    "entity_id": "{'description': ['ID of the rax_mon_entity to target with this check.'], 'required': True}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "label": "{'description': ['Defines a label for this check, between 1 and 64 characters long.'], 'required': True}",
    "metadata": "{'description': ['Hash of arbitrary key-value pairs to accompany this check if it fires. Keys and values must be strings between 1 and 255 characters long.']}",
    "monitoring_zones_poll": "{'description': ['Comma-separated list of the names of the monitoring zones the check should run from. Available monitoring zones include mzdfw, mzhkg, mziad, mzlon, mzord and mzsyd. Required for remote.* checks; prohibited for agent.* checks.']}",
    "period": "{'description': ['The number of seconds between each time the check is performed. Must be greater than the minimum period set on your account.']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Ensure that a check with this C(label) exists or does not exist.'], 'choices': ['present', 'absent']}",
    "target_alias": "{'description': ["One of `target_alias` and `target_hostname` is required for remote.* checks, but prohibited for agent.* checks. Use the corresponding key in the entity's `ip_addresses` hash to resolve an IP address to target."]}",
    "target_hostname": "{'description': ['One of `target_hostname` and `target_alias` is required for remote.* checks, but prohibited for agent.* checks. The hostname this check should target. Must be a valid IPv4, IPv6, or FQDN.']}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "timeout": "{'description': ['The number of seconds this check will wait when attempting to collect results. Must be less than the period.']}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Create a monitoring check
  gather_facts: False
  hosts: local
  connection: local
  tasks:
  - name: Associate a check with an existing entity.
    rax_mon_check:
      credentials: ~/.rax_pub
      state: present
      entity_id: "{{ the_entity['entity']['id'] }}"
      label: the_check
      check_type: remote.ping
      monitoring_zones_poll: mziad,mzord,mzdfw
      details:
        count: 10
      meta:
        hurf: durf
    register: the_check

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
