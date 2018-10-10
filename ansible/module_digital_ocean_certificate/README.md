# Ansible module: ansible.module_digital_ocean_certificate


Manage certificates in DigitalOcean

## Description

Create, Retrieve and remove certificates DigitalOcean.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_chain": "{'description': ["The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate."]}",
    "leaf_certificate": "{'description': ['A PEM-formatted public SSL Certificate.']}",
    "name": "{'description': ['The name of the certificate.'], 'required': True}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "private_key": "{'description': ['A PEM-formatted private key content of SSL Certificate.']}",
    "state": "{'description': ['Whether the certificate should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: create a certificate
  digital_ocean_certificate:
    name: production
    state: present
    private_key: "-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkM8OI7pRpgyj1I
-----END PRIVATE KEY-----"
    leaf_certificate: "-----BEGIN CERTIFICATE-----
MIIFDmg2Iaw==
-----END CERTIFICATE-----"
    oauth_token: b7d03a6947b217efb6f3ec3bd365652

- name: create a certificate using file lookup plugin
  digital_ocean_certificate:
    name: production
    state: present
    private_key: "{{ lookup('file', 'test.key') }}"
    leaf_certificate: "{{ lookup('file', 'test.cert') }}"
    oauth_token: "{{ oauth_token }}"

- name: create a certificate with trust chain
  digital_ocean_certificate:
    name: production
    state: present
    private_key: "{{ lookup('file', 'test.key') }}"
    leaf_certificate: "{{ lookup('file', 'test.cert') }}"
    certificate_chain: "{{ lookup('file', 'chain.cert') }}"
    oauth_token: "{{ oauth_token }}"

- name: remove a certificate
  digital_ocean_certificate:
    name: production
    state: absent
    oauth_token: "{{ oauth_token }}"


```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
