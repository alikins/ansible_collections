# Ansible module: ansible.module_tower_host


create, update, or destroy Ansible Tower host

## Description

Create, update, or destroy Ansible Tower hosts. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description to use for the host.']}",
    "enabled": "{'description': ['If the host should be enabled.'], 'type': 'bool', 'default': True}",
    "inventory": "{'description': ['Inventory the host should be made a member of.'], 'required': True}",
    "name": "{'description': ['The name to use for the host.'], 'required': True}",
    "state": "{'description': ['Desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "variables": "{'description': ['Variables to use for the host. Use C(@) for a file.']}",
}
```

## Examples


``` yaml

- name: Add tower host
  tower_host:
    name: localhost
    description: "Local Host Group"
    inventory: "Local Inventory"
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
