# Ansible module: ansible.module_gcspanner


Create and Delete Instances/Databases on Spanner

## Description

Create and Delete Instances/Databases on Spanner. See U(https://cloud.google.com/spanner/docs) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "configuration": "{'description': ['Configuration the instance should use.', 'Examples are us-central1, asia-east1 and europe-west1.'], 'required': True}",
    "database_name": "{'description': ['Name of database contained on the instance.']}",
    "force_instance_delete": "{'description': ['To delete an instance, this argument must exist and be true (along with state being equal to absent).'], 'type': 'bool', 'default': False}",
    "instance_display_name": "{'description': ['Name of Instance to display.', 'If not specified, instance_id will be used instead.']}",
    "instance_id": "{'description': ['GCP spanner instance name.'], 'required': True}",
    "node_count": "{'description': ['Number of nodes in the instance.'], 'default': 1}",
    "state": "{'description': ['State of the instance or database. Applies to the most granular resource.', 'If a C(database_name) is specified we remove it.', 'If only C(instance_id) is specified, that is what is removed.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Create instance
  gcspanner:
    instance_id: '{{ instance_id }}'
    configuration: '{{ configuration }}'
    state: present
    node_count: 1

- name: Create database
  gcspanner:
    instance_id: '{{ instance_id }}'
    configuration: '{{ configuration }}'
    database_name: '{{ database_name }}'
    state: present

- name: Delete instance (and all databases)
- gcspanner:
    instance_id: '{{ instance_id }}'
    configuration: '{{ configuration }}'
    state: absent
    force_instance_delete: yes

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
