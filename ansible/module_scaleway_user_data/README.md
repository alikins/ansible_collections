# Ansible module: ansible.module_scaleway_user_data


Scaleway user_data management module

## Description

This module manages user_data on compute instances on Scaleway.
It can be used to configure cloud-init for instance

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "region": "{'description': ['Scaleway compute zone'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "server_id": "{'description': ['Scaleway Compute instance ID of the server'], 'required': True}",
    "user_data": "{'description': ['User defined data. Typically used with `cloud-init`.', 'Pass your cloud-init script here as a string'], 'required': False}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Update the cloud-init
  scaleway_user_data:
    server_id: '5a33b4ab-57dd-4eb6-8b0a-d95eb63492ce'
    region: ams1
    user_data:
      cloud-init: 'final_message: "Hello World!"'

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
