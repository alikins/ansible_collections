# Ansible module: ansible.module_online_user_facts


Gather facts about Online user

## Description

Gather facts about the user.

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

- name: Gather Online user facts
  online_user_facts:

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
