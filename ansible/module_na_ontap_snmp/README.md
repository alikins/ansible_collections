# Ansible module: ansible.module_na_ontap_snmp


NetApp ONTAP SNMP community

## Description

Create/Delete SNMP community

## Requirements

TODO

## Arguments

``` json
{
    "access_control": "{'description': ["Access control for the community. The only supported value is 'ro' (read-only)"], 'required': True}",
    "community_name": "{'description': ['The name of the SNMP community to manage.'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified SNMP community should exist or not.'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Create SNMP community
      na_ontap_snmp:
        state: present
        community_name: communityName
        access_control: 'ro'
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Delete SNMP community
      na_ontap_snmp:
        state: absent
        community_name: communityName
        access_control: 'ro'
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
