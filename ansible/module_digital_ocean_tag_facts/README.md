# Ansible module: ansible.module_digital_ocean_tag_facts


Gather facts about DigitalOcean tags

## Description

This module can be used to gather facts about DigitalOcean provided tags.

## Requirements

TODO

## Arguments

``` json
{
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "tag_name": "{'description': ['Tag name that can be used to identify and reference a tag.'], 'required': False}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all tags
  digital_ocean_tag_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about tag with given name
  digital_ocean_tag_facts:
    oauth_token: "{{ oauth_token }}"
    tag_name: "extra_awesome_tag"

- name: Get resources from tag name
  digital_ocean_tag_facts:
  register: resp_out
- set_fact:
    resources: "{{ item.resources }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?name=='extra_awesome_tag']"
- debug: var=resources

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
