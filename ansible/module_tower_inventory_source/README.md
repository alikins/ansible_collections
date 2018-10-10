# Ansible module: ansible.module_tower_inventory_source


create, update, or destroy Ansible Tower inventory source

## Description

Create, update, or destroy Ansible Tower inventories source. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "credential": "{'description': ['Credential to use to retrieve the inventory from.']}",
    "description": "{'description': ['The description to use for the inventory source.']}",
    "group_by": "{'description': ['Specify which groups to create automatically. Group names will be created similar to the options selected. If blank, all groups above are created. Refer to Ansible Tower documentation for more detail.']}",
    "instance_filters": "{'description': ['Provide a comma-separated list of filter expressions. Hosts are imported when all of the filters match. Refer to Ansible Tower documentation for more detail.']}",
    "inventory": "{'description': ['The inventory the source is linked to.'], 'required': True}",
    "name": "{'description': ['The name to use for the inventory source.'], 'required': True}",
    "overwrite": "{'description': ['If set, any hosts and groups that were previously present on the external source but are now removed will be removed from the Tower inventory. Hosts and groups that were not managed by the inventory source will be promoted to the next manually created group or if there is no manually created group to promote them into, they will be left in the "all" default group for the inventory. When not checked, local child hosts and groups not found on the external source will remain untouched by the inventory update process.'], 'type': 'bool'}",
    "overwrite_vars": "{'description': ['If set, all variables for child groups and hosts will be removed and replaced by those found on the external source. When not checked, a merge will be performed, combining local variables with those found on the external source.'], 'type': 'bool'}",
    "source": "{'description': ['Types of inventory source.'], 'choices': ['file', 'scm', 'ec2', 'gce', 'azure', 'azure_rm', 'vmware', 'satellite6', 'cloudforms', 'openstack', 'rhv', 'tower', 'custom'], 'required': True}",
    "source_path": "{'description': ['Path to the file to use as a source in the selected *project*.']}",
    "source_project": "{'description': ['Use a *project* as a source for the *inventory*.']}",
    "source_regions": "{'description': ['List of regions for your cloud provider. You can include multiple all regions. Only Hosts associated with the selected regions will be updated. Refer to Ansible Tower documentation for more detail.']}",
    "source_script": "{'description': ['The source custom script to use to build the inventory. It needs to exist.']}",
    "source_vars": "{'description': ['The source_vars allow to Override variables found in the source config file. For example with Openstack, specifying *private: false* would change the output of the openstack.py script. It has to be YAML or JSON.']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['Number in seconds after which the Tower API methods will time out.']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Tower option to avoid certificates check.'], 'type': 'bool', 'default': True}",
    "update_cache_timeout": "{'description': ['Time in seconds to consider an inventory sync to be current. During job runs and callbacks the task system will evaluate the timestamp of the latest sync. If it is older than Cache Timeout, it is not considered current, and a new inventory sync will be performed.']}",
    "update_on_launch": "{'description': ['Each time a job runs using this inventory, refresh the inventory from the selected source before executing job tasks.'], 'type': 'bool'}",
    "update_on_project_update": "{'description': ['That parameter will sync the inventory when the project is synced. It can only be used with a SCM source.'], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Add tower inventory source
  tower_inventory_source:
    name: Inventory source
    description: My Inventory source
    inventory: My inventory
    credential: Devstack_credential
    source: openstack
    update_on_launch: true
    overwrite: true
    source_vars: '{ private: false }'
    state: present
    tower_verify_ssl: false

```

## License

TODO

## Author Information
  - ['Adrien Fleury (@fleu42)']
