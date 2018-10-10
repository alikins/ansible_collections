# Ansible module: ansible.module_na_ontap_cifs_acl


NetApp ONTAP manage cifs-share-access-control

## Description

Create or destroy or modify cifs-share-access-controls on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "permission": "{'choices': ['no_access', 'read', 'change', 'full_control'], 'description': ['-"The access rights that the user or group has on the defined CIFS share."']}",
    "share_name": "{'description': ['The name of the cifs-share-access-control to manage.'], 'required': True}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified CIFS share acl should exist or not.'], 'default': 'present'}",
    "user_or_group": "{'description': ['The user or group name for which the permissions are listed.'], 'required': True}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['Name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create CIFS share acl
      na_ontap_cifs_acl:
        state: present
        share_name: cifsShareName
        user_or_group: Everyone
        permission: read
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Modify CIFS share acl permission
      na_ontap_cifs_acl:
        state: present
        share_name: cifsShareName
        permission: change
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
