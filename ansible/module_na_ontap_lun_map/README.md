# Ansible module: ansible.module_na_ontap_lun_map


NetApp ONTAP LUN maps

## Description

Map and unmap LUNs on NetApp ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "initiator_group_name": "{'description': ['Initiator group to map to the given LUN.'], 'required': True}",
    "lun_id": "{'description': ['LUN ID assigned for the map.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "path": "{'description': ['Path of the LUN..'], 'required': True}",
    "state": "{'description': ['Whether the specified LUN should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'required': True, 'description': ['The name of the vserver to use.']}",
}
```

## Examples


``` yaml

- name: Create LUN mapping
  na_ontap_lun_map:
    state: present
    initiator_group_name: ansibleIgroup3234
    path: /vol/iscsi_path/iscsi_lun
    vserver: ci_dev
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Unmap LUN
  na_ontap_lun_map:
    state: absent
    initiator_group_name: ansibleIgroup3234
    path: /vol/iscsi_path/iscsi_lun
    vserver: ci_dev
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
