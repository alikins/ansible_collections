# Ansible module: ansible.module_ldap_entry


Add or remove LDAP entries

## Description

Add or remove LDAP entries. This module only asserts the existence or non-existence of an LDAP entry, not its attributes. To assert the attribute values of an entry, see M(ldap_attr).

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['If I(state=present), attributes necessary to create an entry. Existing entries are never modified. To assert specific attribute values on an existing entry, use M(ldap_attr) module instead.']}",
    "bind_dn": "{'description': ["A DN to bind with. If this is omitted, we'll try a SASL bind with the EXTERNAL mechanism.", "If this is blank, we'll use an anonymous bind."]}",
    "bind_pw": "{'description': ['The password to use with I(bind_dn).']}",
    "dn": "{'required': True, 'description': ['The DN of the entry to add or remove.']}",
    "objectClass": "{'description': ['If I(state=present), value or list of values to use when creating the entry. It can either be a string or an actual list of strings.']}",
    "params": "{'description': ['List of options which allows to overwrite any of the task or the I(attributes) options. To remove an option, set the value of the option to C(null).']}",
    "server_uri": "{'default': 'ldapi:///', 'description': ['A URI to the LDAP server.', 'The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.']}",
    "start_tls": "{'default': False, 'type': 'bool', 'description': ["If true, we'll use the START_TLS LDAP extension."]}",
    "state": "{'description': ['The target state of the entry.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'default': True, 'type': 'bool', 'description': ['If set to C(no), SSL certificates will not be validated.', 'This should only be used on sites using self-signed certificates.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Make sure we have a parent entry for users
  ldap_entry:
    dn: ou=users,dc=example,dc=com
    objectClass: organizationalUnit

- name: Make sure we have an admin user
  ldap_entry:
    dn: cn=admin,dc=example,dc=com
    objectClass:
      - simpleSecurityObject
      - organizationalRole
    attributes:
      description: An LDAP administrator
      userPassword: "{SSHA}tabyipcHzhwESzRaGA7oQ/SDoBZQOGND"

- name: Get rid of an old entry
  ldap_entry:
    dn: ou=stuff,dc=example,dc=com
    state: absent
    server_uri: ldap://localhost/
    bind_dn: cn=admin,dc=example,dc=com
    bind_pw: password

#
# The same as in the previous example but with the authentication details
# stored in the ldap_auth variable:
#
# ldap_auth:
#   server_uri: ldap://localhost/
#   bind_dn: cn=admin,dc=example,dc=com
#   bind_pw: password
- name: Get rid of an old entry
  ldap_entry:
    dn: ou=stuff,dc=example,dc=com
    state: absent
    params: "{{ ldap_auth }}"

```

## License

TODO

## Author Information
  - ['Jiri Tyr (@jtyr)']
