# Ansible module: ansible.module_openssl_pkcs12


Generate OpenSSL PKCS#12 archive

## Description

This module allows one to (re-)generate PKCS#12.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'default': 'export', 'choices': ['parse', 'export'], 'description': ['C(export) or C(parse) a PKCS#12.']}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "ca_certificates": "{'description': ['List of CA certificate to include.']}",
    "certificate_path": "{'description': ['The path to read certificates and private keys from.  Must be in PEM format.']}",
    "force": "{'default': False, 'type': 'bool', 'description': ['Should the file be regenerated even if it already exists.']}",
    "friendly_name": "{'aliases': ['name'], 'description': ['Specifies the friendly name for the certificate and private key.']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "iter_size": "{'default': 2048, 'description': ['Number of times to repeat the encryption step.']}",
    "maciter_size": "{'default': 1, 'description': ['Number of times to repeat the MAC step.']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "passphrase": "{'description': ['The PKCS#12 password.']}",
    "path": "{'required': True, 'description': ['Filename to write the PKCS#12 file to.']}",
    "privatekey_passphrase": "{'description': ['Passphrase source to decrypt any input private keys with.']}",
    "privatekey_path": "{'description': ['File to read private key from.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['PKCS#12 file path to parse.']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the file should exist or not. All parameters except C(path) are ignored when state is C(absent).']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: 'Generate PKCS#12 file'
  openssl_pkcs12:
    action: export
    path: '/opt/certs/ansible.p12'
    friendly_name: 'raclette'
    privatekey_path: '/opt/certs/keys/key.pem'
    certificate_path: '/opt/certs/cert.pem'
    ca_certificates: '/opt/certs/ca.pem'
    state: present

- name: 'Change PKCS#12 file permission'
  openssl_pkcs12:
    action: export
    path: '/opt/certs/ansible.p12'
    friendly_name: 'raclette'
    privatekey_path: '/opt/certs/keys/key.pem'
    certificate_path: '/opt/certs/cert.pem'
    ca_certificates: '/opt/certs/ca.pem'
    state: present
    mode: 0600

- name: 'Regen PKCS#12 file'
  openssl_pkcs12:
    action: export
    src: '/opt/certs/ansible.p12'
    path: '/opt/certs/ansible.p12'
    friendly_name: 'raclette'
    privatekey_path: '/opt/certs/keys/key.pem'
    certificate_path: '/opt/certs/cert.pem'
    ca_certificates: '/opt/certs/ca.pem'
    state: present
    mode: 0600
    force: True

- name: 'Dump/Parse PKCS#12 file'
  openssl_pkcs12:
    action: parse
    src: '/opt/certs/ansible.p12'
    path: '/opt/certs/ansible.pem'
    state: present

- name: 'Remove PKCS#12 file'
  openssl_pkcs12:
    path: '/opt/certs/ansible.p12'
    state: absent

```

## License

TODO

## Author Information
  - ['Guillaume Delpierre (@gdelpierre)']
