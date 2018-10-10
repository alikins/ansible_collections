# Ansible module: ansible.module_pushbullet


Sends notifications to Pushbullet

## Description

This module sends push notifications via Pushbullet to channels or devices.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Push bullet API token'], 'required': True}",
    "body": "{'description': ["Body of the notification, e.g. Details of the fault you're alerting."]}",
    "channel": "{'description': ['The channel TAG you wish to broadcast a push notification, as seen on the "My Channels" > "Edit your channel" at Pushbullet page.']}",
    "device": "{'description': ['The device NAME you wish to send a push notification, as seen on the Pushbullet main page.']}",
    "push_type": "{'description': ['Thing you wish to push.'], 'default': 'note', 'choices': ['note', 'link']}",
    "title": "{'description': ['Title of the notification.'], 'required': True}",
}
```

## Examples


``` yaml

# Sends a push notification to a device
- pushbullet:
    api_key: "ABC123abc123ABC123abc123ABC123ab"
    device: "Chrome"
    title: "You may see this on Google Chrome"

# Sends a link to a device
- pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    device: Chrome
    push_type: link
    title: Ansible Documentation
    body: https://docs.ansible.com/

# Sends a push notification to a channel
- pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    channel: my-awesome-channel
    title: Broadcasting a message to the #my-awesome-channel folks

# Sends a push notification with title and body to a channel
- pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    channel: my-awesome-channel
    title: ALERT! Signup service is down
    body: Error rate on signup service is over 90% for more than 2 minutes

```

## License

TODO

## Author Information
  - ['Willy Barro (@willybarro)']
