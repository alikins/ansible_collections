# Ansible module: ansible.module_na_cdot_qtree


Manage qtrees

## Description

Create or destroy Qtrees.

## Requirements

TODO

## Arguments

``` json
{
    "flexvol_name": "{'description': ['The name of the FlexVol the Qtree should exist on. Required when C(state=present).']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "name": "{'description': ['The name of the Qtree to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified Qtree should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create QTree
  na_cdot_qtree:
    state: present
    name: ansibleQTree
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename QTree
  na_cdot_qtree:
    state: present
    name: ansibleQTree
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
