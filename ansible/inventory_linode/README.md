# Ansible inventory: ansible.inventory_linode


Ansible dynamic inventory plugin for Linode

## Description

Reads inventories from the Linode API v4.
Uses a C(<name>.linode.yaml) (or C(<name>.linode.yml)) YAML configuration file.
Linode labels are used by default as the hostnames.
The inventory groups are built from groups and not tags.

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ['The Linode account personal access token.'], 'required': True, 'env': [{'name': 'LINODE_ACCESS_TOKEN'}]}",
    "plugin": "{'description': ["marks this as an instance of the 'linode' plugin"], 'required': True, 'choices': ['linode']}",
    "regions": "{'description': ['Populate inventory with instances in this region.'], 'default': [], 'type': 'list', 'required': False}",
    "types": "{'description': ['Populate inventory with instances with this type.'], 'default': [], 'type': 'list', 'required': False}",
}
```

## Examples


``` yaml

# Minimal example. `LINODE_ACCESS_TOKEN` is exposed in environment.
plugin: linode

# Example with regions, types, groups and access token
plugin: linode
access_token: foobar
regions:
  - eu-west
types:
  - g5-standard-2

```

## License

TODO

## Author Information
  - ['UNKNOWN']
