# Ansible module: ansible.module_digital_ocean_load_balancer_facts


Gather facts about DigitalOcean load balancers

## Description

This module can be used to gather facts about DigitalOcean provided load balancers.

## Requirements

TODO

## Arguments

``` json
{
    "load_balancer_id": "{'description': ['Load balancer ID that can be used to identify and reference a load_balancer.'], 'required': False}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all load balancers
  digital_ocean_load_balancer_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about load balancer with given id
  digital_ocean_load_balancer_facts:
    oauth_token: "{{ oauth_token }}"
    load_balancer_id: "4de7ac8b-495b-4884-9a69-1050c6793cd6"

- name: Get name from load balancer id
  digital_ocean_load_balancer_facts:
  register: resp_out
- set_fact:
    load_balancer_name: "{{ item.name }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?id=='4de7ac8b-495b-4884-9a69-1050c6793cd6']"
- debug: var=load_balancer_name

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
