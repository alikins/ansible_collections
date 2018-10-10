# Ansible module: ansible.module_pn_show


Run show commands on nvOS device

## Description

Execute show command in the nodes and returns the results read from the device.

## Requirements

TODO

## Arguments

``` json
{
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch(es) to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_command": "{'description': ['The C(pn_command) takes a CLI show command as value.'], 'required': True}",
    "pn_options": "{'description': ['Specify formatting options.']}",
    "pn_parameters": "{'description': ["Display output using a specific parameter. Use 'all' to display possible output. List of comma separated parameters."]}",
}
```

## Examples


``` yaml

- name: run the vlan-show command
  pn_show:
    pn_command: 'vlan-show'
    pn_parameters: id,scope,ports
    pn_options: 'layout vertical'

- name: run the vlag-show command
  pn_show:
    pn_command: 'vlag-show'
    pn_parameters: 'id,name,cluster,mode'
    pn_options: 'no-show-headers'

- name: run the cluster-show command
  pn_show:
    pn_command: 'cluster-show'

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
