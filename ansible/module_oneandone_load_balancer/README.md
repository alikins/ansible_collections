# Ansible module: ansible.module_oneandone_load_balancer


Configure 1&1 load balancer

## Description

Create, remove, update load balancers. This module has a dependency on 1and1 >= 1.0

## Requirements

TODO

## Arguments

``` json
{
    "add_rules": "{'description': ['A list of rules that will be added to an existing load balancer. It is syntax is the same as the one used for rules parameter. Used in combination with update state.'], 'required': False}",
    "add_server_ips": "{'description': ['A list of server identifiers (id or name) to be assigned to a load balancer. Used in combination with update state.'], 'required': False}",
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.'], 'required': False}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1.'], 'required': True}",
    "datacenter": "{'description': ['ID or country code of the datacenter where the load balancer will be created.'], 'default': 'US', 'choices': ['US', 'ES', 'DE', 'GB'], 'required': False}",
    "description": "{'description': ['Description of the load balancer. maxLength=256'], 'required': False}",
    "health_check_interval": "{'description': ['Health check period in seconds. minimum=5, maximum=300, multipleOf=1'], 'required': True}",
    "health_check_parse": "{'description': ['Regular expression to check. Required for HTTP health check. maxLength=64'], 'required': False}",
    "health_check_path": "{'description': ['Url to call for cheking. Required for HTTP health check. maxLength=1000'], 'required': False}",
    "health_check_test": "{'description': ['Type of the health check. At the moment, HTTP is not allowed.'], 'choices': ['NONE', 'TCP', 'HTTP', 'ICMP'], 'required': True}",
    "load_balancer": "{'description': ['The identifier (id or name) of the load balancer used with update state.'], 'required': True}",
    "method": "{'description': ['Balancing procedure.'], 'choices': ['ROUND_ROBIN', 'LEAST_CONNECTIONS'], 'required': True}",
    "name": "{'description': ['Load balancer name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128'], 'required': True}",
    "persistence": "{'description': ['Persistence.'], 'required': True}",
    "persistence_time": "{'description': ['Persistence time in seconds. Required if persistence is enabled. minimum=30, maximum=1200, multipleOf=1'], 'required': True}",
    "remove_rules": "{'description': ['A list of rule ids that will be removed from an existing load balancer. Used in combination with update state.'], 'required': False}",
    "remove_server_ips": "{'description': ['A list of server IP ids to be unassigned from a load balancer. Used in combination with update state.'], 'required': False}",
    "rules": "{'description': ['A list of rule objects that will be set for the load balancer. Each rule must contain protocol, port_balancer, and port_server parameters, in addition to source parameter, which is optional.'], 'required': True}",
    "state": "{'description': ['Define a load balancer state to create, remove, or update.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'update']}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the _wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Provisioning example. Create and destroy a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    name: ansible load balancer
    description: Testing creation of load balancer with ansible
    health_check_test: TCP
    health_check_interval: 40
    persistence: true
    persistence_time: 1200
    method: ROUND_ROBIN
    datacenter: US
    rules:
     -
       protocol: TCP
       port_balancer: 80
       port_server: 80
       source: 0.0.0.0
    wait: true
    wait_timeout: 500

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    name: ansible load balancer
    wait: true
    wait_timeout: 500
    state: absent

# Update a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer
    name: ansible load balancer updated
    description: Testing the update of a load balancer with ansible
    wait: true
    wait_timeout: 500
    state: update

# Add server to a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding server to a load balancer with ansible
    add_server_ips:
     - server identifier (id or name)
    wait: true
    wait_timeout: 500
    state: update

# Remove server from a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Removing server from a load balancer with ansible
    remove_server_ips:
     - B2504878540DBC5F7634EB00A07C1EBD (server's ip id)
    wait: true
    wait_timeout: 500
    state: update

# Add rules to a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding rules to a load balancer with ansible
    add_rules:
     -
       protocol: TCP
       port_balancer: 70
       port_server: 70
       source: 0.0.0.0
     -
       protocol: TCP
       port_balancer: 60
       port_server: 60
       source: 0.0.0.0
    wait: true
    wait_timeout: 500
    state: update

# Remove rules from a load balancer.

- oneandone_load_balancer:
    auth_token: oneandone_private_api_key
    load_balancer: ansible load balancer updated
    description: Adding rules to a load balancer with ansible
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
