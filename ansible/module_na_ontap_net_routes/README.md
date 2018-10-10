# Ansible module: ansible.module_na_ontap_net_routes


NetApp ONTAP network routes

## Description

Modify ONTAP network routes.

## Requirements

TODO

## Arguments

``` json
{
    "destination": "{'description': ['Specify the route destination.', 'Example 10.7.125.5/20, fd20:13::/64.'], 'required': True}",
    "gateway": "{'description': ['Specify the route gateway.', 'Example 10.7.125.1, fd20:13::1.'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "metric": "{'description': ['Specify the route metric.', 'If this field is not provided the default will be set to 20.']}",
    "new_destination": "{'description': ['Specify the new route destination.']}",
    "new_gateway": "{'description': ['Specify the new route gateway.']}",
    "new_metric": "{'description': ['Specify the new route metric.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether you want to create or delete a network route.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the vserver.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: create route
      na_ontap_net_routes:
        state=present
        vserver={{ Vserver name }}
        username={{ netapp_username }}
        password={{ netapp_password }}
        hostname={{ netapp_hostname }}
        destination=10.7.125.5/20
        gateway=10.7.125.1
        metric=30

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
