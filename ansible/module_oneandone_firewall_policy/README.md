# Ansible module: ansible.module_oneandone_firewall_policy


Configure 1&1 firewall policy

## Description

Create, remove, reconfigure, update firewall policies. This module has a dependency on 1and1 >= 1.0

## Requirements

TODO

## Arguments

``` json
{
    "add_rules": "{'description': ['A list of rules that will be added to an existing firewall policy. It is syntax is the same as the one used for rules parameter. Used in combination with update state.'], 'required': False}",
    "add_server_ips": "{'description': ['A list of server identifiers (id or name) to be assigned to a firewall policy. Used in combination with update state.'], 'required': False}",
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.'], 'required': False}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1.'], 'required': True}",
    "description": "{'description': ['Firewall policy description. maxLength=256'], 'required': False}",
    "firewall_policy": "{'description': ['The identifier (id or name) of the firewall policy used with update state.'], 'required': True}",
    "name": "{'description': ['Firewall policy name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128'], 'required': True}",
    "remove_rules": "{'description': ['A list of rule ids that will be removed from an existing firewall policy. Used in combination with update state.'], 'required': False}",
    "remove_server_ips": "{'description': ['A list of server IP ids to be unassigned from a firewall policy. Used in combination with update state.'], 'required': False}",
    "rules": "{'description': ['A list of rules that will be set for the firewall policy. Each rule must contain protocol parameter, in addition to three optional parameters (port_from, port_to, and source)']}",
    "state": "{'description': ['Define a firewall policy state to create, remove, or update.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'update']}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the _wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Provisioning example. Create and destroy a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    name: ansible-firewall-policy
    description: Testing creation of firewall policies with ansible
    rules:
     -
       protocol: TCP
       port_from: 80
       port_to: 80
       source: 0.0.0.0
    wait: true
    wait_timeout: 500

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    state: absent
    name: ansible-firewall-policy

# Update a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    state: update
    firewall_policy: ansible-firewall-policy
    name: ansible-firewall-policy-updated
    description: Testing creation of firewall policies with ansible - updated

# Add server to a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    add_server_ips:
     - server_identifier (id or name)
     - server_identifier #2 (id or name)
    wait: true
    wait_timeout: 500
    state: update

# Remove server from a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    remove_server_ips:
     - B2504878540DBC5F7634EB00A07C1EBD (server's IP id)
    wait: true
    wait_timeout: 500
    state: update

# Add rules to a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    description: Adding rules to an existing firewall policy
    add_rules:
     -
       protocol: TCP
       port_from: 70
       port_to: 70
       source: 0.0.0.0
     -
       protocol: TCP
       port_from: 60
       port_to: 60
       source: 0.0.0.0
    wait: true
    wait_timeout: 500
    state: update

# Remove rules from a firewall policy.

- oneandone_firewall_policy:
    auth_token: oneandone_private_api_key
    firewall_policy: ansible-firewall-policy-updated
    remove_rules:
     - rule_id #1
     - rule_id #2
     - ...
    wait: true
    wait_timeout: 500
    state: update


```

## License

TODO

## Author Information
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
