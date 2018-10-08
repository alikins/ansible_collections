# Ansible callback: ansible.callback_jabber


post task events to a jabber server

## Description

The chatty part of ChatOps with a Hipchat server as a target
This callback plugin sends status updates to a HipChat channel during playbook execution.

## Requirements

TODO

## Arguments

``` json
{
    "password": "{'description': ['Password for the user to the jabber server'], 'required': True, 'env': [{'name': 'JABBER_PASS'}]}",
    "server": "{'description': ['connection info to jabber server'], 'required': True, 'env': [{'name': 'JABBER_SERV'}]}",
    "to": "{'description': ['chat identifier that will recieve the message'], 'required': True, 'env': [{'name': 'JABBER_TO'}]}",
    "user": "{'description': ['Jabber user to authenticate as'], 'required': True, 'env': [{'name': 'JABBER_USER'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
