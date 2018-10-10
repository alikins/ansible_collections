# Ansible module: ansible.module_acme_challenge_cert_helper


Prepare certificates required for ACME challenges such as ``tls-alpn-01``

## Description

Prepares certificates for ACME challenges such as C(tls-alpn-01).
The raw data is provided by the M(acme_certificate) module, and needs to be converted to a certificate to be used for challenge validation. This module provides a simple way to generate the required certificates.
The C(tls-alpn-01) implementation is based on L(the draft-05 version of the specification,https://tools.ietf.org/html/draft-ietf-acme-tls-alpn-05).

## Requirements

TODO

## Arguments

``` json
{
    "challenge": "{'description': ['The challenge type.'], 'required': True, 'choices': ['tls-alpn-01']}",
    "challenge_data": "{'description': ['The C(challenge_data) entry provided by M(acme_certificate) for the challenge.'], 'required': True}",
    "private_key_content": "{'description': ['Content of the private key to use for this challenge certificate.', 'Mutually exclusive with C(private_key_src).']}",
    "private_key_src": "{'description': ['Path to a file containing the private key file to use for this challenge certificate.', 'Mutually exclusive with C(private_key_content).']}",
}
```

## Examples


``` yaml

- name: Create challenges for a given CRT for sample.com
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    challenge: tls-alpn-01
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
  register: sample_com_challenge

- name: Create certificates for challenges
  acme_challenge_cert_helper:
    challenge: tls-alpn-01
    challenge_data: "{{ item.value['tls-alpn-01'] }}"
    private_key_src: /etc/pki/cert/key/sample.com.key
  loop: "{{ sample_com_challenge.challenge_data | dictsort }}"
  register: sample_com_challenge_certs

- name: Install challenge certificates
  # We need to set up HTTPS such that for the domain,
  # regular_certificate is delivered for regular connections,
  # except if ALPN selects the "acme-tls/1"; then, the
  # challenge_certificate must be delivered.
  # This can for example be achieved with very new versions
  # of NGINX; search for ssl_preread and
  # ssl_preread_alpn_protocols for information on how to
  # route by ALPN protocol.
  ...:
    domain: "{{ item.domain }}"
    challenge_certificate: "{{ item.challenge_certificate }}"
    regular_certificate: "{{ item.regular_certificate }}"
    private_key: /etc/pki/cert/key/sample.com.key
  loop: "{{ sample_com_challenge_certs.results }}"

- name: Create certificate for a given CSR for sample.com
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    challenge: tls-alpn-01
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
    data: "{{ sample_com_challenge }}"

```

## License

TODO

## Author Information
  - ['Felix Fontein (@felixfontein)']
