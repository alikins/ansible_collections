# Ansible module: ansible.module_gluster_peer


Attach/Detach peers to/from the cluster

## Description

Create or diminish a GlusterFS trusted storage pool. A set of nodes can be added into an existing trusted storage pool or a new storage pool can be formed. Or, nodes can be removed from an existing trusted storage pool.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'type': 'bool', 'default': False, 'description': ['Applicable only while removing the nodes from the pool. gluster will refuse to detach a node from the pool if any one of the node is down, in such cases force can be used.']}",
    "nodes": "{'description': ['List of nodes that have to be probed into the pool.'], 'required': True}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['Determines whether the nodes should be attached to the pool or removed from the pool. If the state is present, nodes will be attached to the pool. If state is absent, nodes will be detached from the pool.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a trusted storage pool
  gluster_peer:
        state: present
        nodes:
             - 10.0.1.5
             - 10.0.1.10

- name: Delete a node from the trusted storage pool
  gluster_peer:
         state: absent
         nodes:
              - 10.0.1.10

- name: Delete a node from the trusted storage pool by force
  gluster_peer:
         state: absent
         nodes:
              - 10.0.0.1
         force: true

```

## License

TODO

## Author Information
  - ['Sachidananda Urs (@sac)']
