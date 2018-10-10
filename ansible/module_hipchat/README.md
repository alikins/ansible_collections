# Ansible module: ansible.module_hipchat


Send a message to Hipchat

## Description

Send a message to a Hipchat room, with options to control the formatting.

## Requirements

TODO

## Arguments

``` json
{
    "api": "{'description': ['API url if using a self-hosted hipchat server. For Hipchat API version 2 use the default URI with C(/v2) instead of C(/v1).'], 'default': 'https://api.hipchat.com/v1', 'version_added': '1.6.0'}",
    "color": "{'description': ['Background color for the message.'], 'default': 'yellow', 'choices': ['yellow', 'red', 'green', 'purple', 'gray', 'random']}",
    "from": "{'description': ['Name the message will appear to be sent from. Max length is 15 characters - above this it will be truncated.'], 'default': 'Ansible'}",
    "msg": "{'description': ['The message body.'], 'required': True}",
    "msg_format": "{'description': ['Message format.'], 'default': 'text', 'choices': ['text', 'html']}",
    "notify": "{'description': ['If true, a notification will be triggered for users in the room.'], 'type': 'bool', 'default': True}",
    "room": "{'description': ['ID or name of the room.'], 'required': True}",
    "token": "{'description': ['API token.'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

- hipchat:
    room: notif
    msg: Ansible task finished

# Use Hipchat API version 2
- hipchat:
    api: https://api.hipchat.com/v2/
    token: OAUTH2_TOKEN
    room: notify
    msg: Ansible task finished

```

## License

TODO

## Author Information
  - ['Shirou Wakayama (@shirou)', 'Paul Bourdel (@pb8226)']
  - ['Shirou Wakayama (@shirou)', 'Paul Bourdel (@pb8226)']
