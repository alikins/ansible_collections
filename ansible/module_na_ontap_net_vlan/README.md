# Ansible module: ansible.module_na_ontap_net_vlan


NetApp ONTAP network VLAN

## Description

Create or Delete a network VLAN

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "node": "{'description': ['Node name of VLAN interface.'], 'required': True}",
    "parent_interface": "{'description': ['The interface that hosts the VLAN interface.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified network VLAN should exist or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vlanid": "{'description': ['The VLAN id. Ranges from 1 to 4094.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: create VLAN
      na_ontap_net_vlan:
        state=present
        vlanid=13
        node={{ vlan node }}
        parent_interface={{ vlan parent interface name }}
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
