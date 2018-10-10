# Ansible module: ansible.module_netscaler_ssl_certkey


Manage ssl cerificate keys

## Description

Manage ssl cerificate keys.

## Requirements

TODO

## Arguments

``` json
{
    "cert": "{'description': ["Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.", 'Minimum length = 1']}",
    "certkey": "{'description': ['Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at C(@), equals C(=), and hyphen C(-) characters. Cannot be changed after the certificate-key pair is created.', 'The following requirement applies only to the NetScaler CLI:', 'If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cert" or \'my cert\').', 'Minimum length = 1']}",
    "expirymonitor": "{'choices': ['enabled', 'disabled'], 'description': ['Issue an alert when the certificate is about to expire.']}",
    "inform": "{'choices': ['DER', 'PEM', 'PFX'], 'description': ['Input format of the certificate and the private-key files. The three formats supported by the appliance are:', 'PEM - Privacy Enhanced Mail', 'DER - Distinguished Encoding Rule', 'PFX - Personal Information Exchange.']}",
    "key": "{'description': ["Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.", 'Minimum length = 1']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "notificationperiod": "{'description': ['Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.', 'Minimum value = C(10)', 'Maximum value = C(100)']}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "passplain": "{'description': ['Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.', 'Minimum length = 1']}",
    "password": "{'description': ['Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format.']}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml


- name: Setup ssl certkey
  delegate_to: localhost
  netscaler_ssl_certkey:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 172.18.0.2

    certkey: certirificate_1
    cert: server.crt
    key: server.key
    expirymonitor: enabled
    notificationperiod: 30
    inform: PEM
    password: False
    passplain: somesecret

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
