# Ansible module: ansible.module_pn_ospfarea


CLI command to add/remove ospf area to/from a vrouter

## Description

Execute vrouter-ospf-add, vrouter-ospf-remove command.
This command adds/removes Open Shortest Path First(OSPF) area to/from a virtual router(vRouter) service.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Login password.'], 'required': True}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the CLI on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Login username.'], 'required': True}",
    "pn_ospf_area": "{'description': ['Specify the OSPF area number.'], 'required': True}",
    "pn_prefix_listin": "{'description': ['OSPF prefix list for filtering incoming packets.']}",
    "pn_prefix_listout": "{'description': ['OSPF prefix list for filtering outgoing packets.']}",
    "pn_quiet": "{'description': ['Enable/disable system information.'], 'required': False, 'default': True}",
    "pn_stub_type": "{'description': ['Specify the OSPF stub type.'], 'choices': ['none', 'stub', 'stub-no-summary', 'nssa', 'nssa-no-summary']}",
    "pn_vrouter_name": "{'description': ['Specify the name of the vRouter.'], 'required': True}",
    "state": "{'description': ["State the action to perform. Use 'present' to add ospf-area, 'absent' to remove ospf-area and 'update' to modify ospf-area."], 'required': True, 'choices': ['present', 'absent', 'update']}",
}
```

## Examples


``` yaml

- name: "Add OSPF area to vrouter"
  pn_ospfarea:
    state: present
    pn_cliusername: admin
    pn_clipassword: admin
    pn_ospf_area: 1.0.0.0
    pn_stub_type: stub

- name: "Remove OSPF from vrouter"
  pn_ospf:
    state: absent
    pn_cliusername: admin
    pn_clipassword: admin
    pn_vrouter_name: name-string
    pn_ospf_area: 1.0.0.0

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
