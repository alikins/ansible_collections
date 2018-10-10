# Ansible module: ansible.module_na_ontap_lun


NetApp ONTAP manage LUNs

## Description

Create, destroy, resize LUNs on NetApp ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "flexvol_name": "{'description': ['The name of the FlexVol the LUN should exist on.'], 'required': True}",
    "force_remove": "{'description': ['If "true", override checks that prevent a LUN from being destroyed if it is online and mapped.', 'If "false", destroying an online and mapped LUN will fail.'], 'type': 'bool', 'default': False}",
    "force_remove_fenced": "{'description': ['If "true", override checks that prevent a LUN from being destroyed while it is fenced.', 'If "false", attempting to destroy a fenced LUN will fail.', 'The default if not specified is "false". This field is available in Data ONTAP 8.2 and later.'], 'type': 'bool', 'default': False}",
    "force_resize": "{'description': ['Forcibly reduce the size. This is required for reducing the size of the LUN to avoid accidentally reducing the LUN size.'], 'type': 'bool', 'default': False}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the LUN to manage.'], 'required': True}",
    "ostype": "{'description': ['The os type for the LUN.'], 'default': 'image'}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "size": "{'description': ['The size of the LUN in C(size_unit).', 'Required when C(state=present).']}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter.'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "space_allocation": "{'description': ['This enables support for the SCSI Thin Provisioning features.  If the Host and file system do not support this do not enable it.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "space_reserve": "{'description': ['This can be set to "false" which will create a LUN without any space being reserved.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['Whether the specified LUN should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'required': True, 'description': ['The name of the vserver to use.']}",
}
```

## Examples


``` yaml

- name: Create LUN
  na_ontap_lun:
    state: present
    name: ansibleLUN
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    size: 5
    size_unit: mb
    ostype: linux
    space_reserve: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Resize LUN
  na_ontap_lun:
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
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
