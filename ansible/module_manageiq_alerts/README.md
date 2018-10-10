# Ansible module: ansible.module_manageiq_alerts


Configuration of alerts in ManageIQ

## Description

The manageiq_alerts module supports adding, updating and deleting alerts in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The unique alert description in ManageIQ.', 'Required when state is "absent" or "present".']}",
    "enabled": "{'description': ['Enable or disable the alert. Required if state is "present".'], 'type': 'bool'}",
    "expression": "{'description': ['The alert expression for ManageIQ.', 'Can either be in the "Miq Expression" format or the "Hash Expression format".', 'Required if state is "present".']}",
    "expression_type": "{'description': ['Expression type.'], 'default': 'hash', 'choices': ['hash', 'miq']}",
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "options": "{'description': ['Additional alert options, such as notification type and frequency']}",
    "resource_type": "{'description': ['The entity type for the alert in ManageIQ. Required when state is "present".'], 'choices': ['Vm', 'ContainerNode', 'MiqServer', 'Host', 'Storage', 'EmsCluster', 'ExtManagementSystem', 'MiddlewareServer']}",
    "state": "{'description': ['absent - alert should not exist,', 'present - alert should exist,'], 'required': False, 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add an alert with a "hash expression" to ManageIQ
  manageiq_alerts:
    state: present
    description: Test Alert 01
    options:
      notifications:
        email:
          to: ["example@example.com"]
          from: "example@example.com"
    resource_type: ContainerNode
    expression:
        eval_method: hostd_log_threshold
        mode: internal
        options: {}
    enabled: true
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Add an alert with a "miq expression" to ManageIQ
  manageiq_alerts:
    state: present
    description: Test Alert 02
    options:
      notifications:
        email:
          to: ["example@example.com"]
          from: "example@example.com"
    resource_type: Vm
    expression_type: miq
    expression:
        and:
          - CONTAINS:
              tag: Vm.managed-environment
              value: prod
          - not:
            CONTAINS:
              tag: Vm.host.managed-environment
              value: prod
    enabled: true
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Delete an alert from ManageIQ
  manageiq_alerts:
    state: absent
    description: Test Alert 01
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
