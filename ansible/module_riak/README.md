# Ansible module: ansible.module_riak


This module handles some common Riak operations

## Description

This module can be used to join nodes to a cluster, check the status of the cluster.

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['The command you would like to perform against the cluster.'], 'choices': ['ping', 'kv_test', 'join', 'plan', 'commit']}",
    "config_dir": "{'description': ['The path to the riak configuration directory'], 'default': '/etc/riak'}",
    "http_conn": "{'description': ['The ip address and port that is listening for Riak HTTP queries'], 'default': '127.0.0.1:8098'}",
    "target_node": "{'description': ['The target node for certain operations (join, ping)'], 'default': 'riak@127.0.0.1'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.5.1'}",
    "wait_for_handoffs": "{'description': ['Number of seconds to wait for handoffs to complete.']}",
    "wait_for_ring": "{'description': ['Number of seconds to wait for all nodes to agree on the ring.']}",
    "wait_for_service": "{'description': ['Waits for a riak service to come online before continuing.'], 'choices': ['kv']}",
}
```

## Examples


``` yaml

# Join's a Riak node to another node
- riak:
    command: join
    target_node: riak@10.1.1.1

# Wait for handoffs to finish.  Use with async and poll.
- riak:
    wait_for_handoffs: yes

# Wait for riak_kv service to startup
- riak:
    wait_for_service: kv

```

## License

TODO

## Author Information
  - ['James Martin (@jsmartin)', 'Drew Kerrigan (@drewkerrigan)']
  - ['James Martin (@jsmartin)', 'Drew Kerrigan (@drewkerrigan)']
