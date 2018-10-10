# Ansible module: ansible.module_async_status


Obtain status of asynchronous task

## Description

This module gets the status of an asynchronous task.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "jid": "{'description': ['Job or task identifier'], 'required': True}",
    "mode": "{'description': ['if C(status), obtain the status; if C(cleanup), clean up the async job cache (by default in C(~/.ansible_async/)) for the specified job I(jid).'], 'choices': ['status', 'cleanup'], 'default': 'status'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
