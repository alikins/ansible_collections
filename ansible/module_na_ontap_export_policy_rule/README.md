# Ansible module: ansible.module_na_ontap_export_policy_rule


NetApp ONTAP manage export policy rules

## Description

Create or delete or modify export rules in ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "allow_suid": "{'description': ["If 'true', NFS server will honor SetUID bits in SETATTR operation. Default value on creation is 'true'"], 'type': 'bool'}",
    "client_match": "{'description': ['List of Client Match Hostnames, IP Addresses, Netgroups, or Domains']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "policy_name": "{'description': ['The name of the export rule to manage.'], 'required': True}",
    "protocol": "{'description': ["Client access protocol. Default value is 'any'"], 'choices': ['any', 'nfs', 'nfs3', 'nfs4', 'cifs', 'flexcache'], 'default': 'any'}",
    "ro_rule": "{'description': ['Read only access specifications for the rule'], 'choices': ['any', 'none', 'never', 'krb5', 'krb5i', 'krb5p', 'ntlm', 'sys']}",
    "rule_index": "{'description': ['rule index of the export policy for delete and modify']}",
    "rw_rule": "{'description': ['Read Write access specifications for the rule'], 'choices': ['any', 'none', 'never', 'krb5', 'krb5i', 'krb5p', 'ntlm', 'sys']}",
    "state": "{'description': ['Whether the specified export policy rule should exist or not.'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "super_user_security": "{'description': ['Read Write access specifications for the rule'], 'choices': ['any', 'none', 'never', 'krb5', 'krb5i', 'krb5p', 'ntlm', 'sys']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['Name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create ExportPolicyRule
      na_ontap_export_policy_rule:
        state: present
        policy_name: default123
        vserver: ci_dev
        client_match: 0.0.0.0/0
        ro_rule: any
        rw_rule: any
        protocol: any
        super_user_security: any
        allow_suid: true
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Delete ExportPolicyRule
      na_ontap_export_policy_rule:
        state: absent
        policy_name: default123
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Modify ExportPolicyRule
      na_ontap_export_policy_rule:
        state: present
        policy_name: default123
        client_match: 0.0.0.0/0
        ro_rule: any
        rw_rule: any
        super_user_security: none
        protocol: any
        allow_suid: false
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
