# Ansible module: ansible.module_na_ontap_snapshot


NetApp ONTAP manage Snapshots

## Description

Create/Modify/Delete ONTAP snapshots

## Requirements

TODO

## Arguments

``` json
{
    "async_bool": "{'description': ['If true, the snapshot is to be created asynchronously.'], 'type': 'bool'}",
    "comment": "{'description': ['A human readable comment attached with the snapshot. The size of the comment can be at most 255 characters.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ignore_owners": "{'description': ['if this field is true, snapshot will be deleted even if some other processes are accessing it.'], 'type': 'bool'}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "snapmirror_label": "{'description': ['A human readable SnapMirror Label attached with the snapshot. Size of the label can be at most 31 characters.']}",
    "snapshot": "{'description': ['Name of the snapshot to be managed. The maximum string length is 256 characters.'], 'required': True}",
    "snapshot_instance_uuid": "{'description': ['The 128 bit unique snapshot identifier expressed in the form of UUID.']}",
    "state": "{'description': ['If you want to create/modify a snapshot, or delete it.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "volume": "{'description': ['Name of the volume on which the snapshot is to be created.'], 'required': True}",
    "vserver": "{'description': ['The Vserver name']}",
}
```

## Examples


``` yaml

    - name: create SnapShot
      tags:
        - create
      na_ontap_snapshot:
        state=present
        snapshot={{ snapshot name }}
        volume={{ vol name }}
        comment="i am a comment"
        vserver={{ vserver name }}
        username={{ netapp username }}
        password={{ netapp password }}
        hostname={{ netapp hostname }}
    - name: delete SnapShot
      tags:
        - delete
      na_ontap_snapshot:
        state=absent
        snapshot={{ snapshot name }}
        volume={{ vol name }}
        vserver={{ vserver name }}
        username={{ netapp username }}
        password={{ netapp password }}
        hostname={{ netapp hostname }}
    - name: modify SnapShot
      tags:
        - modify
      na_ontap_snapshot:
        state=present
        snapshot={{ snapshot name }}
        comment="New comments are great"
        volume={{ vol name }}
        vserver={{ vserver name }}
        username={{ netapp username }}
        password={{ netapp password }}
        hostname={{ netapp hostname }}

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
