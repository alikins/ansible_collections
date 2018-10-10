# Ansible module: ansible.module_clc_loadbalancer


Create, Delete shared loadbalancers in CenturyLink Cloud

## Description

An Ansible module to Create, Delete shared loadbalancers in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "alias": "{'description': ['The alias of your CLC Account'], 'required': True}",
    "description": "{'description': ['A description for the loadbalancer']}",
    "location": "{'description': ['The location of the datacenter where the load balancer resides in'], 'required': True}",
    "method": "{'description': ['-The balancing method for the load balancer pool'], 'choices': ['leastConnection', 'roundRobin']}",
    "name": "{'description': ['The name of the loadbalancer'], 'required': True}",
    "nodes": "{'description': ['A list of nodes that needs to be added to the load balancer pool'], 'default': []}",
    "persistence": "{'description': ['The persistence method for the load balancer'], 'choices': ['standard', 'sticky']}",
    "port": "{'description': ['Port to configure on the public-facing side of the load balancer pool'], 'choices': [80, 443]}",
    "state": "{'description': ['Whether to create or delete the load balancer pool'], 'default': 'present', 'choices': ['present', 'absent', 'port_absent', 'nodes_present', 'nodes_absent']}",
    "status": "{'description': ['The status of the loadbalancer'], 'default': 'enabled', 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples
- name: Create Loadbalancer
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: present

- name: Add node to an existing loadbalancer pool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.234
            privatePort: 80
        state: nodes_present

- name: Remove node from an existing loadbalancer pool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.234
            privatePort: 80
        state: nodes_absent

- name: Delete LoadbalancerPool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Delete things
      clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: port_absent

- name: Delete Loadbalancer
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Delete things
      clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: absent

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
