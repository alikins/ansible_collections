# Ansible module: ansible.module_scaleway_security_group


Scaleway Security Group management module

## Description

This module manages Security Group on Scaleway account U(https://developer.scaleway.com)

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "description": "{'description': ['Description of the Security Group']}",
    "inbound_default_policy": "{'description': ['Default policy for incoming trafic'], 'choices': ['accept', 'drop']}",
    "name": "{'description': ['Name of the Security Group'], 'required': True}",
    "organization": "{'description': ['Organization identifier'], 'required': True}",
    "organization_default": "{'type': 'bool', 'description': ['Create security group to be the default one']}",
    "outbound_default_policy": "{'description': ['Default policy for outcoming trafic'], 'choices': ['accept', 'drop']}",
    "region": "{'description': ['Scaleway region to use (for example C(par1)).'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "state": "{'description': ['Indicate desired state of the Security Group.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "stateful": "{'description': ['Create a stateful security group which allows established connections in and out'], 'required': True, 'type': 'bool'}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

  - name: Create a Security Group
    scaleway_security_group:
      state: present
      region: par1
      name: security_group
      description: "my security group description"
      organization: "43a3b6c8-916f-477b-b7ec-ff1898f5fdd9"
      stateful: false
      inbound_default_policy: accept
      outbound_default_policy: accept
      organization_default: false
    register: security_group_creation_task

```

## License

TODO

## Author Information
  - ['Antoine Barbare (@abarbare)']
