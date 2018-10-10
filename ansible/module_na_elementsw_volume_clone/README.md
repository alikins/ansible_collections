# Ansible module: ansible.module_na_elementsw_volume_clone


NetApp Element Software Create Volume Clone

## Description

Create volume clones on Element OS

## Requirements

TODO

## Arguments

``` json
{
    "access": "{'choices': ['readOnly', 'readWrite', 'locked', 'replicationTarget'], 'description': ['Access allowed for the volume.', 'If unspecified, the access settings of the clone will be the same as the source.', 'readOnly - Only read operations are allowed.', 'readWrite - Reads and writes are allowed.', 'locked - No reads or writes are allowed.', 'replicationTarget - Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.']}",
    "account_id": "{'description': ['Account ID for the owner of this cloned volume. id may be a numeric identifier or an account name.'], 'required': True}",
    "attributes": "{'description': ['A YAML dictionary of attributes that you would like to apply on this cloned volume.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['The name of the clone.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "size": "{'description': ['The size of the cloned volume in (size_unit).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "src_snapshot_id": "{'description': ['The id of the snapshot to clone. id may be a numeric identifier or a snapshot name.']}",
    "src_volume_id": "{'description': ['The id of the src volume to clone. id may be a numeric identifier or a volume name.'], 'required': True}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

    - name: Clone Volume
      na_elementsw_volume_clone:
        hostname: "{{ elementsw_hostname }}"
        username: "{{ elementsw_username }}"
        password: "{{ elementsw_password }}"
        name: CloneAnsibleVol
        src_volume_id: 123
        src_snapshot_id: 41
        account_id: 3
        size: 1
        size_unit: gb
        access: readWrite
        attributes: {"virtual_network_id": 12345}


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
