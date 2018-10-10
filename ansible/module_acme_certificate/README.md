# Ansible module: ansible.module_acme_certificate


Create SSL/TLS certificates with the ACME protocol

## Description

Create and renew SSL/TLS certificates with a CA supporting the L(ACME protocol,https://tools.ietf.org/html/draft-ietf-acme-acme-14), such as L(Let's Encrypt,https://letsencrypt.org/). The current implementation supports the C(http-01), C(dns-01) and C(tls-alpn-01) challenges.
To use this module, it has to be executed twice. Either as two different tasks in the same run or during two runs. Note that the output of the first run needs to be recorded and passed to the second run as the module argument C(data).
Between these two tasks you have to fulfill the required steps for the chosen challenge by whatever means necessary. For C(http-01) that means creating the necessary challenge file on the destination webserver. For C(dns-01) the necessary dns record has to be created. For C(tls-alpn-01) the necessary certificate has to be created and served. It is I(not) the responsibility of this module to perform these steps.
For details on how to fulfill these challenges, you might have to read through L(the main ACME specification,https://tools.ietf.org/html/draft-ietf-acme-acme-14#section-8) and the L(TLS-ALPN-01 specification,https://tools.ietf.org/html/draft-ietf-acme-tls-alpn-05#section-3). Also, consider the examples provided for this module.

## Requirements

TODO

## Arguments

``` json
{
    "account_email": "{'description': ['The email address associated with this account.', 'It will be used for certificate expiration warnings.', 'Note that when C(modify_account) is not set to C(no) and you also used the M(acme_account) module to specify more than one contact for your account, this module will update your account and restrict it to the (at most one) contact email address specified here.']}",
    "account_key_content": "{'description': ['Content of the ACME account RSA or Elliptic Curve key.', 'Mutually exclusive with C(account_key_src).', 'Required if C(account_key_src) is not used.', 'I(Warning): the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.', 'In case C(cryptography) is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed.'], 'version_added': '2.5'}",
    "account_key_src": "{'description': ['Path to a file containing the ACME account RSA or Elliptic Curve key.', 'RSA keys can be created with C(openssl rsa ...). Elliptic curve keys can be created with C(openssl ecparam -genkey ...). Any other tool creating private keys in PEM format can be used as well.', 'Mutually exclusive with C(account_key_content).', 'Required if C(account_key_content) is not used.'], 'aliases': ['account_key']}",
    "account_uri": "{'description': ['If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails.'], 'version_added': '2.7'}",
    "acme_directory": "{'description': ['The ACME directory to use. This is the entry point URL to access CA server API.', "For safety reasons the default is set to the Let's Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.", "For Let's Encrypt, all staging endpoints can be found here: U(https://letsencrypt.org/docs/staging-environment/)", "For Let's Encrypt, the production directory URL for ACME v1 is U(https://acme-v01.api.letsencrypt.org/directory), and the production directory URL for ACME v2 is U(https://acme-v02.api.letsencrypt.org/directory).", "I(Warning): So far, the module has only been tested against Let's Encrypt (staging and production) and against the L(Pebble testing server,https://github.com/letsencrypt/Pebble)."], 'default': 'https://acme-staging.api.letsencrypt.org/directory'}",
    "acme_version": "{'description': ['The ACME version of the endpoint.', "Must be 1 for the classic Let's Encrypt ACME endpoint, or 2 for the new standardized ACME v2 endpoint."], 'default': 1, 'choices': [1, 2], 'version_added': '2.5'}",
    "agreement": "{'description': ['URI to a terms of service document you agree to when using the ACME v1 service at C(acme_directory).', 'Default is latest gathered from C(acme_directory) URL.', 'This option will only be used when C(acme_version) is 1.']}",
    "chain_dest": "{'description': ['If specified, the intermediate certificate will be written to this file.'], 'aliases': ['chain'], 'version_added': 2.5}",
    "challenge": "{'description': ['The challenge to be performed.'], 'choices': ['http-01', 'dns-01', 'tls-alpn-01'], 'default': 'http-01'}",
    "csr": "{'description': ['File containing the CSR for the new certificate.', 'Can be created with C(openssl req ...).', 'The CSR may contain multiple Subject Alternate Names, but each one will lead to an individual challenge that must be fulfilled for the CSR to be signed.', 'I(Note): the private key used to create the CSR I(must not) be the account key. This is a bad idea from a security point of view, and the CA should not accept the CSR. The ACME server should return an error in this case.'], 'required': True, 'aliases': ['src']}",
    "data": "{'description': ['The data to validate ongoing challenges. This must be specified for the second run of the module only.', 'The value that must be used here will be provided by a previous use of this module. See the examples for more details.', 'Note that for ACME v2, only the C(order_uri) entry of C(data) will be used. For ACME v1, C(data) must be non-empty to indicate the second stage is active; all needed data will be taken from the CSR.', 'I(Note): the C(data) option was marked as C(no_log) up to Ansible 2.5. From Ansible 2.6 on, it is no longer marked this way as it causes error messages to be come unusable, and C(data) does not contain any information which can be used without having access to the account key or which are not public anyway.']}",
    "deactivate_authzs": "{'description': ['Deactivate authentication objects (authz) after issuing a certificate, or when issuing the certificate failed.', 'Authentication objects are bound to an account key and remain valid for a certain amount of time, and can be used to issue certificates without having to re-authenticate the domain. This can be a security concern.'], 'type': 'bool', 'default': False, 'version_added': 2.6}",
    "dest": "{'description': ['The destination file for the certificate.', 'Required if C(fullchain_dest) is not specified.'], 'aliases': ['cert']}",
    "force": "{'description': ['Enforces the execution of the challenge and validation, even if an existing certificate is still valid for more than C(remaining_days).', 'This is especially helpful when having an updated CSR e.g. with additional domains for which a new certificate is desired.'], 'type': 'bool', 'default': False, 'version_added': 2.6}",
    "fullchain_dest": "{'description': ['The destination file for the full chain (i.e. certificate followed by chain of intermediate certificates).', 'Required if C(dest) is not specified.'], 'version_added': 2.5, 'aliases': ['fullchain']}",
    "modify_account": "{'description': ['Boolean indicating whether the module should create the account if necessary, and update its contact data.', 'Set to C(no) if you want to use the M(acme_account) module to manage your account instead, and to avoid accidental creation of a new account using an old key if you changed the account key with M(acme_account).', 'If set to C(no), C(terms_agreed) and C(account_email) are ignored.'], 'type': 'bool', 'default': True, 'version_added': '2.6'}",
    "remaining_days": "{'description': ['The number of days the certificate must have left being valid. If C(cert_days < remaining_days), then it will be renewed. If the certificate is not renewed, module return values will not include C(challenge_data).', 'To make sure that the certificate is renewed in any case, you can use the C(force) option.'], 'default': 10}",
    "select_crypto_backend": "{'description': ['Determines which crypto backend to use. The default choice is C(auto), which tries to use C(cryptography) if available, and falls back to C(openssl).', 'If set to C(openssl), will try to use the C(openssl) binary.', 'If set to C(cryptography), will try to use the L(cryptography,https://cryptography.io/) library.'], 'type': 'str', 'default': 'auto', 'choices': ['auto', 'cryptography', 'openssl'], 'version_added': '2.7'}",
    "terms_agreed": "{'description': ['Boolean indicating whether you agree to the terms of service document.', 'ACME servers can require this to be true.', 'This option will only be used when C(acme_version) is not 1.'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "validate_certs": "{'description': ['Whether calls to the ACME directory will validate TLS certificates.', 'I(Warning): Should I(only ever) be set to C(no) for testing purposes, for example when testing against a local Pebble server.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

### Example with HTTP challenge ###

- name: Create a challenge for sample.com using a account key from a variable.
  acme_certificate:
    account_key_content: "{{ account_private_key }}"
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
  register: sample_com_challenge

# Alternative first step:
- name: Create a challenge for sample.com using a account key from hashi vault.
  acme_certificate:
    account_key_content: "{{ lookup('hashi_vault', 'secret=secret/account_private_key:value') }}"
    csr: /etc/pki/cert/csr/sample.com.csr
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
  register: sample_com_challenge

# Alternative first step:
- name: Create a challenge for sample.com using a account key file.
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
  register: sample_com_challenge

# perform the necessary steps to fulfill the challenge
# for example:
#
# - copy:
#     dest: /var/www/html/{{ sample_com_challenge['challenge_data']['sample.com']['http-01']['resource'] }}
#     content: "{{ sample_com_challenge['challenge_data']['sample.com']['http-01']['resource_value'] }}"
#     when: sample_com_challenge is changed

- name: Let the challenge be validated and retrieve the cert and intermediate certificate
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
    chain_dest: /etc/httpd/ssl/sample.com-intermediate.crt
    data: "{{ sample_com_challenge }}"

### Example with DNS challenge against production ACME server ###

- name: Create a challenge for sample.com using a account key file.
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    account_email: myself@sample.com
    src: /etc/pki/cert/csr/sample.com.csr
    cert: /etc/httpd/ssl/sample.com.crt
    challenge: dns-01
    acme_directory: https://acme-v01.api.letsencrypt.org/directory
    # Renew if the certificate is at least 30 days old
    remaining_days: 60
  register: sample_com_challenge

# perform the necessary steps to fulfill the challenge
# for example:
#
# - route53:
#     zone: sample.com
#     record: "{{ sample_com_challenge.challenge_data['sample.com']['dns-01'].record }}"
#     type: TXT
#     ttl: 60
#     # Note: route53 requires TXT entries to be enclosed in quotes
#     value: "{{ sample_com_challenge.challenge_data['sample.com']['dns-01'].resource_value }}"
#     when: sample_com_challenge is changed
#
# Alternative way:
#
# - route53:
#     zone: sample.com
#     record: "{{ item.key }}"
#     type: TXT
#     ttl: 60
#     # Note: item.value is a list of TXT entries, and route53
#     # requires every entry to be enclosed in quotes
#     value: "{{ item.value | map('regex_replace', '^(.*)$', '\'\\1\'' ) | list }}"
#     loop: "{{ sample_com_challenge.challenge_data_dns | dictsort }}"
#     when: sample_com_challenge is changed

- name: Let the challenge be validated and retrieve the cert and intermediate certificate
  acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    account_email: myself@sample.com
    src: /etc/pki/cert/csr/sample.com.csr
    cert: /etc/httpd/ssl/sample.com.crt
    fullchain: /etc/httpd/ssl/sample.com-fullchain.crt
    chain: /etc/httpd/ssl/sample.com-intermediate.crt
    challenge: dns-01
    acme_directory: https://acme-v01.api.letsencrypt.org/directory
    remaining_days: 60
    data: "{{ sample_com_challenge }}"

```

## License

TODO

## Author Information
  - ['Michael Gruener (@mgruener)']
