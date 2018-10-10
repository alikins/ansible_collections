# Ansible module: ansible.module_oneandone_public_ip


Configure 1&1 public IPs

## Description

Create, update, and remove public IPs. This module has a dependency on 1and1 >= 1.0

## Requirements

TODO

## Arguments

``` json
{
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.'], 'required': False}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1.'], 'required': True}",
    "datacenter": "{'description': ['ID of the datacenter where the IP will be created (only for unassigned IPs).'], 'required': False}",
    "public_ip_id": "{'description': ['The ID of the public IP used with update and delete states.'], 'required': True}",
    "reverse_dns": "{'description': ['Reverse DNS name. maxLength=256'], 'required': False}",
    "state": "{'description': ['Define a public ip state to create, remove, or update.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'update']}",
    "type": "{'description': ['Type of IP. Currently, only IPV4 is available.'], 'choices': ['IPV4', 'IPV6'], 'default': 'IPV4', 'required': False}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the _wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Create a public IP.

- oneandone_public_ip:
    auth_token: oneandone_private_api_key
    reverse_dns: example.com
    datacenter: US
    type: IPV4

# Update a public IP.

- oneandone_public_ip:
    auth_token: oneandone_private_api_key
    public_ip_id: public ip id
    reverse_dns: secondexample.com
    state: update


# Delete a public IP

- oneandone_public_ip:
    auth_token: oneandone_private_api_key
    public_ip_id: public ip id
    state: absent


```

## License

TODO

## Author Information
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
