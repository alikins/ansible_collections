# Ansible module: ansible.module_udm_user


Manage posix users on a univention corporate server

## Description

This module allows to manage posix users on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## Requirements

TODO

## Arguments

``` json
{
    "birthday": "{'description': ['Birthday']}",
    "city": "{'description': ['City of users business address.']}",
    "country": "{'description': ['Country of users business address.']}",
    "department_number": "{'description': ['Department number of users business address.'], 'aliases': ['departmentNumber']}",
    "description": "{'description': ['Description (not gecos)']}",
    "display_name": "{'description': ['Display name (not gecos)'], 'aliases': ['displayName']}",
    "email": "{'default': [], 'description': ['A list of e-mail addresses.']}",
    "employee_number": "{'description': ['Employee number'], 'aliases': ['employeeNumber']}",
    "employee_type": "{'description': ['Employee type'], 'aliases': ['employeeType']}",
    "firstname": "{'description': ['First name. Required if C(state=present).']}",
    "gecos": "{'description': ['GECOS']}",
    "groups": "{'default': [], 'description': ['POSIX groups, the LDAP DNs of the groups will be found with the LDAP filter for each group as $GROUP: C((&(objectClass=posixGroup)(cn=$GROUP))).']}",
    "home_share": "{'description': ['Home NFS share. Must be a LDAP DN, e.g. C(cn=home,cn=shares,ou=school,dc=example,dc=com).'], 'aliases': ['homeShare']}",
    "home_share_path": "{'description': ['Path to home NFS share, inside the homeShare.'], 'aliases': ['homeSharePath']}",
    "home_telephone_number": "{'default': [], 'description': ['List of private telephone numbers.'], 'aliases': ['homeTelephoneNumber']}",
    "homedrive": "{'description': ['Windows home drive, e.g. C("H:").']}",
    "lastname": "{'description': ['Last name. Required if C(state=present).']}",
    "mail_alternative_address": "{'default': [], 'description': ['List of alternative e-mail addresses.'], 'aliases': ['mailAlternativeAddress']}",
    "mail_home_server": "{'description': ['FQDN of mail server'], 'aliases': ['mailHomeServer']}",
    "mail_primary_address": "{'description': ['Primary e-mail address'], 'aliases': ['mailPrimaryAddress']}",
    "mobile_telephone_number": "{'default': [], 'description': ['Mobile phone number'], 'aliases': ['mobileTelephoneNumber']}",
    "organisation": "{'description': ['Organisation'], 'aliases': ['organization']}",
    "ou": "{'default': '', 'description': ['Organizational Unit inside the LDAP Base DN, e.g. C(school) for LDAP OU C(ou=school,dc=example,dc=com).']}",
    "override_pw_history": "{'type': 'bool', 'default': False, 'description': ['Override password history'], 'aliases': ['overridePWHistory']}",
    "override_pw_length": "{'type': 'bool', 'default': False, 'description': ['Override password check'], 'aliases': ['overridePWLength']}",
    "pager_telephonenumber": "{'default': [], 'description': ['List of pager telephone numbers.'], 'aliases': ['pagerTelephonenumber']}",
    "password": "{'description': ['Password. Required if C(state=present).']}",
    "phone": "{'description': ['List of telephone numbers.']}",
    "position": "{'default': '', 'description': ['Define the whole position of users object inside the LDAP tree, e.g. C(cn=employee,cn=users,ou=school,dc=example,dc=com).']}",
    "postcode": "{'description': ['Postal code of users business address.']}",
    "primary_group": "{'default': 'cn=Domain Users,cn=groups,$LDAP_BASE_DN', 'description': ['Primary group. This must be the group LDAP DN.'], 'aliases': ['primaryGroup']}",
    "profilepath": "{'description': ['Windows profile directory']}",
    "pwd_change_next_login": "{'choices': ['0', '1'], 'description': ['Change password on next login.'], 'aliases': ['pwdChangeNextLogin']}",
    "room_number": "{'description': ['Room number of users business address.'], 'aliases': ['roomNumber']}",
    "samba_privileges": "{'description': ['Samba privilege, like allow printer administration, do domain join.'], 'aliases': ['sambaPrivileges']}",
    "samba_user_workstations": "{'description': ['Allow the authentication only on this Microsoft Windows host.'], 'aliases': ['sambaUserWorkstations']}",
    "sambahome": "{'description': ["Windows home path, e.g. C('\\\\$FQDN\\$USERNAME')."]}",
    "scriptpath": "{'description': ['Windows logon script.']}",
    "secretary": "{'default': [], 'description': ['A list of superiors as LDAP DNs.']}",
    "serviceprovider": "{'default': [], 'description': ['Enable user for the following service providers.']}",
    "shell": "{'default': '/bin/bash', 'description': ['Login shell']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the user is present or not.']}",
    "street": "{'description': ['Street of users business address.']}",
    "subpath": "{'default': 'cn=users', 'description': ['LDAP subpath inside the organizational unit, e.g. C(cn=teachers,cn=users) for LDAP container C(cn=teachers,cn=users,dc=example,dc=com).']}",
    "title": "{'description': ['Title, e.g. C(Prof.).']}",
    "unixhome": "{'default': '/home/$USERNAME', 'description': ['Unix home directory']}",
    "update_password": "{'default': 'always', 'description': ['C(always) will update passwords if they differ. C(on_create) will only set the password for newly created users.'], 'version_added': '2.3'}",
    "userexpiry": "{'default': 'Today + 1 year', 'description': ['Account expiry date, e.g. C(1999-12-31).']}",
    "username": "{'required': True, 'description': ['User name'], 'aliases': ['name']}",
}
```

## Examples


``` yaml

# Create a user on a UCS
- udm_user:
    name: FooBar
    password: secure_password
    firstname: Foo
    lastname: Bar

# Create a user with the DN
# C(uid=foo,cn=teachers,cn=users,ou=school,dc=school,dc=example,dc=com)
- udm_user:
    name: foo
    password: secure_password
    firstname: Foo
    lastname: Bar
    ou: school
    subpath: 'cn=teachers,cn=users'
# or define the position
- udm_user:
    name: foo
    password: secure_password
    firstname: Foo
    lastname: Bar
    position: 'cn=teachers,cn=users,ou=school,dc=school,dc=example,dc=com'

```

## License

TODO

## Author Information
  - ['Tobias Rueetschi (@2-B)']
