# Ansible module: ansible.module_na_ontap_gather_facts


NetApp information gatherer

## Description

This module allows you to gather various information about ONTAP configuration

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Returns "info"'], 'default': 'info', 'required': False, 'choices': ['info']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Get NetApp info (Password Authentication)
  na_ontap_gather_facts:
    state: info
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"

- debug:
    var: ontap_facts

```

## License

TODO

## Author Information
  - ['Piotr Olczak (polczak@redhat.com)']
