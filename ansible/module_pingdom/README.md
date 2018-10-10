# Ansible module: ansible.module_pingdom


Pause/unpause Pingdom alerts

## Description

This module will let you pause/unpause Pingdom alerts

## Requirements

TODO

## Arguments

``` json
{
    "checkid": "{'description': ['Pingdom ID of the check.'], 'required': True}",
    "key": "{'description': ['Pingdom API key.'], 'required': True}",
    "passwd": "{'description': ['Pingdom user password.'], 'required': True}",
    "state": "{'description': ['Define whether or not the check should be running or paused.'], 'required': True, 'choices': ['running', 'paused']}",
    "uid": "{'description': ['Pingdom user ID.'], 'required': True}",
}
```

## Examples


``` yaml

# Pause the check with the ID of 12345.
- pingdom:
    uid: example@example.com
    passwd: password123
    key: apipassword123
    checkid: 12345
    state: paused

# Unpause the check with the ID of 12345.
- pingdom:
    uid: example@example.com
    passwd: password123
    key: apipassword123
    checkid: 12345
    state: running

```

## License

TODO

## Author Information
  - ['Dylan Silva (@thaumos)', 'Justin Johns']
  - ['Dylan Silva (@thaumos)', 'Justin Johns']
