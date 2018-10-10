# Ansible module: ansible.module_certificate_complete_chain


Complete certificate chain given a set of untrusted and root certificates

## Description

This module completes a given chain of certificates in PEM format by finding intermediate certificates from a given set of certificates, until it finds a root certificate in another given set of certificates.
This can for example be used to find the root certificate for a certificate chain returned by M(acme_certificate).
Note that this module does I(not) check for validity of the chains. It only checks that issuer and subject match, and that the signature is correct. It ignores validity dates and key usage completely. If you need to verify that a generated chain is valid, please use C(openssl verify ...).

## Requirements

TODO

## Arguments

``` json
{
    "input_chain": "{'required': True, 'description': ['A concatenated set of certificates in PEM format forming a chain.', 'The module will try to complete this chain.']}",
    "intermediate_certificates": "{'required': False, 'type': 'list', 'default': [], 'description': ['A list of filenames or directories.', 'A filename is assumed to point to a file containing one or more certificates in PEM format. All certificates in this file will be added to the set of root certificates.', 'If a directory name is given, all files in the directory and its subdirectories will be scanned and tried to be parsed as concatenated certificates in PEM format.', 'Symbolic links will be followed.']}",
    "root_certificates": "{'required': True, 'type': 'list', 'description': ['A list of filenames or directories.', 'A filename is assumed to point to a file containing one or more certificates in PEM format. All certificates in this file will be added to the set of root certificates.', 'If a directory name is given, all files in the directory and its subdirectories will be scanned and tried to be parsed as concatenated certificates in PEM format.', 'Symbolic links will be followed.']}",
}
```

## Examples


``` yaml

# Given a leaf certificate for www.ansible.com and one or more intermediate
# certificates, finds the associated root certificate.
- name: Find root certificate
  certificate_complete_chain:
    input_chain: "{{ lookup('file', '/etc/ssl/csr/www.ansible.com-fullchain.pem') }}"
    root_certificates:
    - /etc/ca-certificates/
  register: www_ansible_com
- name: Write root certificate to disk
  copy:
    dest: /etc/ssl/csr/www.ansible.com-root.pem
    content: "{{ www_ansible_com.root }}"

# Given a leaf certificate for www.ansible.com, and a list of intermediate
# certificates, finds the associated root certificate.
- name: Find root certificate
  certificate_complete_chain:
    input_chain: "{{ lookup('file', '/etc/ssl/csr/www.ansible.com.pem') }}"
    intermediate_certificates:
    - /etc/ssl/csr/www.ansible.com-chain.pem
    root_certificates:
    - /etc/ca-certificates/
  register: www_ansible_com
- name: Write complete chain to disk
  copy:
    dest: /etc/ssl/csr/www.ansible.com-completechain.pem
    content: "{{ ''.join(www_ansible_com.complete_chain) }}"
- name: Write root chain (intermediates and root) to disk
  copy:
    dest: /etc/ssl/csr/www.ansible.com-rootchain.pem
    content: "{{ ''.join(www_ansible_com.chain) }}"

```

## License

TODO

## Author Information
  - ['Felix Fontein (@felixfontein)']
