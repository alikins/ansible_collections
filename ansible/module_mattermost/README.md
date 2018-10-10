# Ansible module: ansible.module_mattermost


Send Mattermost notifications

## Description

Sends notifications to U(http://your.mattermost.url) via the Incoming WebHook integration.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Mattermost webhook api key. Log into your mattermost site, go to Menu -> Integration -> Incoming Webhook -> Add Incoming Webhook. This will give you full URL. api_key is the last part. http://mattermost.example.com/hooks/C(API_KEY)'], 'required': True}",
    "channel": "{'description': ['Channel to send the message to. If absent, the message goes to the channel selected for the I(api_key).']}",
    "icon_url": "{'description': ["Url for the message sender's icon."], 'default': 'https://www.ansible.com/favicon.ico'}",
    "text": "{'description': ['Text to send. Note that the module does not handle escaping characters.'], 'required': True}",
    "url": "{'description': ['Mattermost url (i.e. http://mattermost.yourcompany.com).'], 'required': True}",
    "username": "{'description': ['This is the sender of the message (Username Override need to be enabled by mattermost admin, see mattermost doc.'], 'default': 'Ansible'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Send notification message via Mattermost
  mattermost:
    url: http://mattermost.example.com
    api_key: my_api_key
    text: '{{ inventory_hostname }} completed'

- name: Send notification message via Mattermost all options
  mattermost:
    url: http://mattermost.example.com
    api_key: my_api_key
    text: '{{ inventory_hostname }} completed'
    channel: notifications
    username: 'Ansible on {{ inventory_hostname }}'
    icon_url: http://www.example.com/some-image-file.png

```

## License

TODO

## Author Information
  - ['Benjamin Jolivot (@bjolivot)']
