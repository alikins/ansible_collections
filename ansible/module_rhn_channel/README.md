# Ansible module: ansible.module_rhn_channel


Adds or removes Red Hat software channels

## Description

Adds or removes Red Hat software channels.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the software channel.'], 'required': True}",
    "password": "{'description': ['RHN/Satellite password.'], 'required': True}",
    "state": "{'description': ['Whether the channel should be present or not, taking action if the state is different from what is stated.'], 'default': 'present'}",
    "sysname": "{'description': ['Name of the system as it is known in RHN/Satellite.'], 'required': True}",
    "url": "{'description': ['The full URL to the RHN/Satellite API.'], 'required': True}",
    "user": "{'description': ['RHN/Satellite login.'], 'required': True}",
}
```

## Examples


``` yaml

- rhn_channel:
    name: rhel-x86_64-server-v2vwin-6
    sysname: server01
    url: https://rhn.redhat.com/rpc/api
    user: rhnuser
    password: guessme
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Vincent Van der Kussen (@vincentvdk)']
