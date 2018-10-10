# Ansible module: ansible.module_openssl_dhparam


Generate OpenSSL Diffie-Hellman Parameters

## Description

This module allows one to (re)generate OpenSSL DH-params. This module uses file common arguments to specify generated file permissions.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "force": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Should the parameters be regenerated even it it already exists']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'required': True, 'description': ['Name of the file in which the generated parameters will be saved.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "size": "{'required': False, 'default': 4096, 'description': ['Size (in bits) of the generated DH-params']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the parameters should exist or not, taking action if the state is different from what is stated.']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

# Generate Diffie-Hellman parameters with the default size (4096 bits)
- openssl_dhparam:
    path: /etc/ssl/dhparams.pem

# Generate DH Parameters with a different size (2048 bits)
- openssl_dhparam:
    path: /etc/ssl/dhparams.pem
    size: 2048

# Force regenerate an DH parameters if they already exist
- openssl_dhparam:
    path: /etc/ssl/dhparams.pem
    force: True


```

## License

TODO

## Author Information
  - ['Thom Wiggers (@thomwiggers)']
