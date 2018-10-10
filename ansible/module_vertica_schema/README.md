# Ansible module: ansible.module_vertica_schema


Adds or removes Vertica database schema and roles

## Description

Adds or removes Vertica database schema and, optionally, roles with schema access privileges.
A schema will not be removed until all the objects have been dropped.
In such a situation, if the module tries to remove the schema it will fail and only remove roles created for the schema if they have no dependencies.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['Name of the Vertica cluster.'], 'default': 'localhost'}",
    "create_roles": "{'description': ['Comma separated list of roles to create and grant usage and create access to the schema.'], 'aliases': ['create_role']}",
    "db": "{'description': ['Name of the Vertica database.']}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_user": "{'description': ['The username used to authenticate with.'], 'default': 'dbadmin'}",
    "name": "{'description': ['Name of the schema to add or remove.'], 'required': True}",
    "owner": "{'description': ['Name of the user to set as owner of the schema.']}",
    "port": "{'description': ['Vertica cluster port to connect to.'], 'default': 5433}",
    "state": "{'description': ['Whether to create C(present), or drop C(absent) a schema.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "usage_roles": "{'description': ['Comma separated list of roles to create and grant usage access to the schema.'], 'aliases': ['usage_role']}",
}
```

## Examples


``` yaml

- name: creating a new vertica schema
  vertica_schema: name=schema_name db=db_name state=present

- name: creating a new schema with specific schema owner
  vertica_schema: name=schema_name owner=dbowner db=db_name state=present

- name: creating a new schema with roles
  vertica_schema:
    name=schema_name
    create_roles=schema_name_all
    usage_roles=schema_name_ro,schema_name_rw
    db=db_name
    state=present

```

## License

TODO

## Author Information
  - ['Dariusz Owczarek (@dareko)']
