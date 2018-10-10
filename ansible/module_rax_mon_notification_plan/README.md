# Ansible module: ansible.module_rax_mon_notification_plan


Create or delete a Rackspace Cloud Monitoring notification plan

## Description

Create or delete a Rackspace Cloud Monitoring notification plan by associating existing rax_mon_notifications with severity levels. Rackspace monitoring module flow | rax_mon_entity -> rax_mon_check -> rax_mon_notification -> *rax_mon_notification_plan* -> rax_mon_alarm

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "critical_state": "{'description': ['Notification list to use when the alarm state is CRITICAL. Must be an array of valid rax_mon_notification ids.']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "label": "{'description': ['Defines a friendly name for this notification plan. String between 1 and 255 characters long.'], 'required': True}",
    "ok_state": "{'description': ['Notification list to use when the alarm state is OK. Must be an array of valid rax_mon_notification ids.']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Ensure that the notification plan with this C(label) exists or does not exist.'], 'choices': ['present', 'absent']}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "warning_state": "{'description': ['Notification list to use when the alarm state is WARNING. Must be an array of valid rax_mon_notification ids.']}",
}
```

## Examples


``` yaml

- name: Example notification plan
  gather_facts: False
  hosts: local
  connection: local
  tasks:
  - name: Establish who gets called when.
    rax_mon_notification_plan:
      credentials: ~/.rax_pub
      state: present
      label: defcon1
      critical_state:
      - "{{ everyone['notification']['id'] }}"
      warning_state:
      - "{{ opsfloor['notification']['id'] }}"
    register: defcon1

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
