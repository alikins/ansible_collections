# Ansible module: ansible.module_telegram


module for sending notifications via telegram

## Description

Send notifications via telegram bot, to a verified group or user

## Requirements

TODO

## Arguments

``` json
{
    "chat_id": "{'description': ['Telegram group or user chat_id'], 'required': True}",
    "msg": "{'description': ['What message you wish to send.'], 'required': True}",
    "msg_format": "{'description': ['Message format. Formatting options `markdown` and `html` described in Telegram API docs (https://core.telegram.org/bots/api#formatting-options). If option `plain` set, message will not be formatted.'], 'default': 'plain', 'choices': ['plain', 'markdown', 'html'], 'version_added': '2.4'}",
    "token": "{'description': ['Token identifying your telegram bot.'], 'required': True}",
}
```

## Examples


``` yaml


- name: send a message to chat in playbook
  telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    chat_id: 000000
    msg: Ansible task finished

```

## License

TODO

## Author Information
  - ['Artem Feofanov (@tyouxa)']
