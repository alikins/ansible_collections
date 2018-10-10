# Ansible module: ansible.module_webfaction_db


Add or remove a database on Webfaction

## Description

Add or remove a database on a Webfaction host. Further documentation at https://github.com/quentinsf/ansible-webfaction.

## Requirements

TODO

## Arguments

``` json
{
    "login_name": "{'description': ['The webfaction account to use'], 'required': True}",
    "login_password": "{'description': ['The webfaction password to use'], 'required': True}",
    "machine": "{'description': ['The machine name to use (optional for accounts with only one machine)']}",
    "name": "{'description': ['The name of the database'], 'required': True}",
    "password": "{'description': ['The password for the new database user.']}",
    "state": "{'description': ['Whether the database should exist'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['The type of database to create.'], 'required': True, 'choices': ['mysql', 'postgresql']}",
}
```

## Examples


``` yaml

  # This will also create a default DB user with the same
  # name as the database, and the specified password.

  - name: Create a database
    webfaction_db:
      name: "{{webfaction_user}}_db1"
      password: mytestsql
      type: mysql
      login_name: "{{webfaction_user}}"
      login_password: "{{webfaction_passwd}}"
      machine: "{{webfaction_machine}}"

  # Note that, for symmetry's sake, deleting a database using
  # 'state: absent' will also delete the matching user.


```

## License

TODO

## Author Information
  - ['Quentin Stafford-Fraser (@quentinsf)']
