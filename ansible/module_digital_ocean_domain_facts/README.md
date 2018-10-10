# Ansible module: ansible.module_digital_ocean_domain_facts


Gather facts about DigitalOcean Domains

## Description

This module can be used to gather facts about DigitalOcean provided Domains.

## Requirements

TODO

## Arguments

``` json
{
    "domain_name": "{'description': ['Name of the domain to gather facts for.'], 'required': False}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all domains
  digital_ocean_domain_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about domain with given name
  digital_ocean_domain_facts:
    oauth_token: "{{ oauth_token }}"
    domain_name: "example.com"

- name: Get ttl from domain
  digital_ocean_domain_facts:
  register: resp_out
- set_fact:
    domain_ttl: "{{ item.ttl }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?name=='example.com']"
- debug: var=domain_ttl

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
