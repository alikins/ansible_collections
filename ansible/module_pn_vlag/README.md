# Ansible module: ansible.module_pn_vlag


CLI command to create/delete/modify vlag

## Description

Execute vlag-create/vlag-delete/vlag-modify command.
A virtual link aggregation group (VLAG) allows links that are physically connected to two different Pluribus Networks devices to appear as a single trunk to a third device. The third device can be a switch, server, or any Ethernet device. A VLAG can provide Layer 2 multipathing, which allows you to create redundancy by increasing bandwidth, enabling multiple parallel paths between nodes and loadbalancing traffic where alternative paths exist.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run this command on.']}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_failover_action": "{'description': ['Specify the failover action as move or ignore.'], 'choices': ['move', 'ignore']}",
    "pn_lacp_fallback": "{'description': ['Specify the LACP fallback mode as bundles or individual.'], 'choices': ['bundle', 'individual']}",
    "pn_lacp_fallback_timeout": "{'description': ['Specify the LACP fallback timeout in seconds. The range is between 30 and 60 seconds with a default value of 50 seconds.']}",
    "pn_lacp_mode": "{'description': ['Specify the LACP mode.'], 'choices': ['off', 'passive', 'active']}",
    "pn_lacp_timeout": "{'description': ['Specify the LACP timeout as slow(30 seconds) or fast(4 seconds).'], 'choices': ['slow', 'fast']}",
    "pn_mode": "{'description': ['Specify the mode for the VLAG. Active-standby indicates one side is active and the other side is in standby mode. Active-active indicates that both sides of the vlag are up by default.'], 'choices': ['active-active', 'active-standby']}",
    "pn_name": "{'description': ['The C(pn_name) takes a valid name for vlag configuration.'], 'required': True}",
    "pn_peer_port": "{'description': ['Specify the peer VLAG port.', 'Required for vlag-create.']}",
    "pn_peer_switch": "{'description': ['Specify the fabric-name of the peer switch.']}",
    "pn_port": "{'description': ['Specify the local VLAG port.', 'Required for vlag-create.']}",
    "state": "{'description': ["State the action to perform. Use 'present' to create vlag, 'absent' to delete vlag and 'update' to modify vlag."], 'required': True, 'choices': ['present', 'absent', 'update']}",
}
```

## Examples


``` yaml

- name: create a VLAG
  pn_vlag:
    state: 'present'
    pn_name: spine-to-leaf
    pn_port: 'spine01-to-leaf'
    pn_peer_port: 'spine02-to-leaf'
    pn_peer_switch: spine02
    pn_mode: 'active-active'

- name: delete VLAGs
  pn_vlag:
    state: 'absent'
    pn_name: spine-to-leaf

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
