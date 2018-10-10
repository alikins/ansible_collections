# Ansible module: ansible.module_mongodb_user


Adds or removes a user from a MongoDB database

## Description

Adds or removes a user from a MongoDB database.

## Requirements

TODO

## Arguments

``` json
{
    "database": "{'description': ['The name of the database to add/remove the user from'], 'required': True}",
    "login_database": "{'version_added': '2.0', 'description': ['The database where login credentials are stored']}",
    "login_host": "{'description': ['The host running the database'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with']}",
    "login_port": "{'description': ['The port to connect to'], 'default': 27017}",
    "login_user": "{'description': ['The username used to authenticate with']}",
    "name": "{'description': ['The name of the user to add or remove'], 'required': True, 'aliases': ['user']}",
    "password": "{'description': ['The password to use for the user']}",
    "replica_set": "{'version_added': '1.6', 'description': ['Replica set to connect to (automatically connects to primary for writes)']}",
    "roles": "{'version_added': '1.3', 'description': ["The database user roles valid values could either be one or more of the following strings: 'read', 'readWrite', 'dbAdmin', 'userAdmin', 'clusterAdmin', 'readAnyDatabase', 'readWriteAnyDatabase', 'userAdminAnyDatabase', 'dbAdminAnyDatabase'\n", "Or the following dictionary '{ db: DATABASE_NAME, role: ROLE_NAME }'.", 'This param requires pymongo 2.5+. If it is a string, mongodb 2.4+ is also required. If it is a dictionary, mongo 2.6+  is required.'], 'default': 'readWrite'}",
    "ssl": "{'version_added': '1.8', 'description': ['Whether to use an SSL connection when connecting to the database']}",
    "ssl_cert_reqs": "{'version_added': '2.2', 'description': ['Specifies whether a certificate is required from the other side of the connection, and whether it will be validated if provided.'], 'default': 'CERT_REQUIRED', 'choices': ['CERT_REQUIRED', 'CERT_OPTIONAL', 'CERT_NONE']}",
    "state": "{'description': ['The database user state'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'default': 'always', 'choices': ['always', 'on_create'], 'version_added': '2.1', 'description': ['C(always) will update passwords if they differ.  C(on_create) will only set the password for newly created users.']}",
}
```

## Examples


``` yaml

# Create 'burgers' database user with name 'bob' and password '12345'.
- mongodb_user:
    database: burgers
    name: bob
    password: 12345
    state: present

# Create a database user via SSL (MongoDB must be compiled with the SSL option and configured properly)
- mongodb_user:
    database: burgers
    name: bob
    password: 12345
    state: present
    ssl: True

# Delete 'burgers' database user with name 'bob'.
- mongodb_user:
    database: burgers
    name: bob
    state: absent

# Define more users with various specific roles (if not defined, no roles is assigned, and the user will be added via pre mongo 2.2 style)
- mongodb_user:
    database: burgers
    name: ben
    password: 12345
    roles: read
    state: present
- mongodb_user:
    database: burgers
    name: jim
    password: 12345
    roles: readWrite,dbAdmin,userAdmin
    state: present
- mongodb_user:
    database: burgers
    name: joe
    password: 12345
    roles: readWriteAnyDatabase
    state: present

# add a user to database in a replica set, the primary server is automatically discovered and written to
- mongodb_user:
    database: burgers
    name: bob
    replica_set: belcher
    password: 12345
    roles: readWriteAnyDatabase
    state: present

# add a user 'oplog_reader' with read only access to the 'local' database on the replica_set 'belcher'. This is useful for oplog access (MONGO_OPLOG_URL).
# please notice the credentials must be added to the 'admin' database because the 'local' database is not syncronized and can't receive user credentials
# To login with such user, the connection string should be MONGO_OPLOG_URL="mongodb://oplog_reader:oplog_reader_password@server1,server2/local?authSource=admin"
# This syntax requires mongodb 2.6+ and pymongo 2.5+
- mongodb_user:
    login_user: root
    login_password: root_password
    database: admin
    user: oplog_reader
    password: oplog_reader_password
    state: present
    replica_set: belcher
    roles:
      - db: local
        role: read


```

## License

TODO

## Author Information
  - ['Elliott Foster (@elliotttf)', 'Julien Thebault (@lujeni)']
  - ['Elliott Foster (@elliotttf)', 'Julien Thebault (@lujeni)']
