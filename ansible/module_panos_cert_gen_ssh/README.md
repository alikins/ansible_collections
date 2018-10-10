# Ansible module: ansible.module_panos_cert_gen_ssh


generates a self-signed certificate using SSH protocol with SSH key

## Description

This module generates a self-signed certificate that can be used by GlobalProtect client, SSL connector, or
otherwise. Root certificate must be preset on the system first. This module depends on paramiko for ssh.

## Requirements

TODO

## Arguments

``` json
{
    "cert_cn": "{'description': ['Certificate CN (common name) embedded in the certificate signature.'], 'required': True}",
    "cert_friendly_name": "{'description': ['Human friendly certificate name (not CN but just a friendly name).'], 'required': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device being configured.'], 'required': True}",
    "key_filename": "{'description': ['Location of the filename that is used for the auth. Either I(key_filename) or I(password) is required.'], 'required': True}",
    "password": "{'description': ['Password credentials to use for auth. Either I(key_filename) or I(password) is required.'], 'required': True}",
    "rsa_nbits": "{'description': ['Number of bits used by the RSA algorithm for the certificate generation.'], 'default': '2048'}",
    "signed_by": "{'description': ['Undersigning authority (CA) that MUST already be presents on the device.'], 'required': True}",
}
```

## Examples


``` yaml

# Generates a new self-signed certificate using ssh
- name: generate self signed certificate
  panos_cert_gen_ssh:
    ip_address: "192.168.1.1"
    password: "paloalto"
    cert_cn: "1.1.1.1"
    cert_friendly_name: "test123"
    signed_by: "root-ca"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
