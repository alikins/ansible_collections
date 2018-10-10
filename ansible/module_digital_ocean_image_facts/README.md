# Ansible module: ansible.module_digital_ocean_image_facts


Gather facts about DigitalOcean images

## Description

This module can be used to gather facts about DigitalOcean provided images.
These images can be either of type C(distribution), C(application) and C(private).

## Requirements

TODO

## Arguments

``` json
{
    "image_type": "{'description': ['Specifies the type of image facts to be retrived.', 'If set to C(application), then facts are gathered related to all application images.', 'If set to C(distribution), then facts are gathered related to all distribution images.', 'If set to C(private), then facts are gathered related to all private images.', 'If not set to any of above, then facts are gathered related to all images.'], 'default': 'all', 'choices': ['all', 'application', 'distribution', 'private'], 'required': False}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all images
  digital_ocean_image_facts:
    image_type: all
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about application images
  digital_ocean_image_facts:
    image_type: application
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about distribution images
  digital_ocean_image_facts:
    image_type: distribution
    oauth_token: "{{ oauth_token }}"

- name: Get distribution about image with slug coreos-beta
  digital_ocean_image_facts:
  register: resp_out
- set_fact:
    distribution_name: "{{ item.distribution }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?slug=='coreos-beta']"
- debug: var=distribution_name


```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
