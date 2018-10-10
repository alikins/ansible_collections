# Ansible module: ansible.module_clc_blueprint_package


deploys a blue print package on a set of servers in CenturyLink Cloud

## Description

An Ansible module to deploy blue print package on a set of servers in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "package_id": "{'description': ['The package id of the blue print.'], 'required': True}",
    "package_params": "{'description': ['The dictionary of arguments required to deploy the blue print.'], 'default': {}, 'required': False}",
    "server_ids": "{'description': ['A list of server Ids to deploy the blue print package.'], 'required': True}",
    "state": "{'description': ['Whether to install or un-install the package. Currently it supports only "present" for install action.'], 'required': False, 'default': 'present', 'choices': ['present']}",
    "wait": "{'description': ['Whether to wait for the tasks to finish before returning.'], 'type': 'bool', 'default': True, 'required': False}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Deploy package
  clc_blueprint_package:
        server_ids:
            - UC1TEST-SERVER1
            - UC1TEST-SERVER2
        package_id: 77abb844-579d-478d-3955-c69ab4a7ba1a
        package_params: {}

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
