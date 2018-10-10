# Ansible module: ansible.module_flowdock


Send a message to a flowdock

## Description

Send a message to a flowdock team inbox or chat using the push API (see https://www.flowdock.com/api/team-inbox and https://www.flowdock.com/api/chat)

## Requirements

TODO

## Arguments

``` json
{
    "external_user_name": "{'description': ['(chat only - required) Name of the "user" sending the message'], 'required': False}",
    "from_address": "{'description': ['(inbox only - required) Email address of the message sender'], 'required': False}",
    "from_name": "{'description': ['(inbox only) Name of the message sender'], 'required': False}",
    "link": "{'description': ['(inbox only) Link associated with the message. This will be used to link the message subject in Team Inbox.'], 'required': False}",
    "msg": "{'description': ['Content of the message'], 'required': True}",
    "project": "{'description': ['(inbox only) Human readable identifier for more detailed message categorization'], 'required': False}",
    "reply_to": "{'description': ['(inbox only) Email address for replies'], 'required': False}",
    "source": "{'description': ['(inbox only - required) Human readable identifier of the application that uses the Flowdock API'], 'required': False}",
    "subject": "{'description': ['(inbox only - required) Subject line of the message'], 'required': False}",
    "tags": "{'description': ['tags of the message, separated by commas'], 'required': False}",
    "token": "{'description': ['API token.'], 'required': True}",
    "type": "{'description': ["Whether to post to 'inbox' or 'chat'"], 'required': True, 'choices': ['inbox', 'chat']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool', 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

- flowdock:
    type: inbox
    token: AAAAAA
    from_address: user@example.com
    source: my cool app
    msg: test from ansible
    subject: test subject

- flowdock:
    type: chat
    token: AAAAAA
    external_user_name: testuser
    msg: test from ansible
    tags: tag1,tag2,tag3

```

## License

TODO

## Author Information
  - ['Matt Coddington (@mcodd)']
