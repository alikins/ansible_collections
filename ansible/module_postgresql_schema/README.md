# Ansible module: ansible.module_postgresql_schema


Add or remove PostgreSQL schema from a remote host

## Description

Add or remove PostgreSQL schema from a remote host.

## Requirements

TODO

## Arguments

``` json
{
    "database": "{'description': ['Name of the database to connect to.'], 'default': 'postgres'}",
    "login_host": "{'description': ['Host running the database.'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_unix_socket": "{'description': ['Path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['The username used to authenticate with.']}",
    "name": "{'description': ['Name of the schema to add or remove.'], 'required': True}",
    "owner": "{'description': ['Name of the role to set as owner of the schema.']}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "state": "{'description': ['The schema state.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Create a new schema with name "acme"
- postgresql_schema:
    name: acme

# Create a new schema "acme" with a user "bob" who will own it
- postgresql_schema:
    name: acme
    owner: bob


```

## License

TODO

## Author Information
  - ['Flavien Chantelot (@Dorn-) <contact@flavien.io>']
