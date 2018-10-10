# Ansible module: ansible.module_acme_account_facts


Retrieves information on ACME accounts

## Description

Allows to retrieve information on accounts a CA supporting the L(ACME protocol,https://tools.ietf.org/html/draft-ietf-acme-acme-14), such as L(Let's Encrypt,https://letsencrypt.org/).
This module only works with the ACME v2 protocol.

## Requirements

TODO

## Arguments

``` json
{
    "account_key_content": "{'description': ['Content of the ACME account RSA or Elliptic Curve key.', 'Mutually exclusive with C(account_key_src).', 'Required if C(account_key_src) is not used.', 'I(Warning): the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.', 'In case C(cryptography) is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed.'], 'version_added': '2.5'}",
    "account_key_src": "{'description': ['Path to a file containing the ACME account RSA or Elliptic Curve key.', 'RSA keys can be created with C(openssl rsa ...). Elliptic curve keys can be created with C(openssl ecparam -genkey ...). Any other tool creating private keys in PEM format can be used as well.', 'Mutually exclusive with C(account_key_content).', 'Required if C(account_key_content) is not used.'], 'aliases': ['account_key']}",
    "account_uri": "{'description': ['If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails.'], 'version_added': '2.7'}",
    "acme_directory": "{'description': ['The ACME directory to use. This is the entry point URL to access CA server API.', "For safety reasons the default is set to the Let's Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.", "For Let's Encrypt, all staging endpoints can be found here: U(https://letsencrypt.org/docs/staging-environment/)", "For Let's Encrypt, the production directory URL for ACME v1 is U(https://acme-v01.api.letsencrypt.org/directory), and the production directory URL for ACME v2 is U(https://acme-v02.api.letsencrypt.org/directory).", "I(Warning): So far, the module has only been tested against Let's Encrypt (staging and production) and against the L(Pebble testing server,https://github.com/letsencrypt/Pebble)."], 'default': 'https://acme-staging.api.letsencrypt.org/directory'}",
    "acme_version": "{'description': ['The ACME version of the endpoint.', "Must be 1 for the classic Let's Encrypt ACME endpoint, or 2 for the new standardized ACME v2 endpoint."], 'default': 1, 'choices': [1, 2], 'version_added': '2.5'}",
    "select_crypto_backend": "{'description': ['Determines which crypto backend to use. The default choice is C(auto), which tries to use C(cryptography) if available, and falls back to C(openssl).', 'If set to C(openssl), will try to use the C(openssl) binary.', 'If set to C(cryptography), will try to use the L(cryptography,https://cryptography.io/) library.'], 'type': 'str', 'default': 'auto', 'choices': ['auto', 'cryptography', 'openssl'], 'version_added': '2.7'}",
    "validate_certs": "{'description': ['Whether calls to the ACME directory will validate TLS certificates.', 'I(Warning): Should I(only ever) be set to C(no) for testing purposes, for example when testing against a local Pebble server.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Check whether an account with the given account key exists
  acme_account_facts:
    account_key_src: /etc/pki/cert/private/account.key
    register: account_data
- name: Verify that account exists
  assert:
    that:
      - account_data.exists
- name: Print account URI
  debug: var=account_data.account_uri
- name: Print account contacts
  debug: var=account_data.account.contact

- name: Check whether the account exists and is accessible with the given account key
  acme_account_facts:
    account_key_content: "{{ acme_account_key }}"
    account_uri: "{{ acme_account_uri }}"
    register: account_data
- name: Verify that account exists
  assert:
    that:
      - account_data.exists
- name: Print account contacts
  debug: var=account_data.account.contact

```

## License

TODO

## Author Information
  - ['Felix Fontein (@felixfontein)']
