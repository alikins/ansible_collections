# Ansible module: ansible.module_vertica_configuration


Updates Vertica configuration parameters

## Description

Updates Vertica configuration parameters.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['Name of the Vertica cluster.'], 'default': 'localhost'}",
    "db": "{'description': ['Name of the Vertica database.']}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_user": "{'description': ['The username used to authenticate with.'], 'default': 'dbadmin'}",
    "name": "{'description': ['Name of the parameter to update.'], 'required': True, 'aliases': ['parameter']}",
    "port": "{'description': ['Vertica cluster port to connect to.'], 'default': 5433}",
    "value": "{'description': ['Value of the parameter to be set.'], 'required': True}",
}
```

## Examples


``` yaml

- name: updating load_balance_policy
  vertica_configuration: name=failovertostandbyafter value='8 hours'

```

## License

TODO

## Author Information
  - ['Dariusz Owczarek (@dareko)']
