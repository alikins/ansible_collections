# Ansible module: ansible.module_postgresql_ext


Add or remove PostgreSQL extensions from a database

## Description

Add or remove PostgreSQL extensions from a database.

## Requirements

TODO

## Arguments

``` json
{
    "db": "{'description': ['name of the database to add or remove the extension to/from'], 'required': True}",
    "login_host": "{'description': ['Host running the database'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_user": "{'description': ['The username used to authenticate with']}",
    "name": "{'description': ['name of the extension to add or remove'], 'required': True}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "state": "{'description': ['The database extension state'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Adds postgis to the database "acme"
- postgresql_ext:
    name: postgis
    db: acme

```

## License

TODO

## Author Information
  - ['Daniel Schep (@dschep)']
