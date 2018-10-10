# Ansible module: ansible.module_digital_ocean_certificate_facts


Gather facts about DigitalOcean certificates

## Description

This module can be used to gather facts about DigitalOcean provided certificates.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_id": "{'description': ['Certificate ID that can be used to identify and reference a certificate.'], 'required': False}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all certificates
  digital_ocean_certificate_facts:
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about certificate with given id
  digital_ocean_certificate_facts:
    oauth_token: "{{ oauth_token }}"
    certificate_id: "892071a0-bb95-49bc-8021-3afd67a210bf"

- name: Get not after facts about certificate
  digital_ocean_certificate_facts:
  register: resp_out
- set_fact:
    not_after_date: "{{ item.not_after }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?name=='web-cert-01']"
- debug: var=not_after_date

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
