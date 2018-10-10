# Ansible module: ansible.module_vmware_host_datastore


Manage a datastore on ESXi host

## Description

This module can be used to mount/umount datastore on ESXi host.
This module only support NFS/VMFS type of datastores.
For VMFS datastore, available device must already be connected on ESXi host.
All parameters and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter_name": "{'description': ['Name of the datacenter to add the datastore.'], 'required': True}",
    "datastore_name": "{'description': ['Name of the datastore to add/remove.'], 'required': True}",
    "datastore_type": "{'description': ['Type of the datastore to configure (nfs/vmfs).'], 'required': True, 'choices': ['nfs', 'vmfs']}",
    "esxi_hostname": "{'description': ['ESXi hostname to manage the datastore.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "nfs_path": "{'description': ['Resource path on NFS host.', 'Required if datastore type is set to C(nfs) and state is set to C(present), else unused.']}",
    "nfs_ro": "{'description': ['ReadOnly or ReadWrite mount.', 'Unused if datastore type is not set to C(nfs) and state is not set to C(present).'], 'default': False, 'type': 'bool'}",
    "nfs_server": "{'description': ['NFS host serving nfs datastore.', 'Required if datastore type is set to C(nfs) and state is set to C(present), else unused.']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['present: Mount datastore on host if datastore is absent else do nothing.', 'absent: Umount datastore if datastore is present else do nothing.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vmfs_device_name": "{'description': ['Name of the device to be used as VMFS datastore.', 'Required for VMFS datastore type and state is set to C(present), else unused.']}",
    "vmfs_version": "{'description': ['VMFS version to use for datastore creation.', 'Unused if datastore type is not set to C(vmfs) and state is not set to C(present).']}",
}
```

## Examples


``` yaml

- name: Mount VMFS datastores to ESXi
  vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datacenter_name: '{{ datacenter }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      vmfs_version: 6
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost

- name: Mount NFS datastores to ESXi
  vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datacenter_name: '{{ datacenter }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      nfs_server: '{{ item.server }}'
      nfs_path: '{{ item.path }}'
      nfs_ro: no
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost
  with_items:
      - { 'name': 'NasDS_vol01', 'server': 'nas01', 'path': '/mnt/vol01', 'type': 'nfs'}
      - { 'name': 'NasDS_vol02', 'server': 'nas01', 'path': '/mnt/vol02', 'type': 'nfs'}

- name: Remove/Umount Datastores from ESXi
  vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datacenter_name: '{{ datacenter }}'
      datastore_name: NasDS_vol01
      esxi_hostname: '{{ inventory_hostname }}'
      state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ludovic Rivallain (@lrivallain) <ludovic.rivallain@gmail.com>']
