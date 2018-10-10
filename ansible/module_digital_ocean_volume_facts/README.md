# Ansible module: ansible.module_digital_ocean_volume_facts


Gather facts about DigitalOcean volumes

## Description

This module can be used to gather facts about DigitalOcean provided volumes.

## Requirements

TODO

## Arguments

``` json
{
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "region_name": "{'description': ['Name of region to restrict results to volumes available in a specific region.', 'Please use M(digital_ocean_region_facts) for getting valid values related regions.'], 'required': False}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all volume
  digital_ocean_volume_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about volume in given region
  digital_ocean_volume_facts:
    region_name: nyc1
    oauth_token: "{{ oauth_token }}"

- name: Get facts about volume named nyc3-test-volume
  digital_ocean_volume_facts:
  register: resp_out
- set_fact:
    volume_id: "{{ item.id }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?name=='nyc3-test-volume']"
- debug: var=volume_id

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
