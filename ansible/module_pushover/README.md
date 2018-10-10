# Ansible module: ansible.module_pushover


Send notifications via https://pushover.net

## Description

Send notifications via pushover, to subscriber list of devices, and email addresses. Requires pushover app on devices.

## Requirements

TODO

## Arguments

``` json
{
    "app_token": "{'description': ['Pushover issued token identifying your pushover app.'], 'required': True}",
    "msg": "{'description': ['What message you wish to send.'], 'required': True}",
    "pri": "{'description': ['Message priority (see U(https://pushover.net) for details.)'], 'required': False}",
    "user_key": "{'description': ['Pushover issued authentication key for your user.'], 'required': True}",
}
```

## Examples


``` yaml

- pushover:
    msg: '{{ inventory_hostname }} has exploded in flames, It is now time to panic'
    app_token: wxfdksl
    user_key: baa5fe97f2c5ab3ca8f0bb59
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jim Richardson (@weaselkeeper)']
