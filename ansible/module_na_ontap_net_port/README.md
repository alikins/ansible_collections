# Ansible module: ansible.module_na_ontap_net_port


NetApp ONTAP network ports

## Description

Modify a ONTAP network port.

## Requirements

TODO

## Arguments

``` json
{
    "autonegotiate_admin": "{'description': ['Enables or disables Ethernet auto-negotiation of speed, duplex and flow control.']}",
    "duplex_admin": "{'description': ['Specifies the user preferred duplex setting of the port.', 'Valid values auto, half, full']}",
    "flowcontrol_admin": "{'description': ['Specifies the user preferred flow control setting of the port.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ipspace": "{'description': ["Specifies the port's associated IPspace name.", "The 'Cluster' ipspace is reserved for cluster ports."]}",
    "mtu": "{'description': ['Specifies the maximum transmission unit (MTU) reported by the port.']}",
    "node": "{'description': ['Specifies the name of node.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "port": "{'description': ['Specifies the name of port.'], 'required': True}",
    "speed_admin": "{'description': ['Specifies the user preferred speed setting of the port.']}",
    "state": "{'description': ['Whether the specified net port should exist or not.'], 'choices': ['present'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Modify Net Port
      na_ontap_net_port:
        state=present
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        node={{ Vsim server name }}
        port=e0d
        autonegotiate_admin=true

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
