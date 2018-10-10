# Ansible module: ansible.module_vertica_role


Adds or removes Vertica database roles and assigns roles to them

## Description

Adds or removes Vertica database role and, optionally, assign other roles.

## Requirements

TODO

## Arguments

``` json
{
    "assigned_roles": "{'description': ['Comma separated list of roles to assign to the role.'], 'aliases': ['assigned_role']}",
    "cluster": "{'description': ['Name of the Vertica cluster.'], 'default': 'localhost'}",
    "db": "{'description': ['Name of the Vertica database.']}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_user": "{'description': ['The username used to authenticate with.'], 'default': 'dbadmin'}",
    "name": "{'description': ['Name of the role to add or remove.'], 'required': True}",
    "port": "{'description': ['Vertica cluster port to connect to.'], 'default': 5433}",
    "state": "{'description': ['Whether to create C(present), drop C(absent) or lock C(locked) a role.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: creating a new vertica role
  vertica_role: name=role_name db=db_name state=present

- name: creating a new vertica role with other role assigned
  vertica_role: name=role_name assigned_role=other_role_name state=present

```

## License

TODO

## Author Information
  - ['Dariusz Owczarek (@dareko)']
