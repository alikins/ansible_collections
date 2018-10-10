# Ansible module: ansible.module_bearychat


Send BearyChat notifications

## Description

The M(bearychat) module sends notifications to U(https://bearychat.com) via the Incoming Robot integration.

## Requirements

TODO

## Arguments

``` json
{
    "attachments": "{'description': ['Define a list of attachments. For more information, see https://github.com/bearyinnovative/bearychat-tutorial/blob/master/robots/incoming.md#attachments']}",
    "channel": "{'description': ['Channel to send the message to. If absent, the message goes to the default channel selected by the I(url).']}",
    "markdown": "{'description': ['If C(yes), text will be parsed as markdown.'], 'default': True, 'type': 'bool'}",
    "text": "{'description': ['Message to send.']}",
    "url": "{'description': ['BearyChat WebHook URL. This authenticates you to the bearychat service. It looks like C(https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60).'], 'required': True}",
}
```

## Examples


``` yaml

- name: Send notification message via BearyChat
  local_action:
    module: bearychat
    url: |
      https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60
    text: "{{ inventory_hostname }} completed"

- name: Send notification message via BearyChat all options
  local_action:
    module: bearychat
    url: |
      https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60
    text: "{{ inventory_hostname }} completed"
    markdown: no
    channel: "#ansible"
    attachments:
      - title: "Ansible on {{ inventory_hostname }}"
        text: "May the Force be with you."
        color: "#ffffff"
        images:
          - http://example.com/index.png

```

## License

TODO

## Author Information
  - ['Jiangge Zhang (@tonyseek)']
