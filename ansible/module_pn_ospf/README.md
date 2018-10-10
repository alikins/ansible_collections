# Ansible module: ansible.module_pn_ospf


CLI command to add/remove ospf protocol to a vRouter

## Description

Execute vrouter-ospf-add, vrouter-ospf-remove command.
This command adds/removes Open Shortest Path First(OSPF) routing protocol to a virtual router(vRouter) service.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch to run the CLI on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_network_ip": "{'description': ['Specify the network IP (IPv4 or IPv6) address.'], 'required': True}",
    "pn_ospf_area": "{'description': ['Stub area number for the configuration. Required for vrouter-ospf-add.']}",
    "pn_vrouter_name": "{'description': ['Specify the name of the vRouter.'], 'required': True}",
    "state": "{'description': ["Assert the state of the ospf. Use 'present' to add ospf and 'absent' to remove ospf."], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: "Add OSPF to vrouter"
  pn_ospf:
    state: present
    pn_vrouter_name: name-string
    pn_network_ip: 192.168.11.2/24
    pn_ospf_area: 1.0.0.0

- name: "Remove OSPF from vrouter"
  pn_ospf:
    state: absent
    pn_vrouter_name: name-string

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
