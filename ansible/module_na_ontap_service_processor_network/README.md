# Ansible module: ansible.module_na_ontap_service_processor_network


NetApp ONTAP service processor network

## Description

Modify a ONTAP service processor network

## Requirements

TODO

## Arguments

``` json
{
    "address_type": "{'description': ['Specify address class.'], 'required': True, 'choices': ['ipv4', 'ipv6']}",
    "dhcp": "{'description': ['Specify dhcp type.'], 'choices': ['v4', 'none']}",
    "gateway_ip_address": "{'description': ['Specify the gateway ip.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ip_address": "{'description': ['Specify the service processor ip address.']}",
    "is_enabled": "{'description': ['Specify whether to enable or disable the service processor network.'], 'required': True, 'type': 'bool'}",
    "netmask": "{'description': ['Specify the service processor netmask.']}",
    "node": "{'description': ['The node where the service processor network should be enabled'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "prefix_length": "{'description': ['Specify the service processor prefix_length.']}",
    "state": "{'description': ['Whether the specified service processor network should exist or not.'], 'choices': ['present'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Modify Service Processor Network
      na_ontap_service_processor_network:
        state=present
        address_type=ipv4
        is_enabled=true
        dhcp=v4
        node=FPaaS-A300-01
        node={{ netapp_node }}
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
