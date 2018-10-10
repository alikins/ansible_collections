# Ansible module: ansible.module_tower_settings


Modify Ansible Tower settings

## Description

Get, Modify Ansible Tower settings. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of setting to get/modify']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "value": "{'description': ['Value to be modified for given setting.']}",
}
```

## Examples


``` yaml

- name: Set the value of AWX_PROOT_BASE_PATH
  tower_settings:
    name: AWX_PROOT_BASE_PATH
    value: "/tmp"
  register: testing_settings

- name: Set the value of AWX_PROOT_SHOW_PATHS
  tower_settings:
    name: "AWX_PROOT_SHOW_PATHS"
    value: "'/var/lib/awx/projects/', '/tmp'"
  register: testing_settings

- name: Set the LDAP Auth Bind Password
  tower_settings:
    name: "AUTH_LDAP_BIND_PASSWORD"
    value: "Password"
  no_log: true

```

## License

TODO

## Author Information
  - ['Nikhil Jain (@jainnikhil30)']
