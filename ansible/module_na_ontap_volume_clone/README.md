# Ansible module: ansible.module_na_ontap_volume_clone


NetApp ONTAP manage volume clones

## Description

Create NetApp ONTAP volume clones.
A FlexClone License is required to use this module

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "parent_snapshot": "{'description': ['Parent snapshot in which volume clone is created off.']}",
    "parent_volume": "{'description': ['The parent volume of the volume clone being created.'], 'required': True}",
    "parent_vserver": "{'description': ['Vserver of parent volume in which clone is created off.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "qos_policy_group_name": "{'description': ['The qos-policy-group-name which should be set for volume clone.']}",
    "space_reserve": "{'description': ['The space_reserve setting which should be used for the volume clone.'], 'choices': ['volume', 'none']}",
    "state": "{'description': ['Whether volume clone should be created.'], 'choices': ['present'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "volume": "{'description': ['The name of the volume clone being created.'], 'required': True}",
    "volume_type": "{'description': ['The volume-type setting which should be used for the volume clone.'], 'choices': ['rw', 'dp']}",
    "vserver": "{'description': ['Vserver in which the volume clone should be created.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: create volume clone
      na_ontap_volume_clone:
        state=present
        username=admin
        password=netapp1!
        hostname=10.193.74.27
        vserver=vs_hack
        parent_volume=normal_volume
        volume=clone_volume_7
        space_reserve=none
        parent_snapshot=backup1

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
