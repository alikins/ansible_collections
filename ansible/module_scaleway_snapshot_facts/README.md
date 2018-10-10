# Ansible module: ansible.module_scaleway_snapshot_facts


Gather facts about the Scaleway snapshots available

## Description

Gather facts about the Scaleway snapshot available.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "region": "{'version_added': '2.8', 'description': ['Scaleway region to use (for example par1).'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather Scaleway snapshots facts
  scaleway_snapshot_facts:
    region: par1

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
  - ['Yanis Guenane (@Spredzy)', 'Remy Leone (@sieben)']
