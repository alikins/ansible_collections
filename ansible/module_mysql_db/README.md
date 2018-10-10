# Ansible module: ansible.module_mysql_db


Add or remove MySQL databases from a remote host

## Description

Add or remove MySQL databases from a remote host.

## Requirements

TODO

## Arguments

``` json
{
    "collation": "{'description': ['Collation mode (sorting). This only applies to new table/databases and does not update existing ones, this is a limitation of MySQL.']}",
    "config_file": "{'description': ['Specify a config file from which user and password are to be read.'], 'default': '~/.my.cnf', 'version_added': '2.0'}",
    "connect_timeout": "{'description': ['The connection timeout when connecting to the MySQL server.'], 'default': 30, 'version_added': '2.1'}",
    "encoding": "{'description': ['Encoding mode to use, examples include C(utf8) or C(latin1_swedish_ci)']}",
    "ignore_tables": "{'description': ['A list of table names that will be ignored in the dump of the form database_name.table_name'], 'required': False, 'default': [], 'version_added': '2.7'}",
    "login_host": "{'description': ['Host running the database.'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_port": "{'description': ['Port of the MySQL server. Requires I(login_host) be defined as other then localhost if login_port is used.'], 'default': 3306}",
    "login_unix_socket": "{'description': ['The path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['The username used to authenticate with.']}",
    "name": "{'description': ['name of the database to add or remove', 'name=all May only be provided if I(state) is C(dump) or C(import).', 'if name=all Works like --all-databases option for mysqldump (Added in 2.0)'], 'required': True, 'aliases': ['db']}",
    "quick": "{'description': ['Option used for dumping large tables'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
    "single_transaction": "{'description': ['Execute the dump in a single transaction'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "ssl_ca": "{'version_added': '2.0', 'description': ['The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server.']}",
    "ssl_cert": "{'version_added': '2.0', 'description': ['The path to a client public key certificate.']}",
    "ssl_key": "{'version_added': '2.0', 'description': ['The path to the client private key.']}",
    "state": "{'description': ['The database state'], 'default': 'present', 'choices': ['present', 'absent', 'dump', 'import']}",
    "target": "{'description': ['Location, on the remote host, of the dump file to read from or write to. Uncompressed SQL files (C(.sql)) as well as bzip2 (C(.bz2)), gzip (C(.gz)) and xz (Added in 2.0) compressed files are supported.']}",
}
```

## Examples


``` yaml

- name: Create a new database with name 'bobdata'
  mysql_db:
    name: bobdata
    state: present

# Copy database dump file to remote host and restore it to database 'my_db'
- name: Copy database dump file
  copy:
    src: dump.sql.bz2
    dest: /tmp
- name: Restore database
  mysql_db:
    name: my_db
    state: import
    target: /tmp/dump.sql.bz2

- name: Dump all databases to hostname.sql
  mysql_db:
    state: dump
    name: all
    target: /tmp/{{ inventory_hostname }}.sql

- name: Import file.sql similar to mysql -u <username> -p <password> < hostname.sql
  mysql_db:
    state: import
    name: all
    target: /tmp/{{ inventory_hostname }}.sql

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
