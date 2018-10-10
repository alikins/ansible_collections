# Ansible module: ansible.module_online_server_facts


Gather facts about Online servers

## Description

Gather facts about the servers.
U(https://www.online.net/en/dedicated-server)

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Online API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Online OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Online API URL'], 'default': 'https://api.online.net', 'aliases': ['base_url']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Online API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather Online server facts
  online_server_facts:
    api_token: '0d1627e8-bbf0-44c5-a46f-5c4d3aef033f'

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
