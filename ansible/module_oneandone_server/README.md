# Ansible module: ansible.module_oneandone_server


Create, destroy, start, stop, and reboot a 1&1 Host server

## Description

Create, destroy, update, start, stop, and reboot a 1&1 Host server. When the server is created it can optionally wait for it to be 'running' before returning.

## Requirements

TODO

## Arguments

``` json
{
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.']}",
    "appliance": "{'description': ["The operating system name or ID for the server. It is required only for 'present' state."]}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1. Overrides the ONEANDONE_AUTH_TOKEN environement variable.'], 'required': True}",
    "auto_increment": "{'description': ['When creating multiple servers at once, whether to differentiate hostnames by appending a count after them or substituting the count where there is a %02d or %03d in the hostname string.'], 'type': 'bool', 'default': True}",
    "cores_per_processor": "{'description': ['The number of cores per processor. It must be provided with vcore, ram, and hdds parameters.']}",
    "count": "{'description': ['The number of servers to create.'], 'default': 1}",
    "datacenter": "{'description': ['The datacenter location.'], 'default': 'US', 'choices': ['US', 'ES', 'DE', 'GB']}",
    "description": "{'description': ['The description of the server.']}",
    "firewall_policy": "{'description': ['The firewall policy name or ID.']}",
    "fixed_instance_size": "{'description': ["The instance size name or ID of the server. It is required only for 'present' state, and it is mutually exclusive with vcore, cores_per_processor, ram, and hdds parameters."], 'required': True, 'choices': ['S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL']}",
    "hdds": "{'description': ['A list of hard disks with nested "size" and "is_main" properties. It must be provided with vcore, cores_per_processor, and ram parameters.']}",
    "hostname": "{'description': ["The hostname or ID of the server. Only used when state is 'present'."]}",
    "load_balancer": "{'description': ['The load balancer name or ID.']}",
    "monitoring_policy": "{'description': ['The monitoring policy name or ID.']}",
    "private_network": "{'description': ['The private network name or ID.']}",
    "ram": "{'description': ['The amount of RAM memory. It must be provided with with vcore, cores_per_processor, and hdds parameters.']}",
    "server": "{'description': ["Server identifier (ID or hostname). It is required for all states except 'running' and 'present'."]}",
    "server_type": "{'description': ['The type of server to be built.'], 'default': 'cloud', 'choices': ['cloud', 'baremetal', 'k8s_node']}",
    "ssh_key": "{'description': ["User's public SSH key (contents, not path)."]}",
    "state": "{'description': ["Define a server's state to create, remove, start or stop it."], 'default': 'present', 'choices': ['present', 'absent', 'running', 'stopped']}",
    "vcore": "{'description': ['The total number of processors. It must be provided with cores_per_processor, ram, and hdds parameters.']}",
    "wait": "{'description': ["Wait for the server to be in state 'running' before returning. Also used for delete operation (set to 'false' if you don't want to wait for each individual server to be deleted before moving on with other tasks.)"], 'type': 'bool', 'default': True}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Provisioning example. Creates three servers and enumerate their names.

- oneandone_server:
    auth_token: oneandone_private_api_key
    hostname: node%02d
    fixed_instance_size: XL
    datacenter: US
    appliance: C5A349786169F140BCBC335675014C08
    auto_increment: true
    count: 3

# Create three servers, passing in an ssh_key.

- oneandone_server:
    auth_token: oneandone_private_api_key
    hostname: node%02d
    vcore: 2
    cores_per_processor: 4
    ram: 8.0
    hdds:
      - size: 50
        is_main: false
    datacenter: ES
    appliance: C5A349786169F140BCBC335675014C08
    count: 3
    wait: yes
    wait_timeout: 600
    wait_interval: 10
    ssh_key: SSH_PUBLIC_KEY

# Removing server

- oneandone_server:
    auth_token: oneandone_private_api_key
    state: absent
    server: 'node01'

# Starting server.

- oneandone_server:
    auth_token: oneandone_private_api_key
    state: running
    server: 'node01'

# Stopping server

- oneandone_server:
    auth_token: oneandone_private_api_key
    state: stopped
    server: 'node01'

```

## License

TODO

## Author Information
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
