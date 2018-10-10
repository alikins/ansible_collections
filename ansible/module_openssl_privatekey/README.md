# Ansible module: ansible.module_openssl_privatekey


Generate OpenSSL private keys

## Description

This module allows one to (re)generate OpenSSL private keys. It uses the pyOpenSSL python library to interact with openssl. One can generate either RSA or DSA private keys. Keys are generated in PEM format.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "cipher": "{'required': False, 'description': ['The cipher to encrypt the private key. (cipher can be found by running `openssl list-cipher-algorithms`)'], 'version_added': '2.4'}",
    "force": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Should the key be regenerated even if it already exists']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "passphrase": "{'required': False, 'description': ['The passphrase for the private key.'], 'version_added': '2.4'}",
    "path": "{'required': True, 'description': ['Name of the file in which the generated TLS/SSL private key will be written. It will have 0600 mode.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "size": "{'required': False, 'default': 4096, 'description': ['Size (in bits) of the TLS/SSL key to generate']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the private key should exist or not, taking action if the state is different from what is stated.']}",
    "type": "{'required': False, 'default': 'RSA', 'choices': ['RSA', 'DSA'], 'description': ['The algorithm used to generate the TLS/SSL private key']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

# Generate an OpenSSL private key with the default values (4096 bits, RSA)
- openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem

# Generate an OpenSSL private key with the default values (4096 bits, RSA)
# and a passphrase
- openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    passphrase: ansible
    cipher: aes256

# Generate an OpenSSL private key with a different size (2048 bits)
- openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    size: 2048

# Force regenerate an OpenSSL private key if it already exists
- openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    force: True

# Generate an OpenSSL private key with a different algorithm (DSA)
- openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    type: DSA

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']
