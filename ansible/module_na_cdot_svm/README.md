# Ansible module: ansible.module_na_cdot_svm


Manage NetApp cDOT svm

## Description

Create or destroy svm on NetApp cDOT

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "name": "{'description': ['The name of the SVM to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "root_volume": "{'description': ['Root volume of the SVM. Required when C(state=present).']}",
    "root_volume_aggregate": "{'description': ['The aggregate on which the root volume will be created.', 'Required when C(state=present).']}",
    "root_volume_security_style": "{'description': ['Security Style of the root volume.', 'When specified as part of the vserver-create, this field represents the security style for the Vserver root volume.', 'When specified as part of vserver-get-iter call, this will return the list of matching Vservers.', "Possible values are 'unix', 'ntfs', 'mixed'.", "The 'unified' security style, which applies only to Infinite Volumes, cannot be applied to a Vserver's root volume.", 'Valid options are "unix" for NFS, "ntfs" for CIFS, "mixed" for Mixed, "unified" for Unified.', 'Required when C(state=present)'], 'choices': ['unix', 'ntfs', 'mixed', 'unified']}",
    "state": "{'description': ['Whether the specified SVM should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml


    - name: Create SVM
      na_cdot_svm:
        state: present
        name: ansibleVServer
        root_volume: vol1
        root_volume_aggregate: aggr1
        root_volume_security_style: mixed
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
