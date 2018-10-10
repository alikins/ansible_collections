# Ansible module: ansible.module_tower_inventory


create, update, or destroy Ansible Tower inventory

## Description

Create, update, or destroy Ansible Tower inventories. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description to use for the inventory.']}",
    "host_filter": "{'description': ['The host_filter field. Only useful when C(kind=smart).'], 'version_added': '2.7'}",
    "kind": "{'description': ['The kind field. Cannot be modified after created.'], 'default': '', 'choices': ['', 'smart'], 'version_added': '2.7'}",
    "name": "{'description': ['The name to use for the inventory.'], 'required': True}",
    "organization": "{'description': ['Organization the inventory belongs to.'], 'required': True}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "variables": "{'description': ['Inventory variables. Use C(@) to get from file.']}",
}
```

## Examples


``` yaml

- name: Add tower inventory
  tower_inventory:
    name: "Foo Inventory"
    description: "Our Foo Cloud Servers"
    organization: "Bar Org"
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
