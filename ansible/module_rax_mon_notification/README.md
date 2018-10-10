# Ansible module: ansible.module_rax_mon_notification


Create or delete a Rackspace Cloud Monitoring notification

## Description

Create or delete a Rackspace Cloud Monitoring notification that specifies a channel that can be used to communicate alarms, such as email, webhooks, or PagerDuty. Rackspace monitoring module flow | rax_mon_entity -> rax_mon_check -> *rax_mon_notification* -> rax_mon_notification_plan -> rax_mon_alarm

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "details": "{'description': ['Dictionary of key-value pairs used to initialize the notification. Required keys and meanings vary with notification type. See http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/ service-notification-types-crud.html for details.'], 'required': True}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "label": "{'description': ['Defines a friendly name for this notification. String between 1 and 255 characters long.'], 'required': True}",
    "notification_type": "{'description': ['A supported notification type.'], 'choices': ['webhook', 'email', 'pagerduty'], 'required': True}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Ensure that the notification with this C(label) exists or does not exist.'], 'choices': ['present', 'absent']}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Monitoring notification example
  gather_facts: False
  hosts: local
  connection: local
  tasks:
  - name: Email me when something goes wrong.
    rax_mon_entity:
      credentials: ~/.rax_pub
      label: omg
      type: email
      details:
        address: me@mailhost.com
    register: the_notification

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
