# Ansible module: ansible.module_rax_mon_alarm


Create or delete a Rackspace Cloud Monitoring alarm

## Description

Create or delete a Rackspace Cloud Monitoring alarm that associates an existing rax_mon_entity, rax_mon_check, and rax_mon_notification_plan with criteria that specify what conditions will trigger which levels of notifications. Rackspace monitoring module flow | rax_mon_entity -> rax_mon_check -> rax_mon_notification -> rax_mon_notification_plan -> *rax_mon_alarm*

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "check_id": "{'description': ['ID of the check that should be alerted on. May be acquired by registering the value of a rax_mon_check task.'], 'required': True}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "criteria": "{'description': ['Alarm DSL that describes alerting conditions and their output states. Must be between 1 and 16384 characters long. See http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/alerts-language.html for a reference on the alerting language.']}",
    "disabled": "{'description': ['If yes, create this alarm, but leave it in an inactive state. Defaults to no.'], 'type': 'bool'}",
    "entity_id": "{'description': ['ID of the entity this alarm is attached to. May be acquired by registering the value of a rax_mon_entity task.'], 'required': True}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "label": "{'description': ['Friendly name for this alarm, used to achieve idempotence. Must be a String between 1 and 255 characters long.'], 'required': True}",
    "metadata": "{'description': ['Arbitrary key/value pairs to accompany the alarm. Must be a hash of String keys and values between 1 and 255 characters long.']}",
    "notification_plan_id": "{'description': ['ID of the notification plan to trigger if this alarm fires. May be acquired by registering the value of a rax_mon_notification_plan task.'], 'required': True}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Ensure that the alarm with this C(label) exists or does not exist.'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Alarm example
  gather_facts: False
  hosts: local
  connection: local
  tasks:
  - name: Ensure that a specific alarm exists.
    rax_mon_alarm:
      credentials: ~/.rax_pub
      state: present
      label: uhoh
      entity_id: "{{ the_entity['entity']['id'] }}"
      check_id: "{{ the_check['check']['id'] }}"
      notification_plan_id: "{{ defcon1['notification_plan']['id'] }}"
      criteria: >
        if (rate(metric['average']) > 10) {
          return new AlarmStatus(WARNING);
        }
        return new AlarmStatus(OK);
    register: the_alarm

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
