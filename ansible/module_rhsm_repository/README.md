# Ansible module: ansible.module_rhsm_repository


Manage RHSM repositories using the subscription-manager command

## Description

Manage(Enable/Disable) RHSM repositories to the Red Hat Subscription Management entitlement platform using the C(subscription-manager) command.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The ID of repositories to enable.', 'To operate on several repositories this can accept a comma separated list or a YAML list.'], 'required': True}",
    "state": "{'description': ['If state is equal to present or disabled, indicates the desired repository state.'], 'choices': ['present', 'enabled', 'absent', 'disabled'], 'required': True, 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Enable a RHSM repository
  rhsm_repository:
    name: rhel-7-server-rpms

- name: Disable all RHSM repositories
  rhsm_repository:
    name: '*'
    state: disabled

- name: Enable all repositories starting with rhel-6-server
  rhsm_repository:
    name: rhel-6-server*
    state: enabled

- name: Disable all repositories except rhel-7-server-rpms
  rhsm_repository:
    name: "{{ item }}"
    state: disabled
  with_items: "{{
    rhsm_repository.repositories |
    map(attribute='id') |
    difference(['rhel-7-server-rpms']) }}"

```

## License

TODO

## Author Information
  - ['Giovanni Sciortino (@giovannisciortino)']
