# Ansible module: ansible.module_na_cdot_volume


Manage NetApp cDOT volumes

## Description

Create or destroy volumes on NetApp cDOT

## Requirements

TODO

## Arguments

``` json
{
    "aggregate_name": "{'description': ['The name of the aggregate the flexvol should exist on. Required when C(state=present).']}",
    "export_policy": "{'description': ['Export policy to set for the specified junction path.'], 'required': False, 'default': 'default', 'version_added': '2.6'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "infinite": "{'description': ['Set True if the volume is an Infinite Volume.'], 'type': 'bool', 'default': False}",
    "junction_path": "{'description': ['Junction path where to mount the volume'], 'required': False, 'version_added': '2.6'}",
    "name": "{'description': ['The name of the volume to manage.'], 'required': True}",
    "online": "{'description': ['Whether the specified volume is online, or not.'], 'type': 'bool', 'default': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "size": "{'description': ['The size of the volume in (size_unit). Required when C(state=present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "snapshot_policy": "{'description': ['Snapshot policy to set for the specified volume.'], 'required': False, 'default': 'default', 'version_added': '2.6'}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vserver": "{'description': ['Name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml


    - name: Create FlexVol
      na_cdot_volume:
        state: present
        name: ansibleVolume
        infinite: False
        aggregate_name: aggr1
        size: 20
        size_unit: mb
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
        junction_path: /ansibleVolume
        export_policy: all_nfs_networks
        snapshot_policy: daily

    - name: Make FlexVol offline
      na_cdot_volume:
        state: present
        name: ansibleVolume
        infinite: False
        online: False
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
