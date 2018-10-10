# Ansible module: ansible.module_tower_workflow_template


create, update, or destroy Ansible Tower workflow template

## Description

Create, update, or destroy Ansible Tower workflows. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "allow_simultaneous": "{'description': ['If enabled, simultaneous runs of this job template will be allowed.'], 'type': 'bool'}",
    "description": "{'description': ['The description to use for the workflow.']}",
    "extra_vars": "{'description': ['Extra variables used by Ansible in YAML or key=value format.']}",
    "name": "{'description': ['The name to use for the workflow.'], 'required': True}",
    "organization": "{'description': ['The organization the workflow is linked to.']}",
    "schema": "{'description': ['The schema is a JSON- or YAML-formatted string defining the hierarchy structure that connects the nodes. Refer to Tower documentation for more information.\n']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "survey": "{'description': ['The definition of the survey associated to the workflow.']}",
    "survey_enabled": "{'description': ['Setting that variable will prompt the user for job type on the workflow launch.'], 'type': 'bool'}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- tower_workflow_template:
    name: Workflow Template
    description: My very first Worflow Template
    organization: My optional Organization
    schema: "{{ lookup(file, my_workflow.json }}"

- tower_worflow_template:
    name: Workflow Template
    state: absent

```

## License

TODO

## Author Information
  - ['Adrien Fleury (@fleu42)']
