# Ansible module: ansible.module_tower_user


create, update, or destroy Ansible Tower user

## Description

Create, update, or destroy Ansible Tower users. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "auditor": "{'description': ['User is a system wide auditor.'], 'type': 'bool', 'default': False}",
    "email": "{'description': ['Email address of the user.'], 'required': True}",
    "first_name": "{'description': ['First name of the user.']}",
    "last_name": "{'description': ['Last name of the user.']}",
    "password": "{'description': ['Password of the user.']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "superuser": "{'description': ['User is a system wide administator.'], 'type': 'bool', 'default': False}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username of the user.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Add tower user
  tower_user:
    username: jdoe
    password: foobarbaz
    email: jdoe@example.org
    first_name: John
    last_name: Doe
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
