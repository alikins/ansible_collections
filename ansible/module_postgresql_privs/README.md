# Ansible module: ansible.module_postgresql_privs


Grant or revoke privileges on PostgreSQL database objects

## Description

Grant or revoke privileges on PostgreSQL database objects.
This module is basically a wrapper around most of the functionality of PostgreSQL's GRANT and REVOKE statements with detection of changes (GRANT/REVOKE I(privs) ON I(type) I(objs) TO/FROM I(roles))

## Requirements

TODO

## Arguments

``` json
{
    "database": "{'description': ['Name of database to connect to.', 'Alias: I(db)'], 'required': True}",
    "grant_option": "{'description': ['Whether C(role) may grant/revoke the specified privileges/group memberships to others.', 'Set to C(no) to revoke GRANT OPTION, leave unspecified to make no changes.', 'I(grant_option) only has an effect if I(state) is C(present).', 'Alias: I(admin_option)'], 'type': 'bool'}",
    "host": "{'description': ['Database host address. If unspecified, connect via Unix socket.', 'Alias: I(login_host)']}",
    "login": "{'description': ['The username to authenticate with.', 'Alias: I(login_user)'], 'default': 'postgres'}",
    "login_host": "{'description': ['Host running the database']}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_unix_socket": "{'description': ['Path to a Unix domain socket for local connections']}",
    "login_user": "{'description': ['The username used to authenticate with'], 'default': 'postgres'}",
    "objs": "{'description': ['Comma separated list of database objects to set privileges on.', 'If I(type) is C(table) or C(sequence), the special value C(ALL_IN_SCHEMA) can be provided instead to specify all database objects of type I(type) in the schema specified via I(schema). (This also works with PostgreSQL < 9.0.)', 'If I(type) is C(database), this parameter can be omitted, in which case privileges are set for the database specified via I(database).', 'If I(type) is I(function), colons (":") in object names will be replaced with commas (needed to specify function signatures, see examples)', 'Alias: I(obj)']}",
    "password": "{'description': ['The password to authenticate with.', 'Alias: I(login_password))']}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "privs": "{'description': ['Comma separated list of privileges to grant/revoke.', 'Alias: I(priv)']}",
    "roles": "{'description': ['Comma separated list of role (user/group) names to set permissions for.', 'The special value C(PUBLIC) can be provided instead to set permissions for the implicitly defined PUBLIC group.', 'Alias: I(role)'], 'required': True}",
    "schema": "{'description': ['Schema that contains the database objects specified via I(objs).', 'May only be provided if I(type) is C(table), C(sequence) or C(function). Defaults to  C(public) in these cases.']}",
    "ssl_mode": "{'description': ['Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.', 'See https://www.postgresql.org/docs/current/static/libpq-ssl.html for more information on the modes.', 'Default of C(prefer) matches libpq default.'], 'default': 'prefer', 'choices': ['disable', 'allow', 'prefer', 'require', 'verify-ca', 'verify-full'], 'version_added': '2.3'}",
    "ssl_rootcert": "{'description': ["Specifies the name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities."], 'version_added': '2.3'}",
    "state": "{'description': ['If C(present), the specified privileges are granted, if C(absent) they are revoked.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['Type of database object to set privileges on.', 'The `default_prives` choice is available starting at version 2.7.'], 'default': 'table', 'choices': ['table', 'sequence', 'function', 'database', 'schema', 'language', 'tablespace', 'group', 'default_privs']}",
    "unix_socket": "{'description': ['Path to a Unix domain socket for local connections.', 'Alias: I(login_unix_socket)']}",
}
```

## Examples


``` yaml

# On database "library":
# GRANT SELECT, INSERT, UPDATE ON TABLE public.books, public.authors
# TO librarian, reader WITH GRANT OPTION
- postgresql_privs:
    database: library
    state: present
    privs: SELECT,INSERT,UPDATE
    type: table
    objs: books,authors
    schema: public
    roles: librarian,reader
    grant_option: yes

# Same as above leveraging default values:
- postgresql_privs:
    db: library
    privs: SELECT,INSERT,UPDATE
    objs: books,authors
    roles: librarian,reader
    grant_option: yes

# REVOKE GRANT OPTION FOR INSERT ON TABLE books FROM reader
# Note that role "reader" will be *granted* INSERT privilege itself if this
# isn't already the case (since state: present).
- postgresql_privs:
    db: library
    state: present
    priv: INSERT
    obj: books
    role: reader
    grant_option: no

# REVOKE INSERT, UPDATE ON ALL TABLES IN SCHEMA public FROM reader
# "public" is the default schema. This also works for PostgreSQL 8.x.
- postgresql_privs:
    db: library
    state: absent
    privs: INSERT,UPDATE
    objs: ALL_IN_SCHEMA
    role: reader

# GRANT ALL PRIVILEGES ON SCHEMA public, math TO librarian
- postgresql_privs:
    db: library
    privs: ALL
    type: schema
    objs: public,math
    role: librarian

# GRANT ALL PRIVILEGES ON FUNCTION math.add(int, int) TO librarian, reader
# Note the separation of arguments with colons.
- postgresql_privs:
    db: library
    privs: ALL
    type: function
    obj: add(int:int)
    schema: math
    roles: librarian,reader

# GRANT librarian, reader TO alice, bob WITH ADMIN OPTION
# Note that group role memberships apply cluster-wide and therefore are not
# restricted to database "library" here.
- postgresql_privs:
    db: library
    type: group
    objs: librarian,reader
    roles: alice,bob
    admin_option: yes

# GRANT ALL PRIVILEGES ON DATABASE library TO librarian
# Note that here "db: postgres" specifies the database to connect to, not the
# database to grant privileges on (which is specified via the "objs" param)
- postgresql_privs:
    db: postgres
    privs: ALL
    type: database
    obj: library
    role: librarian

# GRANT ALL PRIVILEGES ON DATABASE library TO librarian
# If objs is omitted for type "database", it defaults to the database
# to which the connection is established
- postgresql_privs:
    db: library
    privs: ALL
    type: database
    role: librarian

# Available since version 2.7
# ALTER DEFAULT PRIVILEGES ON DATABASE library TO librarian
# Objs must be set, ALL_DEFAULT to TABLES/SEQUENCES/TYPES/FUNCTIONS
# ALL_DEFAULT works only with privs=ALL
# For specific
- postgresql_privs:
    db: library
    objs: ALL_DEFAULT
    privs: ALL
    type: default_privs
    role: librarian
    grant_option: yes

# Available since version 2.7
# ALTER DEFAULT PRIVILEGES ON DATABASE library TO reader
# Objs must be set, ALL_DEFAULT to TABLES/SEQUENCES/TYPES/FUNCTIONS
# ALL_DEFAULT works only with privs=ALL
# For specific
- postgresql_privs:
    db: library
    objs: TABLES,SEQUENCES
    privs: SELECT
    type: default_privs
    role: reader

- postgresql_privs:
    db: library
    objs: TYPES
    privs: USAGE
    type: default_privs
    role: reader


```

## License

TODO

## Author Information
  - ['Bernhard Weitzhofer (@b6d)']
