# Ansible module: ansible.module_pn_vrouter


CLI command to create/delete/modify a vrouter

## Description

Execute vrouter-create, vrouter-delete, vrouter-modify command.
Each fabric, cluster, standalone switch, or virtual network (VNET) can provide its tenants with a virtual router (vRouter) service that forwards traffic between networks and implements Layer 3 protocols.
C(vrouter-create) creates a new vRouter service.
C(vrouter-delete) deletes a vRouter service.
C(vrouter-modify) modifies a vRouter service.

## Requirements

TODO

## Arguments

``` json
{
    "pn_bgp_as": "{'description': ['Specify the Autonomous System Number(ASN) if the vRouter runs Border Gateway Protocol(BGP).']}",
    "pn_bgp_max_paths": "{'description': ['Specify the maximum number of paths for BGP. This is a number between 1 and 255 or 0 to unset.']}",
    "pn_bgp_options": "{'description': ["Specify other BGP options as a whitespaces separated string within single quotes ''."]}",
    "pn_bgp_redistribute": "{'description': ['Specify how BGP routes are redistributed.'], 'choices': ['static', 'connected', 'rip', 'ospf']}",
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the CLI on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_hw_vrrp_id": "{'description': ['Specifies the VRRP ID for a hardware vrouter.']}",
    "pn_name": "{'description': ['Specify the name of the vRouter.'], 'required': True}",
    "pn_ospf_options": "{'description': ["Specify other OSPF options as a whitespaces separated string within single quotes ''."]}",
    "pn_ospf_redistribute": "{'description': ['Specify how OSPF routes are redistributed.'], 'choices': ['static', 'connected', 'bgp', 'rip']}",
    "pn_rip_redistribute": "{'description': ['Specify how RIP routes are redistributed.'], 'choices': ['static', 'connected', 'ospf', 'bgp']}",
    "pn_router_id": "{'description': ['Specify the vRouter IP address.']}",
    "pn_router_type": "{'description': ['Specify if the vRouter uses software or hardware.', 'Note that if you specify hardware as router type, you cannot assign IP addresses using DHCP. You must specify a static IP address.'], 'choices': ['hardware', 'software']}",
    "pn_service_state": "{'description': ['Specify to enable or disable vRouter service.'], 'choices': ['enable', 'disable']}",
    "pn_service_type": "{'description': ['Specify if the vRouter is a dedicated or shared VNET service.'], 'choices': ['dedicated', 'shared']}",
    "pn_vnet": "{'description': ['Specify the name of the VNET.', 'Required for vrouter-create.']}",
    "state": "{'description': ["State the action to perform. Use 'present' to create vrouter, 'absent' to delete vrouter and 'update' to modify vrouter."], 'required': True, 'choices': ['present', 'absent', 'update']}",
}
```

## Examples


``` yaml

- name: create vrouter
  pn_vrouter:
    state: 'present'
    pn_name: 'ansible-vrouter'
    pn_vnet: 'ansible-fab-global'
    pn_router_id: 208.74.182.1

- name: delete vrouter
  pn_vrouter:
    state: 'absent'
    pn_name: 'ansible-vrouter'

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
