# Ansible module: ansible.module_pn_vrouterlbif


CLI command to add/remove vrouter-loopback-interface

## Description

Execute vrouter-loopback-interface-add, vrouter-loopback-interface-remove commands.
Each fabric, cluster, standalone switch, or virtual network (VNET) can provide its tenants with a virtual router (vRouter) service that forwards traffic between networks and implements Layer 3 protocols.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_index": "{'description': ['Specify the interface index from 1 to 255.']}",
    "pn_interface_ip": "{'description': ['Specify the IP address.'], 'required': True}",
    "pn_vrouter_name": "{'description': ['Specify the name of the vRouter.'], 'required': True}",
    "state": "{'description': ["State the action to perform. Use 'present' to add vrouter loopback interface and 'absent' to remove vrouter loopback interface."], 'required': True, 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: add vrouter-loopback-interface
  pn_vrouterlbif:
    state: 'present'
    pn_vrouter_name: 'ansible-vrouter'
    pn_interface_ip: '104.104.104.1'

- name: remove vrouter-loopback-interface
  pn_vrouterlbif:
    state: 'absent'
    pn_vrouter_name: 'ansible-vrouter'
    pn_interface_ip: '104.104.104.1'

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
