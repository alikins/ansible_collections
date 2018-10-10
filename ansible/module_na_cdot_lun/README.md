# Ansible module: ansible.module_na_cdot_lun


Manage  NetApp cDOT luns

## Description

Create, destroy, resize luns on NetApp cDOT.

## Requirements

TODO

## Arguments

``` json
{
    "flexvol_name": "{'description': ['The name of the FlexVol the lun should exist on.', 'Required when C(state=present).']}",
    "force_remove": "{'description': ['If "true", override checks that prevent a LUN from being destroyed if it is online and mapped.', 'If "false", destroying an online and mapped LUN will fail.'], 'default': False}",
    "force_remove_fenced": "{'description': ['If "true", override checks that prevent a LUN from being destroyed while it is fenced.', 'If "false", attempting to destroy a fenced LUN will fail.', 'The default if not specified is "false". This field is available in Data ONTAP 8.2 and later.'], 'default': False}",
    "force_resize": "{'description': ['Forcibly reduce the size. This is required for reducing the size of the LUN to avoid accidentally reducing the LUN size.'], 'default': False}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "name": "{'description': ['The name of the lun to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "size": "{'description': ['The size of the lun in C(size_unit).', 'Required when C(state=present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "state": "{'description': ['Whether the specified lun should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vserver": "{'required': True, 'description': ['The name of the vserver to use.']}",
}
```

## Examples


``` yaml

- name: Create LUN
  na_cdot_lun:
    state: present
    name: ansibleLUN
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    size: 5
    size_unit: mb
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Resize Lun
  na_cdot_lun:
    state: present
    name: ansibleLUN
    force_resize: True
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    size: 5
    size_unit: gb
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
