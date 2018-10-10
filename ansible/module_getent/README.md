# Ansible module: ansible.module_getent


A wrapper to the unix getent utility

## Description

Runs getent against one of it's various databases and returns information into the host's facts, in a getent_<database> prefixed variable.

## Requirements

TODO

## Arguments

``` json
{
    "database": "{'description': ['The name of a getent database supported by the target system (passwd, group, hosts, etc).'], 'required': True}",
    "fail_key": "{'description': ['If a supplied key is missing this will make the task fail if C(yes).'], 'type': 'bool', 'default': True}",
    "key": "{'description': ['Key from which to return values from the specified database, otherwise the full contents are returned.'], 'default': ''}",
    "split": "{'description': ["Character used to split the database values into lists/arrays such as ':' or '\t', otherwise  it will try to pick one depending on the database."]}",
}
```

## Examples


``` yaml

# get root user info
- getent:
    database: passwd
    key: root
- debug:
    var: getent_passwd

# get all groups
- getent:
    database: group
    split: ':'
- debug:
    var: getent_group

# get all hosts, split by tab
- getent:
    database: hosts
- debug:
    var: getent_hosts

# get http service info, no error if missing
- getent:
    database: services
    key: http
    fail_key: False
- debug:
    var: getent_services

# get user password hash (requires sudo/root)
- getent:
    database: shadow
    key: www-data
    split: ':'
- debug:
    var: getent_shadow


```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
