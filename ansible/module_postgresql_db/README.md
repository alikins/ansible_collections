# Ansible module: ansible.module_postgresql_db


Add or remove PostgreSQL databases from a remote host

## Description

Add or remove PostgreSQL databases from a remote host.

## Requirements

TODO

## Arguments

``` json
{
    "encoding": "{'description': ['Encoding of the database']}",
    "lc_collate": "{'description': ['Collation order (LC_COLLATE) to use in the database. Must match collation order of template database unless C(template0) is used as template.']}",
    "lc_ctype": "{'description': ['Character classification (LC_CTYPE) to use in the database (e.g. lower, upper, ...) Must match LC_CTYPE of template database unless C(template0) is used as template.']}",
    "login_host": "{'description': ['Host running the database']}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_unix_socket": "{'description': ['Path to a Unix domain socket for local connections']}",
    "login_user": "{'description': ['The username used to authenticate with'], 'default': 'postgres'}",
    "maintenance_db": "{'version_added': '2.5', 'description': ['The value specifies the initial database (which is also called as maintenance DB) that Ansible connects to.'], 'default': 'postgres'}",
    "name": "{'description': ['name of the database to add or remove'], 'required': True, 'aliases': ['db']}",
    "owner": "{'description': ['Name of the role to set as owner of the database']}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "ssl_mode": "{'description': ['Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.', 'See https://www.postgresql.org/docs/current/static/libpq-ssl.html for more information on the modes.', 'Default of C(prefer) matches libpq default.'], 'default': 'prefer', 'choices': ['disable', 'allow', 'prefer', 'require', 'verify-ca', 'verify-full'], 'version_added': '2.3'}",
    "ssl_rootcert": "{'description': ['Specifies the name of a file containing SSL certificate authority (CA) certificate(s).', "If the file exists, the server's certificate will be verified to be signed by one of these authorities."], 'version_added': '2.3'}",
    "state": "{'description': ['The database state. present implies that the database should be created if necessary.\nabsent implies that the database should be removed if present.\ndump requires a target definition to which the database will be backed up.\n(Added in 2.4) restore also requires a target definition from which the database will be restored.\n(Added in 2.4) The format of the backup will be detected based on the target name.\nSupported compression formats for dump and restore are: .bz2, .gz, and .xz\nSupported formats for dump and restore are: .sql and .tar\n'], 'default': 'present', 'choices': ['present', 'absent', 'dump', 'restore']}",
    "target": "{'version_added': '2.4', 'description': ['File to back up or restore from. Used when state is "dump" or "restore"']}",
    "target_opts": "{'version_added': '2.4', 'description': ['Further arguments for pg_dump or pg_restore. Used when state is "dump" or "restore"']}",
    "template": "{'description': ['Template used to create the database']}",
}
```

## Examples


``` yaml

# Create a new database with name "acme"
- postgresql_db:
    name: acme

# Create a new database with name "acme" and specific encoding and locale
# settings. If a template different from "template0" is specified, encoding
# and locale settings must match those of the template.
- postgresql_db:
    name: acme
    encoding: UTF-8
    lc_collate: de_DE.UTF-8
    lc_ctype: de_DE.UTF-8
    template: template0

# Dump an existing database to a file
- postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql

# Dump an existing database to a file (with compression)
- postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql.gz

# Dump a single schema for an existing database
- postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql
    target_opts: "-n public"

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
