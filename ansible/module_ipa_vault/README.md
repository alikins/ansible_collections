# Ansible module: ansible.module_ipa_vault


Manage FreeIPA vaults

## Description

Add, modify and delete vaults and secret vaults.
KRA service should be enabled to use this module.

## Requirements

TODO

## Arguments

``` json
{
    "cn": "{'description': ['Vault name.', 'Can not be changed as it is the unique identifier.'], 'required': True, 'aliases': ['name']}",
    "description": "{'description': ['Description.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "ipavaultpublickey": "{'description': ['Public key.'], 'aliases': ['vault_public_key']}",
    "ipavaultsalt": "{'description': ['Vault Salt.'], 'aliases': ['vault_salt']}",
    "ipavaulttype": "{'description': ['Vault types are based on security level.'], 'default': 'symmetric', 'choices': ['standard', 'symmetric', 'asymmetric'], 'required': True, 'aliases': ['vault_type']}",
    "replace": "{'description': ['Force replace the existant vault on IPA server.'], 'type': 'bool', 'default': False, 'choices': ['True', 'False']}",
    "service": "{'description': ['Any service can own one or more service vaults.', 'Mutually exclusive with user.']}",
    "state": "{'description': ['State to ensure.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['Any user can own one or more user vaults.', 'Mutually exclusive with service.'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['Validate IPA server certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure vault is present
- ipa_vault:
    name: vault01
    vault_type: standard
    user: user01
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    validate_certs: false

# Ensure vault is present for Admin user
- ipa_vault:
    name: vault01
    vault_type: standard
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure vault is absent
- ipa_vault:
    name: vault01
    vault_type: standard
    user: user01
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Modify vault if already exists
- ipa_vault:
    name: vault01
    vault_type: standard
    description: "Vault for test"
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    replace: True

# Get vault info if already exists
- ipa_vault:
    name: vault01
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Juan Manuel Parrilla (@jparrill)']
