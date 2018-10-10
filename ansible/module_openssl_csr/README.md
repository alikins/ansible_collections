# Ansible module: ansible.module_openssl_csr


Generate OpenSSL Certificate Signing Request (CSR)

## Description

This module allows one to (re)generate OpenSSL certificate signing requests. It uses the pyOpenSSL python library to interact with openssl. This module supports the subjectAltName, keyUsage, extendedKeyUsage, basicConstraints and OCSP Must Staple extensions.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "basic_constraints": "{'required': False, 'aliases': ['basicConstraints'], 'description': ['Indicates basic constraints, such as if the certificate is a CA.'], 'version_added': 2.5}",
    "basic_constraints_critical": "{'required': False, 'aliases': ['basicConstraints_critical'], 'description': ['Should the basicConstraints extension be considered as critical'], 'version_added': 2.5}",
    "common_name": "{'required': False, 'aliases': ['CN', 'commonName'], 'description': ['commonName field of the certificate signing request subject']}",
    "country_name": "{'required': False, 'aliases': ['C', 'countryName'], 'description': ['countryName field of the certificate signing request subject']}",
    "digest": "{'required': False, 'default': 'sha256', 'description': ['Digest used when signing the certificate signing request with the private key']}",
    "email_address": "{'required': False, 'aliases': ['E', 'emailAddress'], 'description': ['emailAddress field of the certificate signing request subject']}",
    "extended_key_usage": "{'required': False, 'aliases': ['extKeyUsage', 'extendedKeyUsage'], 'description': ['Additional restrictions (e.g. client authentication, server authentication) on the allowed purposes for which the public key may be used.', "This can either be a 'comma separated string' or a YAML list."]}",
    "extended_key_usage_critical": "{'required': False, 'aliases': ['extKeyUsage_critical', 'extendedKeyUsage_critical'], 'description': ['Should the extkeyUsage extension be considered as critical']}",
    "force": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Should the certificate signing request be forced regenerated by this ansible module']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "key_usage": "{'required': False, 'aliases': ['keyUsage'], 'description': ['This defines the purpose (e.g. encipherment, signature, certificate signing) of the key contained in the certificate.', "This can either be a 'comma separated string' or a YAML list."]}",
    "key_usage_critical": "{'required': False, 'aliases': ['keyUsage_critical'], 'description': ['Should the keyUsage extension be considered as critical']}",
    "locality_name": "{'required': False, 'aliases': ['L', 'localityName'], 'description': ['localityName field of the certificate signing request subject']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "ocsp_must_staple": "{'required': False, 'aliases': ['ocspMustStaple'], 'description': ['Indicates that the certificate should contain the OCSP Must Staple extension (U(https://tools.ietf.org/html/rfc7633)).'], 'version_added': 2.5}",
    "ocsp_must_staple_critical": "{'required': False, 'aliases': ['ocspMustStaple_critical'], 'description': ['Should the OCSP Must Staple extension be considered as critical', 'Warning: according to the RFC, this extension should not be marked as critical, as old clients not knowing about OCSP Must Staple are required to reject such certificates (see U(https://tools.ietf.org/html/rfc7633#section-4)).'], 'version_added': 2.5}",
    "organization_name": "{'required': False, 'aliases': ['O', 'organizationName'], 'description': ['organizationName field of the certificate signing request subject']}",
    "organizational_unit_name": "{'required': False, 'aliases': ['OU', 'organizationalUnitName'], 'description': ['organizationalUnitName field of the certificate signing request subject']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'required': True, 'description': ['Name of the file into which the generated OpenSSL certificate signing request will be written']}",
    "privatekey_passphrase": "{'required': False, 'description': ['The passphrase for the privatekey.']}",
    "privatekey_path": "{'required': True, 'description': ['Path to the privatekey to use when signing the certificate signing request']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the certificate signing request should exist or not, taking action if the state is different from what is stated.']}",
    "state_or_province_name": "{'required': False, 'aliases': ['ST', 'stateOrProvinceName'], 'description': ['stateOrProvinceName field of the certificate signing request subject']}",
    "subject": "{'required': False, 'description': ['Key/value pairs that will be present in the subject name field of the certificate signing request.', 'If you need to specify more than one value with the same key, use a list as value.'], 'version_added': '2.5'}",
    "subject_alt_name": "{'required': False, 'aliases': ['subjectAltName'], 'description': ['SAN extension to attach to the certificate signing request', "This can either be a 'comma separated string' or a YAML list.", 'Values should be prefixed by their options. (i.e., C(email), C(URI), C(DNS), C(RID), C(IP), C(dirName), C(otherName) and the ones specific to your CA)', 'More at U(https://tools.ietf.org/html/rfc5280#section-4.2.1.6)']}",
    "subject_alt_name_critical": "{'required': False, 'aliases': ['subjectAltName_critical'], 'description': ['Should the subjectAltName extension be considered as critical']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "version": "{'required': False, 'default': 1, 'description': ['Version of the certificate signing request']}",
}
```

## Examples


``` yaml

# Generate an OpenSSL Certificate Signing Request
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    common_name: www.ansible.com

# Generate an OpenSSL Certificate Signing Request with a
# passphrase protected private key
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    privatekey_passphrase: ansible
    common_name: www.ansible.com

# Generate an OpenSSL Certificate Signing Request with Subject information
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    country_name: FR
    organization_name: Ansible
    email_address: jdoe@ansible.com
    common_name: www.ansible.com

# Generate an OpenSSL Certificate Signing Request with subjectAltName extension
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    subject_alt_name: 'DNS:www.ansible.com,DNS:m.ansible.com'

# Generate an OpenSSL CSR with subjectAltName extension with dynamic list
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    subject_alt_name: "{{ item.value | map('regex_replace', '^', 'DNS:') | list }}"
  with_dict:
    dns_server:
    - www.ansible.com
    - m.ansible.com

# Force re-generate an OpenSSL Certificate Signing Request
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    force: True
    common_name: www.ansible.com

# Generate an OpenSSL Certificate Signing Request with special key usages
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    common_name: www.ansible.com
    key_usage:
      - digitalSignature
      - keyAgreement
    extended_key_usage:
      - clientAuth

# Generate an OpenSSL Certificate Signing Request with OCSP Must Staple
- openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    common_name: www.ansible.com
    ocsp_must_staple: true

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']