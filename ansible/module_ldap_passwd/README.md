# Ansible module: ansible.module_ldap_passwd


Set passwords in LDAP

## Description

Set a password for an LDAP entry.  This module only asserts that a given password is valid for a given entry.  To assert the existence of an entry, see M(ldap_entry).

## Requirements

TODO

## Arguments

``` json
{
    "bind_dn": "{'description': ["A DN to bind with. If this is omitted, we'll try a SASL bind with the EXTERNAL mechanism.", "If this is blank, we'll use an anonymous bind."]}",
    "bind_pw": "{'description': ['The password to use with I(bind_dn).']}",
    "dn": "{'required': True, 'description': ['The DN of the entry to add or remove.']}",
    "passwd": "{'required': True, 'description': ['The (plaintext) password to be set for I(dn).']}",
    "server_uri": "{'default': 'ldapi:///', 'description': ['A URI to the LDAP server.', 'The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.']}",
    "start_tls": "{'default': False, 'type': 'bool', 'description': ["If true, we'll use the START_TLS LDAP extension."]}",
    "validate_certs": "{'default': True, 'type': 'bool', 'description': ['If set to C(no), SSL certificates will not be validated.', 'This should only be used on sites using self-signed certificates.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Set a password for the admin user
  ldap_passwd:
    dn: cn=admin,dc=example,dc=com
    passwd: "{{ vault_secret }}"

- name: Setting passwords in bulk
  ldap_passwd:
    dn: "{{ item.key }}"
    passwd: "{{ item.value }}"
  with_dict:
    alice: alice123123
    bob:   "|30b!"
    admin: "{{ vault_secret }}"

```

## License

TODO

## Author Information
  - ['Keller Fuchs (@KellerFuchs)']
