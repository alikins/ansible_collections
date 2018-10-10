# Ansible module: ansible.module_udm_group


Manage of the posix group

## Description

This module allows to manage user groups on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'required': False, 'description': ['Group description.']}",
    "name": "{'required': True, 'description': ['Name of the posix group.']}",
    "ou": "{'required': False, 'description': ['LDAP OU, e.g. school for LDAP OU C(ou=school,dc=example,dc=com).']}",
    "position": "{'required': False, 'description': ['define the whole ldap position of the group, e.g. C(cn=g123m-1A,cn=classes,cn=schueler,cn=groups,ou=schule,dc=example,dc=com).']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the group is present or not.']}",
    "subpath": "{'required': False, 'description': ['Subpath inside the OU, e.g. C(cn=classes,cn=students,cn=groups).']}",
}
```

## Examples


``` yaml

# Create a POSIX group
- udm_group:
    name: g123m-1A

# Create a POSIX group with the exact DN
# C(cn=g123m-1A,cn=classes,cn=students,cn=groups,ou=school,dc=school,dc=example,dc=com)
- udm_group:
    name: g123m-1A
    subpath: 'cn=classes,cn=students,cn=groups'
    ou: school
# or
- udm_group:
    name: g123m-1A
    position: 'cn=classes,cn=students,cn=groups,ou=school,dc=school,dc=example,dc=com'

```

## License

TODO

## Author Information
  - ['Tobias Rueetschi (@2-B)']
