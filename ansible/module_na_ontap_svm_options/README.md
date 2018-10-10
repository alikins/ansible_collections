# Ansible module: ansible.module_na_ontap_svm_options


NetApp ONTAP Modify SVM Options

## Description

Modify ONTAP SVM Options
Only Options that appear on "vserver options show" can be set

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the option.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "value": "{'description': ['Value of the option.', 'Value must be in quote']}",
    "vserver": "{'description': ['The name of the vserver to which this option belongs to.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Set SVM Options
      na_ontap_svm_options:
        vserver: "{{ netapp_vserver_name }}"
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
        name: snmp.enable
        value: 'on'

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
