# Ansible module: ansible.module_postgresql_user


Adds or removes a users (roles) from a PostgreSQL database

## Description

Add or remove PostgreSQL users (roles) from a remote host and, optionally, grant the users access to an existing database or tables.
The fundamental function of the module is to create, or delete, roles from a PostgreSQL cluster. Privilege assignment, or removal, is an optional step, which works on one database at a time. This allows for the module to be called several times in the same module to modify the permissions on different databases, or to grant permissions to already existing users.
A user cannot be removed until all the privileges have been stripped from the user. In such situation, if the module tries to remove the user it will fail. To avoid this from happening the fail_on_user option signals the module to try to remove the user, but if not possible keep going; the module will report if changes happened and separately if the user was removed or not.

## Requirements

TODO

## Arguments

``` json
{
    "conn_limit": "{'description': ['Specifies the user connection limit.'], 'version_added': '2.4'}",
    "db": "{'description': ['Name of database where permissions will be granted.']}",
    "encrypted": "{'description': ['Whether the password is stored hashed in the database. Passwords can be passed already hashed or unhashed, and postgresql ensures the stored password is hashed when C(encrypted) is set.', "Note: Postgresql 10 and newer doesn't support unhashed passwords.", 'Previous to Ansible 2.6, this was C(no) by default.'], 'default': True, 'type': 'bool', 'version_added': '1.4'}",
    "expires": "{'description': ["The date at which the user's password is to expire.", "If set to C('infinity'), user's password never expire.", 'Note that this value should be a valid SQL date and time type.'], 'version_added': '1.4'}",
    "fail_on_user": "{'description': ["If C(yes), fail when user can't be removed. Otherwise just log and continue."], 'default': True, 'type': 'bool'}",
    "login_host": "{'description': ['Host running PostgreSQL.'], 'default': 'localhost'}",
    "login_password": "{'description': ['Password used to authenticate with PostgreSQL.']}",
    "login_unix_socket": "{'description': ['Path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['User (role) used to authenticate with PostgreSQL.'], 'default': 'postgres'}",
    "name": "{'description': ['Name of the user (role) to add or remove.'], 'required': True}",
    "no_password_changes": "{'description': ["If C(yes), don't inspect database for password changes. Effective when C(pg_authid) is not accessible (such as AWS RDS). Otherwise, make password changes as necessary."], 'default': False, 'type': 'bool', 'version_added': '2.0'}",
    "password": "{'description': ["Set the user's password, before 1.4 this was required.", 'Password can be passed unhashed or hashed (MD5-hashed).', 'Unhashed password will automatically be hashed when saved into the database if C(encrypted) parameter is set, otherwise it will be save in plain text format.', 'When passing a hashed password it must be generated with the format C(\'str["md5"] + md5[ password + username ]\'), resulting in a total of 35 characters. An easy way to do this is C(echo "md5$(echo -n \'verysecretpasswordJOE\' | md5sum | awk \'{print $1}\')").', 'Note that if the provided password string is already in MD5-hashed format, then it is used as-is, regardless of C(encrypted) parameter.']}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "priv": "{'description': ['PostgreSQL privileges string in the format: C(table:priv1,priv2).']}",
    "role_attr_flags": "{'description': ['PostgreSQL role attributes string in the format: CREATEDB,CREATEROLE,SUPERUSER.', "Note that '[NO]CREATEUSER' is deprecated."], 'choices': ['[NO]SUPERUSER', '[NO]CREATEROLE', '[NO]CREATEDB', '[NO]INHERIT', '[NO]LOGIN', '[NO]REPLICATION', '[NO]BYPASSRLS']}",
    "ssl_mode": "{'description': ['Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.', 'See U(https://www.postgresql.org/docs/current/static/libpq-ssl.html) for more information on the modes.', 'Default of C(prefer) matches libpq default.'], 'default': 'prefer', 'choices': ['disable', 'allow', 'prefer', 'require', 'verify-ca', 'verify-full'], 'version_added': '2.3'}",
    "ssl_rootcert": "{'description': ["Specifies the name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities."], 'version_added': '2.3'}",
    "state": "{'description': ['The user (role) state.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Create django user and grant access to database and products table
- postgresql_user:
    db: acme
    name: django
    password: ceec4eif7ya
    priv: "CONNECT/products:ALL"
    expires: "Jan 31 2020"

# Create rails user, set its password (MD5-hashed) and grant privilege to create other
# databases and demote rails from super user status
- postgresql_user:
    name: rails
    password: md59543f1d82624df2b31672ec0f7050460
    role_attr_flags: CREATEDB,NOSUPERUSER

# Remove test user privileges from acme
- postgresql_user:
    db: acme
    name: test
    priv: "ALL/products:ALL"
    state: absent
    fail_on_user: no

# Remove test user from test database and the cluster
- postgresql_user:
    db: test
    name: test
    priv: ALL
    state: absent

# Set user's password with no expire date
- postgresql_user:
    db: acme
    name: django
    password: mysupersecretword
    priv: "CONNECT/products:ALL"
    expires: infinity

# Example privileges string format
# INSERT,UPDATE/table:SELECT/anothertable:ALL

# Remove an existing user's password
- postgresql_user:
    db: test
    user: test
    password: ""

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
