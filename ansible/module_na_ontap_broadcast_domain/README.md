# Ansible module: ansible.module_na_ontap_broadcast_domain


NetApp ONTAP manage broadcast domains

## Description

Modify a ONTAP broadcast domain.

## Requirements

TODO

## Arguments

``` json
{
    "broadcast_domain": "{'description': ['Specify the broadcast_domain name'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ipspace": "{'description': ['Specify the required ipspace for the broadcast domain.', 'A domain ipspace can not be modified after the domain has been created']}",
    "mtu": "{'description': ['Specify the required mtu for the broadcast domain']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "ports": "{'description': ['Specify the ports associated with this broadcast domain. Should be comma separated']}",
    "state": "{'description': ['Whether the specified broadcast domain should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: create broadcast domain
      na_ontap_broadcast_domain:
        state=present
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        broadcast_domain=123kevin
        mtu=1000
        ipspace=Default
        ports=khutton-vsim1:e0d-12,khutton-vsim1:e0d-13
    - name: delete broadcast domain
      na_ontap_broadcast_domain:
        state=absent
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        broadcast_domain=123kevin
        mtu=1000
        ipspace=Default
    - name: modify broadcast domain
      na_ontap_broadcast_domain:
        state=absent
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        broadcast_domain=123kevin
        mtu=1100
        ipspace=Default

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
