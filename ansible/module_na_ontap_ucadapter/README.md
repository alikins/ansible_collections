# Ansible module: ansible.module_na_ontap_ucadapter


NetApp ONTAP UC adapter configuration

## Description

modify the UC adapter mode and type taking pending type and mode into account.

## Requirements

TODO

## Arguments

``` json
{
    "adapter_name": "{'description': ['Specifies the adapter name.'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "mode": "{'description': ['Specifies the mode of the adapter.']}",
    "node_name": "{'description': ['Specifies the adapter home node.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified adapter should exist.'], 'required': False, 'choices': ['present'], 'default': 'present'}",
    "type": "{'description': ['Specifies the fc4 type of the adapter.']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Modify adapter
      na_ontap_adapter:
        state: present
        adapter_name: data2
        node_name: laurentn-vsim1
        mode: fc
        type: target
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
