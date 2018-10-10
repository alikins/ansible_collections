# Ansible module: ansible.module_logentries_msg


Send a message to logentries

## Description

Send a message to logentries

## Requirements

TODO

## Arguments

``` json
{
    "api": "{'description': ['API endpoint'], 'default': 'data.logentries.com'}",
    "msg": "{'description': ['The message body.'], 'required': True}",
    "port": "{'description': ['API endpoint port'], 'default': 80}",
    "token": "{'description': ['Log token.'], 'required': True}",
}
```

## Examples


``` yaml

- logentries_msg:
    token=00000000-0000-0000-0000-000000000000
    msg="{{ ansible_hostname }}"

```

## License

TODO

## Author Information
  - ['Jimmy Tang (@jcftang) <jimmy_tang@rapid7.com>']
