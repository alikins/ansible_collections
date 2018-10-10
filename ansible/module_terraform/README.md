# Ansible module: ansible.module_terraform


Manages a Terraform deployment (and plans)

## Description

Provides support for deploying resources with Terraform and pulling resource information back into Ansible.

## Requirements

TODO

## Arguments

``` json
{
    "backend_config": "{'description': ['A group of key-values to provide at init stage to the -backend-config parameter.'], 'required': False, 'version_added': 2.7}",
    "binary_path": "{'description': ["The path of a terraform binary to use, relative to the 'service_path' unless you supply an absolute path."], 'required': False}",
    "force_init": "{'description': ["To avoid duplicating infra, if a state file can't be found this will force a `terraform init`. Generally, this should be turned off unless you intend to provision an entirely new Terraform deployment."], 'default': False, 'required': False, 'type': 'bool'}",
    "lock": "{'description': ['Enable statefile locking, if you use a service that accepts locks (such as S3+DynamoDB) to store your statefile.'], 'required': False}",
    "lock_timeout": "{'description': ['How long to maintain the lock on the statefile, if you use a service that accepts locks (such as S3+DynamoDB).'], 'required': False}",
    "plan_file": "{'description': ["The path to an existing Terraform plan file to apply. If this is not specified, Ansible will build a new TF plan and execute it. Note that this option is required if 'state' has the 'planned' value."], 'required': False}",
    "project_path": "{'description': ['The path to the root of the Terraform directory with the vars.tf/main.tf/etc to use.'], 'required': True}",
    "purge_workspace": "{'description': ['Only works with state = absent', 'If true, the workspace will be deleted after the "terraform destroy" action.', "The 'default' workspace will not be deleted."], 'required': False, 'default': False, 'type': 'bool', 'version_added': 2.7}",
    "state": "{'choices': ['planned', 'present', 'absent'], 'description': ['Goal state of given stage/project'], 'required': False, 'default': 'present'}",
    "state_file": "{'description': ['The path to an existing Terraform state file to use when building plan. If this is not specified, the default `terraform.tfstate` will be used.', 'This option is ignored when plan is specified.'], 'required': False}",
    "targets": "{'description': ['A list of specific resources to target in this plan/application. The resources selected here will also auto-include any dependencies.'], 'required': False}",
    "variables": "{'description': ['A group of key-values to override template variables or those in variables files.'], 'required': False}",
    "variables_file": "{'description': ['The path to a variables file for Terraform to fill into the TF configurations.'], 'required': False}",
    "workspace": "{'description': ['The terraform workspace to work with.'], 'required': False, 'default': 'default', 'version_added': 2.7}",
}
```

## Examples


``` yaml

# Basic deploy of a service
- terraform:
    project_path: '{{ project_dir }}'
    state: present

# Define the backend configuration at init
- terraform:
    project_path: 'project/'
    state: "{{ state }}"
    force_init: true
    backend_config:
      region: "eu-west-1"
      bucket: "some-bucket"
      key: "random.tfstate"

```

## License

TODO

## Author Information
  - ['Ryan Scott Brown @ryansb']
