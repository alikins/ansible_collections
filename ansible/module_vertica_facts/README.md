# Ansible module: ansible.module_vertica_facts


Gathers Vertica database facts

## Description

Gathers Vertica database facts.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['Name of the cluster running the schema.'], 'default': 'localhost'}",
    "db": "{'description': ['Name of the database running the schema.']}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_user": "{'description': ['The username used to authenticate with.'], 'default': 'dbadmin'}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5433}",
}
```

## Examples


``` yaml

- name: gathering vertica facts
  vertica_facts: db=db_name

```

## License

TODO

## Author Information
  - ['Dariusz Owczarek (@dareko)']
