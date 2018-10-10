# Ansible module: ansible.module_tower_team


create, update, or destroy Ansible Tower team

## Description

Create, update, or destroy Ansible Tower teams. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name to use for the team.'], 'required': True}",
    "organization": "{'description': ['Organization the team should be made a member of.'], 'required': True}",
    "state": "{'description': ['Desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create tower team
  tower_team:
    name: Team Name
    description: Team Description
    organization: test-org
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
