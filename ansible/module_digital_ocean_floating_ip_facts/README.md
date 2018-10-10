# Ansible module: ansible.module_digital_ocean_floating_ip_facts


DigitalOcean Floating IPs facts

## Description

This module can be used to fetch DigitalOcean Floating IPs facts.

## Requirements

TODO

## Arguments

``` json
{
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: "Gather facts about all Floating IPs"
  digital_ocean_floating_ip_facts:
  register: result

- name: "List of current floating ips"
  debug: var=result.floating_ips

```

## License

TODO

## Author Information
  - ['Patrick Marques (@pmarques)']
