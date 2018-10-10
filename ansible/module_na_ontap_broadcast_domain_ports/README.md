# Ansible module: ansible.module_na_ontap_broadcast_domain_ports


NetApp ONTAP manage broadcast domain ports

## Description

Add or remove ONTAP broadcast domain ports.  Existing ports that are not listed are kept.

## Requirements

TODO

## Arguments

``` json
{
    "broadcast_domain": "{'description': ['Specify the broadcast_domain name'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ipspace": "{'description': ['Specify the ipspace for the broadcast domain']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "ports": "{'description': ['Specify the list of ports to add to or remove from this broadcast domain.']}",
    "state": "{'description': ['Whether the specified broadcast domain should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: create broadcast domain ports
      na_ontap_broadcast_domain_ports:
        state=present
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        broadcast_domain=123kevin
        ports=khutton-vsim1:e0d-13
    - name: delete broadcast domain ports
      na_ontap_broadcast_domain_ports:
        state=absent
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        broadcast_domain=123kevin
        ports=khutton-vsim1:e0d-13

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
