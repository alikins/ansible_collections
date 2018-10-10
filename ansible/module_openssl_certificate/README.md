# Ansible module: ansible.module_openssl_certificate


Generate and/or check OpenSSL certificates

## Description

This module allows one to (re)generate OpenSSL certificates. It implements a notion of provider (ie. C(selfsigned), C(ownca), C(acme), C(assertonly)) for your certificate. The 'assertonly' provider is intended for use cases where one is only interested in checking properties of a supplied certificate. The 'ownca' provider is intended for generate OpenSSL certificate signed with your own CA (Certificate Authority) certificate (self-signed certificate). Many properties that can be specified in this module are for validation of an existing or newly generated certificate. The proper place to specify them, if you want to receive a certificate with these properties is a CSR (Certificate Signing Request). It uses the pyOpenSSL python library to interact with OpenSSL.

## Requirements

TODO

## Arguments

``` json
{
    "acme_accountkey_path": "{'description': ['Path to the accountkey for the C(acme) provider']}",
    "acme_chain": "{'default': True, 'description': ['Include the intermediate certificate to the generated certificate'], 'version_added': '2.5'}",
    "acme_challenge_path": "{'description': ['Path to the ACME challenge directory that is served on U(http://<HOST>:80/.well-known/acme-challenge/)']}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "csr_path": "{'description': ['Path to the Certificate Signing Request (CSR) used to generate this certificate. This is not required in C(assertonly) mode.']}",
    "extended_key_usage": "{'description': ['The I(extended_key_usage) extension field must contain all these values.'], 'aliases': ['extendedKeyUsage']}",
    "extended_key_usage_strict": "{'default': False, 'type': 'bool', 'description': ['If set to True, the I(extended_key_usage) extension field must contain only these values.'], 'aliases': ['extendedKeyUsage_strict']}",
    "force": "{'default': False, 'type': 'bool', 'description': ['Generate the certificate, even if it already exists.']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "has_expired": "{'default': False, 'type': 'bool', 'description': ['Checks if the certificate is expired/not expired at the time the module is executed.']}",
    "invalid_at": "{'description': ['The certificate must be invalid at this point in time. The timestamp is formatted as an ASN.1 TIME.']}",
    "issuer": "{'description': ['Key/value pairs that must be present in the issuer name field of the certificate. If you need to specify more than one value with the same key, use a list as value.']}",
    "issuer_strict": "{'default': False, 'type': 'bool', 'description': ['If set to True, the I(issuer) field must contain only these values.'], 'version_added': '2.5'}",
    "key_usage": "{'description': ['The I(key_usage) extension field must contain all these values.'], 'aliases': ['keyUsage']}",
    "key_usage_strict": "{'default': False, 'type': 'bool', 'description': ['If set to True, the I(key_usage) extension field must contain only these values.'], 'aliases': ['keyUsage_strict']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "not_after": "{'description': ['The certificate must expire at this point in time. The timestamp is formatted as an ASN.1 TIME.'], 'aliases': ['notAfter']}",
    "not_before": "{'description': ['The certificate must start to become valid at this point in time. The timestamp is formatted as an ASN.1 TIME.'], 'aliases': ['notBefore']}",
    "ownca_digest": "{'default': 'sha256', 'description': ['Digest algorithm to be used for the C(ownca) certificate.'], 'version_added': '2.7'}",
    "ownca_not_after": "{'description': ['The timestamp at which the certificate stops being valid. The timestamp is formatted as an ASN.1 TIME. If this value is not specified, certificate will stop being valid 10 years from now.'], 'version_added': '2.7'}",
    "ownca_not_before": "{'description': ['The timestamp at which the certificate starts being valid. The timestamp is formatted as an ASN.1 TIME. If this value is not specified, certificate will start being valid from now.'], 'version_added': '2.7'}",
    "ownca_path": "{'description': ['Remote absolute path of the CA (Certificate Authority) certificate.'], 'version_added': '2.7'}",
    "ownca_privatekey_passphrase": "{'description': ['The passphrase for the I(ownca_privatekey_path).'], 'version_added': '2.7'}",
    "ownca_privatekey_path": "{'description': ['Path to the CA (Certificate Authority) private key to use when signing the certificate.'], 'version_added': '2.7'}",
    "ownca_version": "{'default': 3, 'description': ['Version of the C(ownca) certificate. Nowadays it should almost always be C(3).'], 'version_added': '2.7'}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'required': True, 'description': ['Remote absolute path where the generated certificate file should be created or is already located.']}",
    "privatekey_passphrase": "{'description': ['The passphrase for the I(privatekey_path).']}",
    "privatekey_path": "{'description': ['Path to the private key to use when signing the certificate.']}",
    "provider": "{'required': True, 'choices': ['selfsigned', 'ownca', 'assertonly', 'acme'], 'description': ['Name of the provider to use to generate/retrieve the OpenSSL certificate. The C(assertonly) provider will not generate files and fail if the certificate file is missing.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "selfsigned_digest": "{'default': 'sha256', 'description': ['Digest algorithm to be used when self-signing the certificate']}",
    "selfsigned_not_after": "{'description': ['The timestamp at which the certificate stops being valid. The timestamp is formatted as an ASN.1 TIME. If this value is not specified, certificate will stop being valid 10 years from now.'], 'aliases': ['selfsigned_notAfter']}",
    "selfsigned_not_before": "{'description': ['The timestamp at which the certificate starts being valid. The timestamp is formatted as an ASN.1 TIME. If this value is not specified, certificate will start being valid from now.'], 'aliases': ['selfsigned_notBefore']}",
    "selfsigned_version": "{'default': 3, 'description': ['Version of the C(selfsigned) certificate. Nowadays it should almost always be C(3).'], 'version_added': '2.5'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "signature_algorithms": "{'description': ["list of algorithms that you would accept the certificate to be signed with (e.g. ['sha256WithRSAEncryption', 'sha512WithRSAEncryption'])."]}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the certificate should exist or not, taking action if the state is different from what is stated.']}",
    "subject": "{'description': ['Key/value pairs that must be present in the subject name field of the certificate. If you need to specify more than one value with the same key, use a list as value.']}",
    "subject_alt_name": "{'description': ['The I(subject_alt_name) extension field must contain these values.'], 'aliases': ['subjectAltName']}",
    "subject_alt_name_strict": "{'default': False, 'type': 'bool', 'description': ['If set to True, the I(subject_alt_name) extension field must contain only these values.'], 'aliases': ['subjectAltName_strict']}",
    "subject_strict": "{'default': False, 'type': 'bool', 'description': ['If set to True, the I(subject) field must contain only these values.'], 'version_added': '2.5'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "valid_at": "{'description': ['The certificate must be valid at this point in time. The timestamp is formatted as an ASN.1 TIME.']}",
    "valid_in": "{'description': ['The certificate must still be valid in I(valid_in) seconds from now.']}",
    "version": "{'description': ['Version of the certificate. Nowadays it should almost always be 3.']}",
}
```

