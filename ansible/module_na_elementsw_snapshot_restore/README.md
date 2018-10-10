# Ansible module: ansible.module_na_elementsw_snapshot_restore


NetApp Element Software Restore Snapshot

## Description

Element OS Cluster restore snapshot to volume.

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['Account ID or Name of Parent/Source Volume.'], 'required': True}",
    "dest_volume_name": "{'description': ['New Name of destination for restoring the snapshot'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "src_snapshot_id": "{'description': ['ID or Name of an existing snapshot.'], 'required': True}",
    "src_volume_id": "{'description': ['ID or Name of source active volume.'], 'required': True}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Restore snapshot to volume
     tags:
     - elementsw_create_snapshot_restore
     na_elementsw_snapshot_restore:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       account_id: ansible-1
       src_snapshot_id: snapshot_20171021
       src_volume_id: volume-playarea
       dest_volume_name: dest-volume-area


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
