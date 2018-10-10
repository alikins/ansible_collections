# Ansible module: ansible.module_pn_vlan


CLI command to create/delete a VLAN

## Description

Execute vlan-create or vlan-delete command.
VLANs are used to isolate network traffic at Layer 2.The VLAN identifiers 0 and 4095 are reserved and cannot be used per the IEEE 802.1Q standard. The range of configurable VLAN identifiers is 2 through 4092.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_description": "{'description': ['Specify a description for the VLAN.']}",
    "pn_ports": "{'description': ['Specifies the switch network data port number, list of ports, or range of ports. Port numbers must ne in the range of 1 to 64.']}",
    "pn_scope": "{'description': ['Specify a scope for the VLAN.', 'Required for vlan-create.'], 'choices': ['fabric', 'local']}",
    "pn_stats": "{'description': ['Specify if you want to collect statistics for a VLAN. Statistic collection is enabled by default.']}",
    "pn_untagged_ports": "{'description': ['Specifies the ports that should have untagged packets mapped to the VLAN. Untagged packets are packets that do not contain IEEE 802.1Q VLAN tags.']}",
    "pn_vlanid": "{'description': ['Specify a VLAN identifier for the VLAN. This is a value between 2 and 4092.'], 'required': True}",
    "state": "{'description': ["State the action to perform. Use 'present' to create vlan and 'absent' to delete vlan."], 'required': True, 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: create a VLAN
  pn_vlan:
    state: 'present'
    pn_vlanid: 1854
    pn_scope: fabric

- name: delete VLANs
  pn_vlan:
    state: 'absent'
    pn_vlanid: 1854

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
