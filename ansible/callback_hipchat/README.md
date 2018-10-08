# Ansible callback: ansible.callback_hipchat


post task events to hipchat

## Description

This callback plugin sends status updates to a HipChat channel during playbook execution.
Before 2.4 only environment variables were available for configuring this plugin.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['HipChat API version, v1 or v2.'], 'required': False, 'default': 'v1', 'env': [{'name': 'HIPCHAT_API_VERSION'}], 'ini': [{'section': 'callback_hipchat', 'key': 'api_version'}]}",
    "from": "{'description': ['Name to post as'], 'default': 'ansible', 'env': [{'name': 'HIPCHAT_FROM'}], 'ini': [{'section': 'callback_hipchat', 'key': 'from'}]}",
    "notify": "{'description': ['Add notify flag to important messages'], 'type': 'bool', 'default': True, 'env': [{'name': 'HIPCHAT_NOTIFY'}], 'ini': [{'section': 'callback_hipchat', 'key': 'notify'}]}",
    "room": "{'description': ['HipChat room to post in.'], 'default': 'ansible', 'env': [{'name': 'HIPCHAT_ROOM'}], 'ini': [{'section': 'callback_hipchat', 'key': 'room'}]}",
    "token": "{'description': ['HipChat API token for v1 or v2 API.'], 'required': True, 'env': [{'name': 'HIPCHAT_TOKEN'}], 'ini': [{'section': 'callback_hipchat', 'key': 'token'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
