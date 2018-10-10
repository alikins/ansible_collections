# Ansible module: ansible.module_ldap_attr


Add or remove LDAP attribute values

## Description

Add or remove LDAP attribute values.

## Requirements

TODO

## Arguments

``` json
{
    "bind_dn": "{'description': ["A DN to bind with. If this is omitted, we'll try a SASL bind with the EXTERNAL mechanism.", "If this is blank, we'll use an anonymous bind."]}",
    "bind_pw": "{'description': ['The password to use with I(bind_dn).']}",
    "dn": "{'required': True, 'description': ['The DN of the entry to add or remove.']}",
    "name": "{'description': ['The name of the attribute to modify.'], 'required': True}",
    "server_uri": "{'default': 'ldapi:///', 'description': ['A URI to the LDAP server.', 'The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.']}",
    "start_tls": "{'default': False, 'type': 'bool', 'description': ["If true, we'll use the START_TLS LDAP extension."]}",
    "state": "{'description': ["The state of the attribute values. If C(present), all given values will be added if they're missing. If C(absent), all given values will be removed if present. If C(exact), the set of values will be forced to exactly those provided and no others. If I(state=exact) and I(value) is an empty list, all values for this attribute will be removed."], 'choices': ['present', 'absent', 'exact'], 'default': 'present'}",
    "validate_certs": "{'default': True, 'type': 'bool', 'description': ['If set to C(no), SSL certificates will not be validated.', 'This should only be used on sites using self-signed certificates.'], 'version_added': '2.4'}",
    "values": "{'description': ['The value(s) to add or remove. This can be a string or a list of strings. The complex argument format is required in order to pass a list of strings (see examples).'], 'required': True}",
}
```

## Examples


``` yaml

- name: Configure directory number 1 for example.com
  ldap_attr:
    dn: olcDatabase={1}hdb,cn=config
    name: olcSuffix
    values: dc=example,dc=com
    state: exact

# The complex argument format is required here to pass a list of ACL strings.
- name: Set up the ACL
  ldap_attr:
    dn: olcDatabase={1}hdb,cn=config
    name: olcAccess
    values:
      - >-
        {0}to attrs=userPassword,shadowLastChange
        by self write
        by anonymous auth
        by dn="cn=admin,dc=example,dc=com" write
        by * none'
      - >-
        {1}to dn.base="dc=example,dc=com"
        by dn="cn=admin,dc=example,dc=com" write
        by * read
    state: exact

- name: Declare some indexes
  ldap_attr:
    dn: olcDatabase={1}hdb,cn=config
    name: olcDbIndex
    values: "{{ item }}"
  with_items:
    - objectClass eq
    - uid eq

- name: Set up a root user, which we can use later to bootstrap the directory
  ldap_attr:
    dn: olcDatabase={1}hdb,cn=config
    name: "{{ item.key }}"
    values: "{{ item.value }}"
    state: exact
  with_dict:
    olcRootDN: cn=root,dc=example,dc=com
    olcRootPW: "{SSHA}tabyipcHzhwESzRaGA7oQ/SDoBZQOGND"

- name: Get rid of an unneeded attribute
  ldap_attr:
    dn: uid=jdoe,ou=people,dc=example,dc=com
    name: shadowExpire
    values: []
    state: exact
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
- name: Get rid of an unneeded attribute
  ldap_attr:
    dn: uid=jdoe,ou=people,dc=example,dc=com
    name: shadowExpire
    values: []
    state: exact
    params: "{{ ldap_auth }}"

```

## License

TODO

## Author Information
  - ['Jiri Tyr (@jtyr)']
