# Ansible module: ansible.module_rocketchat


Send notifications to Rocket Chat

## Description

The C(rocketchat) module sends notifications to Rocket Chat via the Incoming WebHook integration

## Requirements

TODO

## Arguments

``` json
{
    "attachments": "{'description': ['Define a list of attachments.']}",
    "channel": "{'description': ['Channel to send the message to. If absent, the message goes to the channel selected for the I(token) specified during the creation of webhook.']}",
    "color": "{'description': ["Allow text to use default colors - use the default of 'normal' to not send a custom color bar at the start of the message"], 'default': 'normal', 'choices': ['normal', 'good', 'warning', 'danger']}",
    "domain": "{'description': ['The domain for your environment without protocol. (i.e. C(example.com) or C(chat.example.com))'], 'required': True}",
    "icon_emoji": "{'description': ['Emoji for the message sender. The representation for the available emojis can be got from Rocket Chat. (for example :thumbsup:) (if I(icon_emoji) is set, I(icon_url) will not be used)']}",
    "icon_url": "{'description': ["URL for the message sender's icon."], 'default': 'https://www.ansible.com/favicon.ico'}",
    "link_names": "{'description': ['Automatically create links for channels and usernames in I(msg).'], 'default': 1, 'choices': [1, 0]}",
    "msg": "{'description': ['Message to be sent.']}",
    "protocol": "{'description': ['Specify the protocol used to send notification messages before the webhook url. (i.e. http or https)'], 'default': 'https', 'choices': ['http', 'https']}",
    "token": "{'description': ["Rocket Chat Incoming Webhook integration token.  This provides authentication to Rocket Chat's Incoming webhook for posting messages."], 'required': True}",
    "username": "{'description': ['This is the sender of the message.'], 'default': 'Ansible'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Send notification message via Rocket Chat
  rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    msg: '{{ inventory_hostname }} completed'
  delegate_to: localhost

- name: Send notification message via Rocket Chat all options
  rocketchat:
    domain: chat.example.com
    token: thetoken/generatedby/rocketchat
    msg: '{{ inventory_hostname }} completed'
    channel: #ansible
    username: 'Ansible on {{ inventory_hostname }}'
    icon_url: http://www.example.com/some-image-file.png
    link_names: 0
  delegate_to: localhost

- name: insert a color bar in front of the message for visibility purposes and use the default webhook icon and name configured in rocketchat
  rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    msg: '{{ inventory_hostname }} is alive!'
    color: good
    username: ''
    icon_url: ''
  delegate_to: localhost

- name: Use the attachments API
  rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    attachments:
      - text: Display my system load on host A and B
        color: #ff00dd
        title: System load
        fields:
          - title: System A
            value: 'load average: 0,74, 0,66, 0,63'
            short: True
          - title: System B
            value: 'load average: 5,16, 4,64, 2,43'
            short: True
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ramon de la Fuente (@ramondelafuente)']
