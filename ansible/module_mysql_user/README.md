# Ansible module: ansible.module_mysql_user


Adds or removes a user from a MySQL database

## Description

Adds or removes a user from a MySQL database.

## Requirements

TODO

## Arguments

``` json
{
    "append_privs": "{'description': ['Append the privileges defined by priv to the existing ones for this user instead of overwriting existing ones.'], 'type': 'bool', 'default': False, 'version_added': '1.4'}",
    "check_implicit_admin": "{'description': ['Check if mysql allows login as root/nopassword before trying supplied credentials.'], 'type': 'bool', 'default': False, 'version_added': '1.3'}",
    "config_file": "{'description': ['Specify a config file from which user and password are to be read.'], 'default': '~/.my.cnf', 'version_added': '2.0'}",
    "connect_timeout": "{'description': ['The connection timeout when connecting to the MySQL server.'], 'default': 30, 'version_added': '2.1'}",
    "encrypted": "{'description': ["Indicate that the 'password' field is a `mysql_native_password` hash"], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "host": "{'description': ["the 'host' part of the MySQL username"], 'default': 'localhost'}",
    "host_all": "{'description': ['override the host option, making ansible apply changes to all hostnames for a given user.  This option cannot be used when creating users'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "login_host": "{'description': ['Host running the database.'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_port": "{'description': ['Port of the MySQL server. Requires I(login_host) be defined as other then localhost if login_port is used.'], 'default': 3306}",
    "login_unix_socket": "{'description': ['The path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['The username used to authenticate with.']}",
    "name": "{'description': ['name of the user (role) to add or remove'], 'required': True}",
    "password": "{'description': ["set the user's password."]}",
    "priv": "{'description': ['MySQL privileges string in the format: C(db.table:priv1,priv2).', 'Multiple privileges can be specified by separating each one using a forward slash: C(db.table:priv/db.table:priv).', 'The format is based on MySQL C(GRANT) statement.', 'Database and table names can be quoted, MySQL-style.', 'If column privileges are used, the C(priv1,priv2) part must be exactly as returned by a C(SHOW GRANT) statement. If not followed, the module will always report changes. It includes grouping columns by permission (C(SELECT(col1,col2)) instead of C(SELECT(col1),SELECT(col2))).']}",
    "sql_log_bin": "{'description': ['Whether binary logging should be enabled or disabled for the connection.'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
    "ssl_ca": "{'version_added': '2.0', 'description': ['The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server.']}",
    "ssl_cert": "{'version_added': '2.0', 'description': ['The path to a client public key certificate.']}",
    "ssl_key": "{'version_added': '2.0', 'description': ['The path to the client private key.']}",
    "state": "{'description': ['Whether the user should exist.  When C(absent), removes the user.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'default': 'always', 'choices': ['always', 'on_create'], 'version_added': '2.0', 'description': ['C(always) will update passwords if they differ.  C(on_create) will only set the password for newly created users.']}",
}
```

## Examples


``` yaml

# Removes anonymous user account for localhost
- mysql_user:
    name: ''
    host: localhost
    state: absent

# Removes all anonymous user accounts
- mysql_user:
    name: ''
    host_all: yes
    state: absent

# Create database user with name 'bob' and password '12345' with all database privileges
- mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL'
    state: present

# Create database user with name 'bob' and previously hashed mysql native password '*EE0D72C1085C46C5278932678FBE2C6A782821B4' with all database privileges
- mysql_user:
    name: bob
    password: '*EE0D72C1085C46C5278932678FBE2C6A782821B4'
    encrypted: yes
    priv: '*.*:ALL'
    state: present

# Creates database user 'bob' and password '12345' with all database privileges and 'WITH GRANT OPTION'
- mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL,GRANT'
    state: present

# Modify user Bob to require SSL connections. Note that REQUIRESSL is a special privilege that should only apply to *.* by itself.
- mysql_user:
    name: bob
    append_privs: true
    priv: '*.*:REQUIRESSL'
    state: present

# Ensure no user named 'sally'@'localhost' exists, also passing in the auth credentials.
- mysql_user:
    login_user: root
    login_password: 123456
    name: sally
    state: absent

# Ensure no user named 'sally' exists at all
- mysql_user:
    name: sally
    host_all: yes
    state: absent

# Specify grants composed of more than one word
- mysql_user:
    name: replication
    password: 12345
    priv: "*.*:REPLICATION CLIENT"
    state: present

# Revoke all privileges for user 'bob' and password '12345'
- mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present

# Example privileges string format
# mydb.*:INSERT,UPDATE/anotherdb.*:SELECT/yetanotherdb.*:ALL

# Example using login_unix_socket to connect to server
- mysql_user:
    name: root
    password: abc123
    login_unix_socket: /var/run/mysqld/mysqld.sock

# Example of skipping binary logging while adding user 'bob'
- mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present
    sql_log_bin: no

# Example .my.cnf file for setting the root password
# [client]
# user=root
# password=n<_665{vS43y

```

## License

TODO

## Author Information
  - ['Jonathan Mainguy (@Jmainguy)']
