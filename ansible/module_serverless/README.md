# Ansible module: ansible.module_serverless


Manages a Serverless Framework project

## Description

Provides support for managing Serverless Framework (https://serverless.com/) project deployments and stacks.

## Requirements

TODO

## Arguments

``` json
{
    "deploy": "{'description': ['Whether or not to deploy artifacts after building them. When this option is `false` all the functions will be built, but no stack update will be run to send them out. This is mostly useful for generating artifacts to be stored/deployed elsewhere.'], 'required': False, 'default': True}",
    "force": "{'description': ['Whether or not to force full deployment, equivalent to serverless `--force` option.'], 'required': False, 'default': False, 'version_added': '2.7'}",
    "functions": "{'description': ['A list of specific functions to deploy. If this is not provided, all functions in the service will be deployed.'], 'required': False, 'default': []}",
    "region": "{'description': ['AWS region to deploy the service to'], 'required': False, 'default': 'us-east-1'}",
    "serverless_bin_path": "{'description': ["The path of a serverless framework binary relative to the 'service_path' eg. node_module/.bin/serverless"], 'required': False, 'version_added': '2.4'}",
    "service_path": "{'description': ['The path to the root of the Serverless Service to be operated on.'], 'required': True}",
    "stage": "{'description': ['The name of the serverless framework project stage to deploy to. This uses the serverless framework default "dev".'], 'required': False}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Goal state of given stage/project'], 'required': False, 'default': 'present'}",
    "verbose": "{'description': ['Shows all stack events during deployment, and display any Stack Output.'], 'required': False, 'default': False, 'version_added': '2.7'}",
}
```

## Examples


``` yaml

# Basic deploy of a service
- serverless:
    service_path: '{{ project_dir }}'
    state: present

# Deploy specific functions
- serverless:
    service_path: '{{ project_dir }}'
    functions:
      - my_func_one
      - my_func_two

# deploy a project, then pull its resource list back into Ansible
- serverless:
    stage: dev
    region: us-east-1
    service_path: '{{ project_dir }}'
  register: sls
# The cloudformation stack is always named the same as the full service, so the
# cloudformation_facts module can get a full list of the stack resources, as
# well as stack events and outputs
- cloudformation_facts:
    region: us-east-1
    stack_name: '{{ sls.service_name }}'
    stack_resources: true

# Deploy a project but use a locally installed serverless binary instead of the global serverless binary
- serverless:
    stage: dev
    region: us-east-1
    service_path: '{{ project_dir }}'
    serverless_bin_path: node_modules/.bin/serverless

```

## License

TODO

## Author Information
  - ['Ryan Scott Brown (@ryansb)']
