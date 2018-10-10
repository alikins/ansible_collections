# Ansible module: ansible.module_tower_organization


create, update, or destroy Ansible Tower organizations

## Description

Create, update, or destroy Ansible Tower organizations. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description to use for the organization.']}",
    "name": "{'description': ['Name to use for the organization.'], 'required': True}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create tower organization
  tower_organization:
    name: "Foo"
    description: "Foo bar organization"
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
