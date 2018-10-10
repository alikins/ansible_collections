# Ansible module: ansible.module_digital_ocean_firewall_facts


Gather facts about DigitalOcean firewalls

## Description

This module can be used to gather facts about DigitalOcean firewalls.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Firewall rule name that can be used to identify and reference a specific firewall rule.'], 'required': False}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all firewalls
  digital_ocean_firewall_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about a specific firewall by name
  digital_ocean_firewall_facts:
    oauth_token: "{{ oauth_token }}"
    name: "firewall_name"

- name: Gather information from a firewall rule
  digital_ocean_firewall_facts:
    name: SSH
  register: resp_out

- set_fact:
    firewall_id: "{{ resp_out.data.id }}"

- debug:
    msg: "{{ firewall_id }}"

```

## License

TODO

## Author Information
  - ['Anthony Bond (@BondAnthony)']
