# Ansible module: ansible.module_na_elementsw_snapshot


NetApp Element Software Manage Snapshots

## Description

Create, Modify or Delete Snapshot on Element OS Cluster.

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['Account ID or Name of Parent/Source Volume.'], 'required': True}",
    "enable_remote_replication": "{'description': ['Flag, whether to replicate the snapshot created to a remote replication cluster.', "To enable specify 'true' value."], 'type': 'bool'}",
    "expiration_time": "{'description': ['The date and time (format ISO 8601 date string) at which this snapshot will expire.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['Name of new snapshot create.', 'If unspecified, date and time when the snapshot was taken is used.']}",
    "password": "{'required': True, 'description': ['Element OS access account password'], 'aliases': ['pass']}",
    "retention": "{'description': ['Retention period for the snapshot.', "Format is 'HH:mm:ss'."]}",
    "snap_mirror_label": "{'description': ['Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint.']}",
    "src_snapshot_id": "{'description': ['ID or Name of an existing snapshot.', 'Required when C(state=present), to modify snapshot properties.', 'Required when C(state=present), to create snapshot from another snapshot in the volume.', 'Required when C(state=absent), to delete snapshot.']}",
    "src_volume_id": "{'description': ['ID or Name of active volume.'], 'required': True}",
    "state": "{'description': ['Whether the specified snapshot should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['Element OS access account user-name'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Create snapshot
     tags:
     - elementsw_create_snapshot
     na_elementsw_snapshot:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       src_volume_id: 118
       account_id: sagarsh
       name: newsnapshot-1

   - name: Modify Snapshot
     tags:
     - elementsw_modify_snapshot
     na_elementsw_snapshot:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       src_volume_id: sagarshansivolume
       src_snapshot_id: test1
       account_id: sagarsh
       expiration_time: '2018-06-16T12:24:56Z'
       enable_remote_replication: false

   - name: Delete Snapshot
     tags:
     - elementsw_delete_snapshot
     na_elementsw_snapshot:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       src_snapshot_id: deltest1
       account_id: sagarsh
       src_volume_id: sagarshansivolume

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
