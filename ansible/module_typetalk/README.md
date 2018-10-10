# Ansible module: ansible.module_typetalk


Send a message to typetalk

## Description

Send a message to typetalk using typetalk API

## Requirements

TODO

## Arguments

``` json
{
    "client_id": "{'description': ['OAuth2 client ID'], 'required': True}",
    "client_secret": "{'description': ['OAuth2 client secret'], 'required': True}",
    "msg": "{'description': ['message body'], 'required': True}",
    "topic": "{'description': ['topic id to post message'], 'required': True}",
}
```

## Examples


``` yaml

- typetalk:
    client_id: 12345
    client_secret: 12345
    topic: 1
    msg: install completed

```

## License

TODO

## Author Information
  - ['Takashi Someda (@tksmd)']
