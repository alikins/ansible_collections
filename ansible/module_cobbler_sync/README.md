# Ansible module: ansible.module_cobbler_sync


Sync Cobbler

## Description

Sync Cobbler to commit changes.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['The name or IP address of the Cobbler system.'], 'default': '127.0.0.1'}",
    "password": "{'description': ['The password to log in to Cobbler.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter C(use_ssl).']}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to log in to Cobbler.'], 'default': 'cobbler'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Commit Cobbler changes
  cobbler_sync:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
  run_once: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
