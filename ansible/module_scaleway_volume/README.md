# Ansible module: ansible.module_scaleway_volume


Scaleway volumes management module

## Description

This module manages volumes on Scaleway account U(https://developer.scaleway.com)

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "name": "{'description': ['Name used to identify the volume.'], 'required': True}",
    "organization": "{'description': ['ScaleWay organization ID to which volume belongs.']}",
    "region": "{'description': ['Scaleway region to use (for example par1).'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "size": "{'description': ['Size of the volume in bytes.']}",
    "state": "{'description': ['Indicate desired state of the volume.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
    "volume_type": "{'description': ["Type of the volume (for example 'l_ssd')."]}",
}
```

## Examples


``` yaml

  - name: Create 10GB volume
    scaleway_volume:
      name: my-volume
      state: present
      region: par1
      organization: "{{ scw_org }}"
      "size": 10000000000
      volume_type: l_ssd
    register: server_creation_check_task

  - name: Make sure volume deleted
    scaleway_volume:
      name: my-volume
      state: absent
      region: par1


```

## License

TODO

## Author Information
  - ['Henryk Konsek (@hekonsek)']
