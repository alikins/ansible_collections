# Ansible module: ansible.module_vertica_user


Adds or removes Vertica database users and assigns roles

## Description

Adds or removes Vertica database user and, optionally, assigns roles.
A user will not be removed until all the dependencies have been dropped.
In such a situation, if the module tries to remove the user it will fail and only remove roles granted to the user.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['Name of the Vertica cluster.'], 'default': 'localhost'}",
    "db": "{'description': ['Name of the Vertica database.']}",
    "expired": "{'description': ["Sets the user's password expiration."]}",
    "ldap": "{'description': ['Set to true if users are authenticated via LDAP.', 'The user will be created with password expired and set to I($ldap$).']}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_user": "{'description': ['The username used to authenticate with.'], 'default': 'dbadmin'}",
    "name": "{'description': ['Name of the user to add or remove.'], 'required': True}",
    "password": "{'description': ["The user's password encrypted by the MD5 algorithm.", 'The password must be generated with the format C("md5" + md5[password + username]), resulting in a total of 35 characters. An easy way to do this is by querying the Vertica database with select \'md5\'||md5(\'<user_password><user_name>\').']}",
    "port": "{'description': ['Vertica cluster port to connect to.'], 'default': 5433}",
    "profile": "{'description': ["Sets the user's profile."]}",
    "resource_pool": "{'description': ["Sets the user's resource pool."]}",
    "roles": "{'description': ['Comma separated list of roles to assign to the user.'], 'aliases': ['role']}",
    "state": "{'description': ['Whether to create C(present), drop C(absent) or lock C(locked) a user.'], 'choices': ['present', 'absent', 'locked'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: creating a new vertica user with password
  vertica_user: name=user_name password=md5<encrypted_password> db=db_name state=present

- name: creating a new vertica user authenticated via ldap with roles assigned
  vertica_user:
    name=user_name
    ldap=true
    db=db_name
    roles=schema_name_ro
    state=present

```

## License

TODO

## Author Information
  - ['Dariusz Owczarek (@dareko)']
