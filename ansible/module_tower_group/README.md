# Ansible module: ansible.module_tower_group


create, update, or destroy Ansible Tower group

## Description

Create, update, or destroy Ansible Tower groups. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "credential": "{'description': ['Credential to use for the group.']}",
    "description": "{'description': ['The description to use for the group.']}",
    "group_by": "{'description': ['Limit groups automatically created from inventory source.']}",
    "instance_filters": "{'description': ['Comma-separated list of filter expressions for matching hosts.']}",
    "inventory": "{'description': ['Inventory the group should be made a member of.'], 'required': True}",
    "name": "{'description': ['The name to use for the group.'], 'required': True}",
    "overwrite": "{'description': ['Delete child groups and hosts not found in source.'], 'type': 'bool', 'default': False}",
    "overwrite_vars": "{'description': ['Override vars in child groups and hosts with those from external source.']}",
    "source": "{'description': ['The source to use for this group.'], 'choices': ['manual', 'file', 'ec2', 'rax', 'vmware', 'gce', 'azure', 'azure_rm', 'openstack', 'satellite6', 'cloudforms', 'custom']}",
    "source_regions": "{'description': ['Regions for cloud provider.']}",
    "source_script": "{'description': ['Inventory script to be used when group type is C(custom).']}",
    "source_vars": "{'description': ['Override variables from source with variables from this field.']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "update_on_launch": "{'description': ['Refresh inventory data from its source each time a job is run.'], 'type': 'bool', 'default': False}",
    "variables": "{'description': ['Variables to use for the group, use C(@) for a file.']}",
}
```

## Examples


``` yaml

- name: Add tower group
  tower_group:
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
