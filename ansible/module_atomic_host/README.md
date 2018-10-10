# Ansible module: ansible.module_atomic_host


Manage the atomic host platform

## Description

Manage the atomic host platform.
Rebooting of Atomic host platform should be done outside this module.

## Requirements

TODO

## Arguments

``` json
{
    "revision": "{'description': ['The version number of the atomic host to be deployed. Providing C(latest) will upgrade to the latest available version.'], 'default': 'latest', 'aliases': ['version']}",
}
```

## Examples


``` yaml

- name: Upgrade the atomic host platform to the latest version (atomic host upgrade)
  atomic_host:
    revision: latest

- name: Deploy a specific revision as the atomic host (atomic host deploy 23.130)
  atomic_host:
    revision: 23.130

```

## License

TODO

## Author Information
  - ['Saravanan KR (@krsacme)']
