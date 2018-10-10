# Ansible module: ansible.module_java_keystore


Create or delete a Java keystore in JKS format

## Description

Create or delete a Java keystore in JKS format for a given certificate.

## Requirements

TODO

## Arguments

``` json
{
    "certificate": "{'description': ['Certificate that should be used to create the key store.'], 'required': False}",
    "dest": "{'description': ['Absolute path where the jks should be generated.'], 'required': True}",
    "force": "{'description': ['Key store will be created even if it already exists.'], 'required': False, 'type': 'bool', 'default': False}",
    "group": "{'description': ['Name of the group that should own jks file.'], 'required': False}",
    "mode": "{'description': ['Mode the file should be.'], 'required': False}",
    "name": "{'description': ['Name of the certificate.'], 'required': True}",
    "owner": "{'description': ['Name of the user that should own jks file.'], 'required': False}",
    "password": "{'description': ['Password that should be used to secure the key store.'], 'required': False}",
    "private_key": "{'description': ['Private key that should be used to create the key store.'], 'required': False}",
}
```

## Examples


``` yaml

# Create a key store for the given certificate (inline)
- java_keystore:
    name: example
    certificate: |
      -----BEGIN CERTIFICATE-----
      h19dUZ2co2fI/ibYiwxWk4aeNE6KWvCaTQOMQ8t6Uo2XKhpL/xnjoAgh1uCQN/69
      MG+34+RhUWzCfdZH7T8/qDxJw2kEPKluaYh7KnMsba+5jHjmtzix5QIDAQABo4IB
      -----END CERTIFICATE-----
    private_key: |
      -----BEGIN RSA PRIVATE KEY-----
      DBVFTEVDVFJJQ0lURSBERSBGUkFOQ0UxFzAVBgNVBAsMDjAwMDIgNTUyMDgxMzE3
      GLlDNMw/uHyME7gHFsqJA7O11VY6O5WQ4IDP3m/s5ZV6s+Nn6Lerz17VZ99
      -----END RSA PRIVATE KEY-----
    password: changeit
    dest: /etc/security/keystore.jks

# Create a key store for the given certificate (lookup)
- java_keystore:
    name: example
    certificate: "{{lookup('file', '/path/to/certificate.crt') }}"
    private_key: "{{lookup('file', '/path/to/private.key') }}"
    password: changeit
    dest: /etc/security/keystore.jks

```

## License

TODO

## Author Information
  - ['Guillaume Grossetie']
