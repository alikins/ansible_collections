# Ansible module: ansible.module_manageiq_alert_profiles


Configuration of alert profiles for ManageIQ

## Description

The manageiq_alert_profiles module supports adding, updating and deleting alert profiles in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "alerts": "{'description': ['List of alert descriptions to assign to this profile.', 'Required if state is "present"']}",
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "name": "{'description': ['The unique alert profile name in ManageIQ.', 'Required when state is "absent" or "present".']}",
    "notes": "{'description': ['Optional notes for this profile']}",
    "resource_type": "{'description': ['The resource type for the alert profile in ManageIQ. Required when state is "present".'], 'choices': ['Vm', 'ContainerNode', 'MiqServer', 'Host', 'Storage', 'EmsCluster', 'ExtManagementSystem', 'MiddlewareServer']}",
    "state": "{'description': ['absent - alert profile should not exist,', 'present - alert profile should exist,'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add an alert profile to ManageIQ
  manageiq_alert_profiles:
    state: present
    name: Test profile
    resource_type: ContainerNode
    alerts:
      - Test Alert 01
      - Test Alert 02
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Delete an alert profile from ManageIQ
  manageiq_alert_profiles:
    state: absent
    name: Test profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

```

## License

TODO

## Author Information
  - ['Elad Alfassa (ealfassa@redhat.com)']
