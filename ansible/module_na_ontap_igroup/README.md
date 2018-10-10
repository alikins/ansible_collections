# Ansible module: ansible.module_na_ontap_igroup


NetApp ONTAP iSCSI igroup configuration

## Description

create, destroy or rename Igroups and add or remove initiator in igroups.

## Requirements

TODO

## Arguments

``` json
{
    "bind_portset": "{'description': ['Name of a current portset to bind to the newly created igroup.']}",
    "force_remove_initiator": "{'description': ['Forcibly remove the initiator even if there are existing LUNs mapped to this initiator group.'], 'type': 'bool'}",
    "from_name": "{'description': ['Name of igroup to rename to name.'], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "initiator": "{'description': ['WWPN, WWPN Alias, or iSCSI name of Initiator to add or remove.']}",
    "initiator_group_type": "{'description': ['Type of the initiator group.', 'Required when C(state=present).'], 'choices': ['fcp', 'iscsi', 'mixed']}",
    "name": "{'description': ['The name of the igroup to manage.'], 'required': True}",
    "ostype": "{'description': ['OS type of the initiators within the group.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified Igroup should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create Igroup
      na_ontap_igroup:
        state: present
        name: ansibleIgroup3
        initiator_group_type: iscsi
        ostype: linux
        initiator: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: rename Igroup
      na_ontap_igroup:
        state: present
        from_name: ansibleIgroup3
        name: testexamplenewname
        initiator_group_type: iscsi
        ostype: linux
        initiator: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: remove Igroup
      na_ontap_igroup:
        state: absent
        name: ansibleIgroup3
        initiator_group_type: iscsi
        ostype: linux
        initiator: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
