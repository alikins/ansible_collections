# Ansible module: ansible.module_na_ontap_cifs_server


NetApp ONTAP CIFS server configuration

## Description

Creating / deleting and modifying the CIFS server.

## Requirements

TODO

## Arguments

``` json
{
    "admin_password": "{'description': ['Specifies the cifs server admin password.']}",
    "admin_user_name": "{'description': ['Specifies the cifs server admin username.']}",
    "cifs_server_name": "{'description': ['Specifies the cifs_server name.'], 'required': True}",
    "domain": "{'description': ['The Fully Qualified Domain Name of the Windows Active Directory this CIFS server belongs to.']}",
    "force": "{'type': 'bool', 'description': ["If this is set and a machine account with the same name as specified in 'cifs_server_name' exists in the Active Directory, it will be overwritten and reused."], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ou": "{'description': ['The Organizational Unit (OU) within the Windows Active Directory this CIFS server belongs to.'], 'version_added': '2.7'}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "service_state": "{'description': ['CIFS Server Administrative Status.'], 'choices': ['stopped', 'started']}",
    "state": "{'description': ['Whether the specified cifs_server should exist or not.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
    "workgroup": "{'description': ['The NetBIOS name of the domain or workgroup this CIFS server belongs to.']}",
}
```

## Examples


``` yaml

    - name: Create cifs_server
      na_ontap_cifs_server:
        state: present
        vserver: svm1
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Delete cifs_server
      na_ontap_cifs_server:
        state: absent
        cifs_server_name: data2
        vserver: svm1
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
