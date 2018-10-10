# Ansible module: ansible.module_vcenter_folder


Manage folders on given datacenter

## Description

This module can be used to create, delete, move and rename folder on then given datacenter.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Name of the datacenter.'], 'required': True}",
    "folder_name": "{'description': ['Name of folder to be managed.', 'This is case sensitive parameter.', 'Folder name should be under 80 characters. This is a VMware restriction.'], 'required': True}",
    "folder_type": "{'description': ['This is type of folder.', "If set to C(vm), then 'VM and Template Folder' is created under datacenter.", "If set to C(host), then 'Host and Cluster Folder' is created under datacenter.", "If set to C(datastore), then 'Storage Folder' is created under datacenter.", "If set to C(network), then 'Network Folder' is created under datacenter.", 'This parameter is required, if C(state) is set to C(present) and parent_folder is absent.', 'This option is ignored, if C(parent_folder) is set.'], 'default': 'vm', 'required': False, 'choices': ['datastore', 'host', 'network', 'vm']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "parent_folder": "{'description': ['Name of the parent folder under which new folder needs to be created.', 'This is case sensitive parameter.', 'Please specify unique folder name as there is no way to detect duplicate names.', "If user wants to create a folder under '/DC0/vm/vm_folder', this value will be 'vm_folder'."], 'required': False}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['State of folder.', 'If set to C(present) without parent folder parameter, then folder with C(folder_type) is created.', 'If set to C(present) with parent folder parameter,  then folder in created under parent folder. C(folder_type) is ignored.', 'If set to C(absent), then folder is unregistered and destroyed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create a VM folder on given datacenter
  vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    folder_name: sample_vm_folder
    folder_type: vm
    state: present
  register: vm_folder_creation_result
  delegate_to: localhost

- name: Create a datastore folder on given datacenter
  vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    folder_name: sample_datastore_folder
    folder_type: datastore
    state: present
  register: datastore_folder_creation_result
  delegate_to: localhost

- name: Create a sub folder under VM folder on given datacenter
  vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    folder_name: sample_sub_folder
    parent_folder: vm_folder
    state: present
  register: sub_folder_creation_result
  delegate_to: localhost

- name: Delete a VM folder on given datacenter
  vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    folder_name: sample_vm_folder
    folder_type: vm
    state: absent
  register: vm_folder_deletion_result
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
