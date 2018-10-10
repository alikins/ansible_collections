# Ansible module: ansible.module_jabber


Send a message to jabber user or chat room

## Description

Send a message to jabber

## Requirements

TODO

## Arguments

``` json
{
    "encoding": "{'description': ['message encoding']}",
    "host": "{'description': ['host to connect, overrides user info']}",
    "msg": "{'description': ['The message body.'], 'required': True}",
    "password": "{'description': ['password for user to connect'], 'required': True}",
    "port": "{'description': ['port to connect to, overrides default'], 'default': 5222}",
    "to": "{'description': ['user ID or name of the room, when using room use a slash to indicate your nick.'], 'required': True}",
    "user": "{'description': ['User as which to connect'], 'required': True}",
}
```

## Examples


``` yaml

# send a message to a user
- jabber:
    user: mybot@example.net
    password: secret
    to: friend@example.net
    msg: Ansible task finished

# send a message to a room
- jabber:
    user: mybot@example.net
    password: secret
    to: mychaps@conference.example.net/ansiblebot
    msg: Ansible task finished

# send a message, specifying the host and port
- jabber:
    user: mybot@example.net
    host: talk.example.net
    port: 5223
    password: secret
    to: mychaps@example.net
    msg: Ansible task finished

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
