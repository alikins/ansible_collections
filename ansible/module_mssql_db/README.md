# Ansible module: ansible.module_mssql_db


Add or remove MSSQL databases from a remote host

## Description

Add or remove MSSQL databases from a remote host.

## Requirements

TODO

## Arguments

``` json
{
    "autocommit": "{'description': ["Automatically commit the change only if the import succeed. Sometimes it is necessary to use autocommit=true, since some content can't be changed within a transaction."], 'type': 'bool', 'default': False}",
    "login_host": "{'description': ['Host running the database']}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_port": "{'description': ['Port of the MSSQL server. Requires login_host be defined as other then localhost if login_port is used'], 'default': 1433}",
    "login_user": "{'description': ['The username used to authenticate with']}",
    "name": "{'description': ['name of the database to add or remove'], 'required': True, 'aliases': ['db']}",
    "state": "{'description': ['The database state'], 'default': 'present', 'choices': ['present', 'absent', 'import']}",
    "target": "{'description': ['Location, on the remote host, of the dump file to read from or write to. Uncompressed SQL files (C(.sql)) files are supported.']}",
}
```

## Examples


``` yaml

# Create a new database with name 'jackdata'
- mssql_db:
    name: jackdata
    state: present

# Copy database dump file to remote host and restore it to database 'my_db'
- copy:
    src: dump.sql
    dest: /tmp

- mssql_db:
    name: my_db
    state: import
    target: /tmp/dump.sql

```

## License

TODO

## Author Information
  - ['Vedit Firat Arig (@vedit)']
