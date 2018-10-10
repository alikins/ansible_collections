# Ansible module: ansible.module_scaleway_ip


Scaleway IP management module

## Description

This module manages IP on Scaleway account U(https://developer.scaleway.com)

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "id": "{'description': ['id of the Scaleway IP (UUID)']}",
    "organization": "{'description': ['Scaleway organization identifier'], 'required': True}",
    "region": "{'description': ['Scaleway region to use (for example par1).'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "reverse": "{'description': ['Reverse to assign to the IP']}",
    "server": "{'description': ['id of the server you want to attach an IP to.', "To unattach an IP don't specify this option"]}",
    "state": "{'description': ['Indicate desired state of the IP.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

  - name: Create an IP
    scaleway_ip:
      organization: '{{ scw_org }}'
      state: present
      region: par1
    register: ip_creation_task

  - name: Make sure IP deleted
    scaleway_ip:
      id: '{{ ip_creation_task.scaleway_ip.id }}'
      state: absent
      region: par1


```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
