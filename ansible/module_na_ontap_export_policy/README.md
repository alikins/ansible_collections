# Ansible module: ansible.module_na_ontap_export_policy


NetApp ONTAP manage export-policy

## Description

Create or destroy or rename export-policies on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "from_name": "{'description': ['The name of the export-policy to be renamed.'], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the export-policy to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified export policy should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['Name of the vserver to use.']}",
}
```

## Examples


``` yaml

    - name: Create Export Policy
      na_ontap_export_policy:
        state: present
        name: ansiblePolicyName
        vserver: vs_hack
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Rename Export Policy
      na_ontap_export_policy:
        action: present
        from_name: ansiblePolicyName
        vserver: vs_hack
        name: newPolicyName
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Delete Export Policy
      na_ontap_export_policy:
        state: absent
        name: ansiblePolicyName
        vserver: vs_hack
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
