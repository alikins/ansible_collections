# Ansible module: ansible.module_campfire


Send a message to Campfire

## Description

Send a message to Campfire.
Messages with newlines will result in a "Paste" message being sent.

## Requirements

TODO

## Arguments

``` json
{
    "msg": "{'description': ['The message body.'], 'required': True}",
    "notify": "{'description': ['Send a notification sound before the message.'], 'required': False, 'choices': ['56k', 'bell', 'bezos', 'bueller', 'clowntown', 'cottoneyejoe', 'crickets', 'dadgummit', 'dangerzone', 'danielsan', 'deeper', 'drama', 'greatjob', 'greyjoy', 'guarantee', 'heygirl', 'horn', 'horror', 'inconceivable', 'live', 'loggins', 'makeitso', 'noooo', 'nyan', 'ohmy', 'ohyeah', 'pushit', 'rimshot', 'rollout', 'rumble', 'sax', 'secret', 'sexyback', 'story', 'tada', 'tmyk', 'trololo', 'trombone', 'unix', 'vuvuzela', 'what', 'whoomp', 'yeah', 'yodel']}",
    "room": "{'description': ['Room number to which the message should be sent.'], 'required': True}",
    "subscription": "{'description': ['The subscription name to use.'], 'required': True}",
    "token": "{'description': ['API token.'], 'required': True}",
}
```

## Examples


``` yaml

- campfire:
    subscription: foo
    token: 12345
    room: 123
    msg: Task completed.

- campfire:
    subscription: foo
    token: 12345
    room: 123
    notify: loggins
    msg: Task completed ... with feeling.

```

## License

TODO

## Author Information
  - ['Adam Garside (@fabulops)']
