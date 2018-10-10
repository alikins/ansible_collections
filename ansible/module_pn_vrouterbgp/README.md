# Ansible module: ansible.module_pn_vrouterbgp


CLI command to add/remove/modify vrouter-bgp

## Description

Execute vrouter-bgp-add, vrouter-bgp-remove, vrouter-bgp-modify command.
Each fabric, cluster, standalone switch, or virtual network (VNET) can provide its tenants with a vRouter service that forwards traffic between networks and implements Layer 4 protocols.

## Requirements

TODO

## Arguments

``` json
{
    "pn_bfd": "{'description': ['Specify if you want BFD protocol support for fault detection.']}",
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_default_originate": "{'description': ['Specify if you want announce default routes to the neighbor or not.']}",
    "pn_ebgp": "{'description': ['Specify a value for external BGP to accept or attempt BGP connections to external peers, not directly connected, on the network. This is a value between 1 and 255.']}",
    "pn_holdtime": "{'description': ['Specify BGP neighbor holdtime in seconds.']}",
    "pn_keepalive": "{'description': ['Specify BGP neighbor keepalive interval in seconds.']}",
    "pn_max_prefix": "{'description': ['Specify the maximum number of prefixes.']}",
    "pn_max_prefix_warn": "{'description': ['Specify if you want a warning message when the maximum number of prefixes is exceeded.']}",
    "pn_multiprotocol": "{'description': ['Specify a multi-protocol for BGP.'], 'choices': ['ipv4-unicast', 'ipv6-unicast']}",
    "pn_neighbor": "{'description': ['Specify a neighbor IP address to use for BGP.', 'Required for vrouter-bgp-add.']}",
    "pn_next_hop_self": "{'description': ['Specify if the next-hop is the same router or not.']}",
    "pn_override_capability": "{'description': ['Specify if you want to override capability.']}",
    "pn_password": "{'description': ['Specify a password, if desired.']}",
    "pn_prefix_listin": "{'description': ['Specify the prefix list to filter traffic inbound.']}",
    "pn_prefix_listout": "{'description': ['Specify the prefix list to filter traffic outbound.']}",
    "pn_remote_as": "{'description': ['Specify the remote Autonomous System(AS) number. This value is between 1 and 4294967295.', 'Required for vrouter-bgp-add.']}",
    "pn_route_mapin": "{'description': ['Specify inbound route map for neighbor.']}",
    "pn_route_mapout": "{'description': ['Specify outbound route map for neighbor.']}",
    "pn_route_reflector": "{'description': ['Specify if a route reflector client is used.']}",
    "pn_soft_reconfig": "{'description': ['Specify if you want a soft reconfiguration of inbound traffic.']}",
    "pn_vrouter_name": "{'description': ['Specify a name for the vRouter service.'], 'required': True}",
    "pn_weight": "{'description': ['Specify a default weight value between 0 and 65535 for the neighbor routes.']}",
    "state": "{'description': ["State the action to perform. Use 'present' to add bgp, 'absent' to remove bgp and 'update' to modify bgp."], 'required': True, 'choices': ['present', 'absent', 'update']}",
}
```

## Examples


``` yaml

- name: add vrouter-bgp
  pn_vrouterbgp:
    state: 'present'
    pn_vrouter_name: 'ansible-vrouter'
    pn_neighbor: 104.104.104.1
    pn_remote_as: 1800

- name: remove vrouter-bgp
  pn_vrouterbgp:
    state: 'absent'
    pn_name: 'ansible-vrouter'

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
