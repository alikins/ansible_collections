# Ansible module: ansible.module_na_ontap_cifs


NetApp ONTAP manage cifs-share

## Description

Create or destroy or modify(path) cifs-share on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "path": "{'description': ['The file system path that is shared through this CIFS share. The path is the full, user visible path relative to the vserver root, and it might be crossing junction mount points. The path is in UTF8 and uses forward slash as directory separator'], 'required': False}",
    "share_name": "{'description': ['The name of the CIFS share. The CIFS share name is a UTF-8 string with the following characters being illegal; control characters from 0x00 to 0x1F, both inclusive, 0x22 (double quotes)'], 'required': True}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified CIFS share should exist or not.'], 'required': False, 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['Vserver containing the CIFS share.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create CIFS share
      na_ontap_cifs:
        state: present
        share_name: cifsShareName
        path: /
        vserver: vserverName
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Delete CIFS share
      na_ontap_cifs:
        state: absent
        share_name: cifsShareName
        vserver: vserverName
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Modify path CIFS share
      na_ontap_cifs:
        state: present
        share_name: pb_test
        vserver: vserverName
        path: /
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
