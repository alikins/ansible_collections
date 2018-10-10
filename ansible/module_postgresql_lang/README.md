# Ansible module: ansible.module_postgresql_lang


Adds, removes or changes procedural languages with a PostgreSQL database

## Description

Adds, removes or changes procedural languages with a PostgreSQL database.
This module allows you to add a language, remote a language or change the trust relationship with a PostgreSQL database. The module can be used on the machine where executed or on a remote host.
When removing a language from a database, it is possible that dependencies prevent the database from being removed. In that case, you can specify casade to automatically drop objects that depend on the language (such as functions in the language). In case the language can't be deleted because it is required by the database system, you can specify fail_on_drop=no to ignore the error.
Be carefull when marking a language as trusted since this could be a potential security breach. Untrusted languages allow only users with the PostgreSQL superuser privilege to use this language to create new functions.

## Requirements

TODO

## Arguments

``` json
{
    "cascade": "{'description': ['when dropping a language, also delete object that depend on this language.', 'only used when C(state=absent).'], 'type': 'bool', 'default': False}",
    "db": "{'description': ['name of database where the language will be added, removed or changed']}",
    "fail_on_drop": "{'description': ['if C(yes), fail when removing a language. Otherwise just log and continue', 'in some cases, it is not possible to remove a language (used by the db-system). When         dependencies block the removal, consider using C(cascade).'], 'type': 'bool', 'default': True}",
    "force_trust": "{'description': ["marks the language as trusted, even if it's marked as untrusted in pg_pltemplate.", 'use with care!'], 'type': 'bool', 'default': False}",
    "lang": "{'description': ['name of the procedural language to add, remove or change'], 'required': True}",
    "login_host": "{'description': ['Host running PostgreSQL where you want to execute the actions.'], 'default': 'localhost'}",
    "login_password": "{'description': ['Password used to authenticate with PostgreSQL (must match C(login_user))']}",
    "login_user": "{'description': ['User used to authenticate with PostgreSQL'], 'default': 'postgres'}",
    "port": "{'description': ['Database port to connect to.'], 'default': 5432}",
    "state": "{'description': ['The state of the language for the selected database'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trust": "{'description': ['make this language trusted for the selected db'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Add language pltclu to database testdb if it doesn't exist:
- postgresql_lang db=testdb lang=pltclu state=present

# Add language pltclu to database testdb if it doesn't exist and mark it as trusted:
# Marks the language as trusted if it exists but isn't trusted yet
# force_trust makes sure that the language will be marked as trusted
- postgresql_lang:
    db: testdb
    lang: pltclu
    state: present
    trust: yes
    force_trust: yes

# Remove language pltclu from database testdb:
- postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent

# Remove language pltclu from database testdb and remove all dependencies:
- postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent
    cascade: yes

# Remove language c from database testdb but ignore errors if something prevents the removal:
- postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent
    fail_on_drop: no

```

## License

TODO

## Author Information
  - ['Jens Depuydt (@jensdepuydt)']
