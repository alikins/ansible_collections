# Ansible module: ansible.module_na_ontap_volume


NetApp ONTAP manage volumes

## Description

Create or destroy or modify volumes on NetApp ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate_name": "{'description': ['The name of the aggregate the flexvol should exist on.', 'Required when C(state=present).']}",
    "efficiency_policy": "{'description': ['Allows a storage efficiency policy to be set on volume creation.'], 'version_added': '2.7'}",
    "encrypt": "{'type': 'bool', 'description': ['Whether or not to enable Volume Encryption.'], 'default': False, 'version_added': '2.7'}",
    "from_name": "{'description': ['Name of the existing volume to be renamed to name.'], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "is_infinite": "{'type': 'bool', 'description': ['Set True if the volume is an Infinite Volume. Deleting an infinite volume is asynchronous.']}",
    "is_online": "{'type': 'bool', 'description': ['Whether the specified volume is online, or not.'], 'default': True}",
    "junction_path": "{'description': ['Junction path of the volume.']}",
    "name": "{'description': ['The name of the volume to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "percent_snapshot_space": "{'description': ['Amount of space reserved for snapshot copies of the volume.']}",
    "policy": "{'description': ['Name of the export policy.']}",
    "size": "{'description': ['The size of the volume in (size_unit). Required when C(state=present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "space_guarantee": "{'description': ['Space guarantee style for the volume.'], 'choices': ['none', 'volume']}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['The volume type, either read-write (RW) or data-protection (DP).']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "volume_security_style": "{'description': ['The security style associated with this volume.'], 'choices': ['mixed', 'ntfs', 'unified', 'unix'], 'default': 'mixed'}",
    "vserver": "{'description': ['Name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml


    - name: Create FlexVol
      na_ontap_volume:
        state: present
        name: ansibleVolume
        is_infinite: False
        aggregate_name: aggr1
        size: 20
        size_unit: mb
        junction_path: /ansibleVolume11
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Make FlexVol offline
      na_ontap_volume:
        state: present
        name: ansibleVolume
        is_infinite: False
        is_online: False
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