## Examples


``` yaml

- name: Generate a Self Signed OpenSSL certificate
  openssl_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    privatekey_path: /etc/ssl/private/ansible.com.pem
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: selfsigned

- name: Generate an OpenSSL certificate signed with your own CA certificate
  openssl_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    ownca_path: /etc/ssl/crt/ansible_CA.crt
    ownca_privatekey_path: /etc/ssl/private/ansible_CA.pem
    provider: ownca

- name: Generate a Let's Encrypt Certificate
  openssl_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: acme
    acme_accountkey_path: /etc/ssl/private/ansible.com.pem
    acme_challenge_path: /etc/ssl/challenges/ansible.com/

- name: Force (re-)generate a new Let's Encrypt Certificate
  openssl_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: acme
    acme_accountkey_path: /etc/ssl/private/ansible.com.pem
    acme_challenge_path: /etc/ssl/challenges/ansible.com/
    force: True

# Examples for some checks one could use the assertonly provider for:

# How to use the assertonly provider to implement and trigger your own custom certificate generation workflow:
- name: Check if a certificate is currently still valid, ignoring failures
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    has_expired: False
  ignore_errors: True
  register: validity_check

- name: Run custom task(s) to get a new, valid certificate in case the initial check failed
  command: superspecialSSL recreate /etc/ssl/crt/example.com.crt
  when: validity_check.failed

- name: Check the new certificate again for validity with the same parameters, this time failing the play if it is still invalid
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    has_expired: False
  when: validity_check.failed

# Some other checks that assertonly could be used for:
- name: Verify that an existing certificate was issued by the Let's Encrypt CA and is currently still valid
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    issuer:
      O: Let's Encrypt
    has_expired: False

- name: Ensure that a certificate uses a modern signature algorithm (no SHA1, MD5 or DSA)
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    signature_algorithms:
      - sha224WithRSAEncryption
      - sha256WithRSAEncryption
      - sha384WithRSAEncryption
      - sha512WithRSAEncryption
      - sha224WithECDSAEncryption
      - sha256WithECDSAEncryption
      - sha384WithECDSAEncryption
      - sha512WithECDSAEncryption

- name: Ensure that the existing certificate belongs to the specified private key
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    privatekey_path: /etc/ssl/private/example.com.pem
    provider: assertonly

- name: Ensure that the existing certificate is still valid at the winter solstice 2017
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    valid_at: 20171221162800Z

- name: Ensure that the existing certificate is still valid 2 weeks (1209600 seconds) from now
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    valid_in: 1209600

- name: Ensure that the existing certificate is only used for digital signatures and encrypting other keys
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    key_usage:
      - digitalSignature
      - keyEncipherment
    key_usage_strict: true

- name: Ensure that the existing certificate can be used for client authentication
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    extended_key_usage:
      - clientAuth

- name: Ensure that the existing certificate can only be used for client authentication and time stamping
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    extended_key_usage:
      - clientAuth
      - 1.3.6.1.5.5.7.3.8
    extended_key_usage_strict: true

- name: Ensure that the existing certificate has a certain domain in its subjectAltName
  openssl_certificate:
    path: /etc/ssl/crt/example.com.crt
    provider: assertonly
    subject_alt_name:
      - www.example.com
      - test.example.com

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)', 'Markus Teufelberger (@MarkusTeufelberger)']
  - ['Yanis Guenane (@Spredzy)', 'Markus Teufelberger (@MarkusTeufelberger)']
