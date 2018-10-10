# Ansible module: ansible.module_openssl_publickey


Generate an OpenSSL public key from its private key

## Description

This module allows one to (re)generate OpenSSL public keys from their private keys. It uses the pyOpenSSL python library to interact with openssl. Keys are generated in PEM format. This module works only if the version of PyOpenSSL is recent enough (> 16.0.0).

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "force": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Should the key be regenerated even it it already exists']}",
    "format": "{'required': False, 'default': 'PEM', 'choices': ['PEM', 'OpenSSH'], 'description': ['The format of the public key.'], 'version_added': '2.4'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'required': True, 'description': ['Name of the file in which the generated TLS/SSL public key will be written.']}",
    "privatekey_passphrase": "{'required': False, 'description': ['The passphrase for the privatekey.'], 'version_added': '2.4'}",
    "privatekey_path": "{'required': True, 'description': ['Path to the TLS/SSL private key from which to generate the public key.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the public key should exist or not, taking action if the state is different from what is stated.']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

# Generate an OpenSSL public key in PEM format.
- openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem

# Generate an OpenSSL public key in OpenSSH v2 format.
- openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    format: OpenSSH

# Generate an OpenSSL public key with a passphrase protected
# private key
- openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    privatekey_passphrase: ansible

# Force regenerate an OpenSSL public key if it already exists
- openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    force: True

# Remove an OpenSSL public key
- openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    state: absent

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']
