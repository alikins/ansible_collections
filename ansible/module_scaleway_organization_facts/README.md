# Ansible module: ansible.module_scaleway_organization_facts


Gather facts about the Scaleway organizations available

## Description

Gather facts about the Scaleway organizations available.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://account.scaleway.com', 'aliases': ['base_url']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather Scaleway organizations facts
  scaleway_organization_facts:

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
