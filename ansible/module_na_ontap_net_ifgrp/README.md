# Ansible module: ansible.module_na_ontap_net_ifgrp


NetApp Ontap modify network interface group

## Description

Create, modify, destroy the network interface group

## Requirements

TODO

## Arguments

``` json
{
    "distribution_function": "{'description': ['Specifies the traffic distribution function for the ifgrp.'], 'choices': ['mac', 'ip', 'sequential', 'port']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "mode": "{'description': ['Specifies the link policy for the ifgrp.']}",
    "name": "{'description': ['Specifies the interface group name.'], 'required': True}",
    "node": "{'description': ['Specifies the name of node.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "port": "{'description': ['Adds the specified port.']}",
    "state": "{'description': ['Whether the specified network interface group should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: create ifgrp
      na_ontap_net_ifgrp:
        state=present
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        distribution_function=ip
        name=a0c
        port=e0d
        mode=multimode
        node={{ Vsim node name }}
    - name: delete ifgrp
      na_ontap_net_ifgrp:
        state=absent
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        name=a0c
        node={{ Vsim node name }}

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
