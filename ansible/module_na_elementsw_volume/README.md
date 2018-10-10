# Ansible module: ansible.module_na_elementsw_volume


NetApp Element Software Manage Volumes

## Description

Create, destroy, or update volumes on ElementSW

## Requirements

TODO

## Arguments

``` json
{
    "access": "{'description': ['Access allowed for the volume.', 'readOnly           Only read operations are allowed.', 'readWrite          Reads and writes are allowed.', 'locked             No reads or writes are allowed.', 'replicationTarget  Identify a volume as the target volume for a paired set of volumes.', 'If the volume is not paired, the access status is locked.', 'If unspecified, the access settings of the clone will be the same as the source.'], 'choices': ['readOnly', 'readWrite', 'locked', 'replicationTarget']}",
    "account_id": "{'description': ['Account ID for the owner of this volume.', 'It accepts Account_id or Account_name'], 'required': True}",
    "attributes": "{'description': ['A YAML dictionary of attributes that you would like to apply on this volume.']}",
    "enable512e": "{'description': ['Required when C(state=present)', 'Should the volume provide 512-byte sector emulation?'], 'type': 'bool', 'aliases': ['512emulation']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['The name of the volume to manage.', 'It accepts volume_name or volume_id'], 'required': True}",
    "password": "{'required': True, 'description': ['ElementSW access account password'], 'aliases': ['pass']}",
    "qos": "{'description': ['Initial quality of service settings for this volume. Configure as dict in playbooks.']}",
    "size": "{'description': ['The size of the volume in (size_unit).', 'Required when C(state = present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['ElementSW access account user-name'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Create Volume
     na_elementsw_volume:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       name: AnsibleVol
       qos: {minIOPS: 1000, maxIOPS: 20000, burstIOPS: 50000}
       account_id: 3
       enable512e: False
       size: 1
       size_unit: gb

   - name: Update Volume
     na_elementsw_volume:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       name: AnsibleVol
       account_id: 3
       access: readWrite

   - name: Delete Volume
     na_elementsw_volume:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       name: AnsibleVol
       account_id: 2

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
