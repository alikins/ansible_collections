# Ansible module: ansible.module_sf_volume_manager


Manage SolidFire volumes

## Description

Create, destroy, or update volumes on SolidFire

## Requirements

TODO

## Arguments

``` json
{
    "512emulation": "{'description': ['Should the volume provide 512-byte sector emulation?', 'Required when C(state=present)']}",
    "access": "{'description': ['Access allowed for the volume.', 'readOnly: Only read operations are allowed.', 'readWrite: Reads and writes are allowed.', 'locked: No reads or writes are allowed.', 'replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.', 'If unspecified, the access settings of the clone will be the same as the source.'], 'choices': ['readOnly', 'readWrite', 'locked', 'replicationTarget']}",
    "account_id": "{'description': ['Account ID for the owner of this volume.'], 'required': True}",
    "attributes": "{'description': ['A YAML dictionary of attributes that you would like to apply on this volume.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['The name of the volume to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "qos": "{'description': ['Initial quality of service settings for this volume. Configure as dict in playbooks.']}",
    "size": "{'description': ['The size of the volume in (size_unit).', 'Required when C(state = present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "volume_id": "{'description': ['The ID of the volume to manage or update.', "In order to create multiple volumes with the same name, but different volume_ids, please declare the I(volume_id) parameter with an arbitrary value. However, the specified volume_id will not be assigned to the newly created volume (since it's an auto-generated property)."]}",
}
```

## Examples


``` yaml

   - name: Create Volume
     sf_volume_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       name: AnsibleVol
       qos: {minIOPS: 1000, maxIOPS: 20000, burstIOPS: 50000}
       account_id: 3
       enable512e: False
       size: 1
       size_unit: gb

   - name: Update Volume
     sf_volume_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       name: AnsibleVol
       account_id: 3
       access: readWrite

   - name: Delete Volume
     sf_volume_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: absent
       name: AnsibleVol
       account_id: 2

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
