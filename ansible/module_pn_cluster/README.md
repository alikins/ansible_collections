# Ansible module: ansible.module_pn_cluster


CLI command to create/delete a cluster

## Description

Execute cluster-create or cluster-delete command.
A cluster allows two switches to cooperate in high-availability (HA) deployments. The nodes that form the cluster must be members of the same fabric. Clusters are typically used in conjunction with a virtual link aggregation group (VLAG) that allows links physically connected to two separate switches appear as a single trunk to a third device. The third device can be a switch,server, or any Ethernet device.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_cluster_node1": "{'description': ['Specify the name of the first switch in the cluster.', "Required for 'cluster-create'."]}",
    "pn_cluster_node2": "{'description': ['Specify the name of the second switch in the cluster.', "Required for 'cluster-create'."]}",
    "pn_name": "{'description': ['Specify the name of the cluster.'], 'required': True}",
    "pn_validate": "{'description': ['Validate the inter-switch links and state of switches in the cluster.'], 'choices': ['validate', 'no-validate']}",
    "state": "{'description': ["Specify action to perform. Use 'present' to create cluster and 'absent' to delete cluster."], 'required': True, 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: create spine cluster
  pn_cluster:
    state: 'present'
    pn_name: 'spine-cluster'
    pn_cluster_node1: 'spine01'
    pn_cluster_node2: 'spine02'
    pn_validate: validate
    pn_quiet: True

- name: delete spine cluster
  pn_cluster:
    state: 'absent'
    pn_name: 'spine-cluster'
    pn_quiet: True

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
