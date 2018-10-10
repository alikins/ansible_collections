# Ansible module: ansible.module_scaleway_image_facts


Gather facts about the Scaleway images available

## Description

Gather facts about the Scaleway images available.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "region": "{'version_added': '2.7', 'description': ['Scaleway compute zone'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather Scaleway images facts
  scaleway_image_facts:
    region: par1

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
