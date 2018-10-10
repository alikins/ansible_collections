# Ansible module: ansible.module_win_msg


Sends a message to logged in users on Windows hosts

## Description

Wraps the msg.exe command in order to send messages to Windows hosts.

## Requirements

TODO

## Arguments

``` json
{
    "display_seconds": "{'description': ['How long to wait for receiver to acknowledge message, in seconds.'], 'type': 'int', 'default': 10}",
    "msg": "{'description': ['The text of the message to be displayed.', 'The message must be less than 256 characters.'], 'default': 'Hello world!'}",
    "to": "{'description': ['Who to send the message to. Can be a username, sessionname or sessionid.'], 'default': '*'}",
    "wait": "{'description': ["Whether to wait for users to respond.  Module will only wait for the number of seconds specified in display_seconds or 10 seconds if not specified. However, if I(wait) is C(yes), the message is sent to each logged on user in turn, waiting for the user to either press 'ok' or for the timeout to elapse before moving on to the next user."], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Warn logged in users of impending upgrade
  win_msg:
    display_seconds: 60
    msg: Automated upgrade about to start.  Please save your work and log off before {{ deployment_start_time }}

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
