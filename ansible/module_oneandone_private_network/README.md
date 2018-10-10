# Ansible module: ansible.module_oneandone_private_network


Configure 1&1 private networking

## Description

Create, remove, reconfigure, update a private network. This module has a dependency on 1and1 >= 1.0

## Requirements

TODO

## Arguments

``` json
{
    "add_members": "{'description': ['List of server identifiers (name or id) to be added to the private network.']}",
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.'], 'required': False}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1.'], 'required': True}",
    "datacenter": "{'description': ['The identifier of the datacenter where the private network will be created']}",
    "description": "{'description': ['Set a description for the network.']}",
    "name": "{'description': ['Private network name used with present state. Used as identifier (id or name) when used with absent state.'], 'required': True}",
    "network_address": "{'description': ['Set a private network space, i.e. 192.168.1.0']}",
    "private_network": "{'description': ['The identifier (id or name) of the network used with update state.'], 'required': True}",
    "remove_members": "{'description': ['List of server identifiers (name or id) to be removed from the private network.']}",
    "state": "{'description': ["Define a network's state to create, remove, or update."], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'update']}",
    "subnet_mask": "{'description': ['Set the netmask for the private network, i.e. 255.255.255.0']}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the _wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Provisioning example. Create and destroy private networks.

- oneandone_private_network:
    auth_token: oneandone_private_api_key
    name: backup_network
    description: Testing creation of a private network with ansible
    network_address: 70.35.193.100
    subnet_mask: 255.0.0.0
    datacenter: US

- oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: absent
    name: backup_network

# Modify the private network.

- oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    network_address: 192.168.2.0
    subnet_mask: 255.255.255.0

# Add members to the private network.

- oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    add_members:
     - server identifier (id or name)

# Remove members from the private network.

- oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    remove_members:
     - server identifier (id or name)


```

## License

TODO

## Author Information
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
