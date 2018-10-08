# Ansible callback: ansible.callback_slack


Sends play events to a Slack channel

## Description

This is an ansible callback plugin that sends status updates to a Slack channel during playbook execution.
Before 2.4 only environment variables were available for configuring this plugin

## Requirements

TODO

## Arguments

``` json
{
    "channel": "{'default': '#ansible', 'description': ['Slack room to post in.'], 'env': [{'name': 'SLACK_CHANNEL'}], 'ini': [{'section': 'callback_slack', 'key': 'channel'}]}",
    "username": "{'description': ['Username to post as.'], 'env': [{'name': 'SLACK_USERNAME'}], 'default': 'ansible', 'ini': [{'section': 'callback_slack', 'key': 'username'}]}",
    "webhook_url": "{'required': True, 'description': ['Slack Webhook URL'], 'env': [{'name': 'SLACK_WEBHOOK_URL'}], 'ini': [{'section': 'callback_slack', 'key': 'webhook_url'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
