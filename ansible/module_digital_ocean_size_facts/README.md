# Ansible module: ansible.module_digital_ocean_size_facts


Gather facts about DigitalOcean Droplet sizes

## Description

This module can be used to gather facts about droplet sizes.

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

- name: Gather facts about all droplet sizes
  digital_ocean_size_facts:
    oauth_token: "{{ oauth_token }}"

- name: Get droplet Size Slug where vcpus is 1
  digital_ocean_size_facts:
    oauth_token: "{{ oauth_token }}"
  register: resp_out
- debug: var=resp_out
- set_fact:
    size_slug: "{{ item.slug }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?vcpus==`1`]"
- debug: var=size_slug



```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
