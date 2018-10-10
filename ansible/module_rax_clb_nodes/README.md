# Ansible module: ansible.module_rax_clb_nodes


add, modify and remove nodes from a Rackspace Cloud Load Balancer

## Description

Adds, modifies and removes nodes from a Rackspace Cloud Load Balancer

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'required': False, 'description': ['IP address or domain name of the node']}",
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "condition": "{'required': False, 'choices': ['enabled', 'disabled', 'draining'], 'description': ['Condition for the node, which determines its role within the load balancer']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "load_balancer_id": "{'required': True, 'description': ['Load balancer id']}",
    "node_id": "{'required': False, 'description': ['Node id']}",
    "port": "{'required': False, 'description': ['Port number of the load balanced service on the node']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Indicate desired state of the node']}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "type": "{'required': False, 'choices': ['primary', 'secondary'], 'description': ['Type of node']}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "wait": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Wait for the load balancer to become active before returning']}",
    "wait_timeout": "{'required': False, 'default': 30, 'description': ['How long to wait before giving up and returning an error']}",
    "weight": "{'required': False, 'description': ['Weight of node']}",
}
```

## Examples


``` yaml

# Add a new node to the load balancer
- local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    address: 10.2.2.3
    port: 80
    condition: enabled
    type: primary
    wait: yes
    credentials: /path/to/credentials

# Drain connections from a node
- local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    node_id: 410
    condition: draining
    wait: yes
    credentials: /path/to/credentials

# Remove a node from the load balancer
- local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    node_id: 410
    state: absent
    wait: yes
    credentials: /path/to/credentials

```

## License

TODO

## Author Information
  - ['Lukasz Kawczynski (@neuroid)']
