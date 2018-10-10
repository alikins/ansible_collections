# Ansible module: ansible.module_vmware_local_role_manager


Manage local roles on an ESXi host

## Description

This module can be used to manage local roles on an ESXi host.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['This parameter is only valid while updating an existing role with privileges.', 'C(add) will add the privileges to the existing privilege list.', 'C(remove) will remove the privileges from the existing privilege list.', 'C(set) will replace the privileges of the existing privileges with user defined list of privileges.'], 'default': 'set', 'choices': ['add', 'remove', 'set'], 'version_added': 2.8}",
    "force_remove": "{'description': ['If set to C(False) then prevents the role from being removed if any permissions are using it.'], 'default': False, 'type': 'bool'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "local_privilege_ids": "{'description': ['The list of privileges that role needs to have.', 'Please see U(https://docs.vmware.com/en/VMware-vSphere/6.0/com.vmware.vsphere.security.doc/GUID-ED56F3C4-77D0-49E3-88B6-B99B8B437B62.html)'], 'default': []}",
    "local_role_name": "{'description': ['The local role name to be managed.'], 'required': True}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Indicate desired state of the role.', 'If the role already exists when C(state=present), the role info is updated.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add local role to ESXi
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    state: present
  delegate_to: localhost

- name: Add local role with privileges to ESXi
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create', 'Folder.Delete']
    state: present
  delegate_to: localhost

- name: Remove local role from ESXi
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    state: absent
  delegate_to: localhost

- name: Add a privilege to an existing local role
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: add
  delegate_to: localhost

- name: Remove a privilege to an existing local role
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: remove
  delegate_to: localhost

- name: Set a privilege to an existing local role
  vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: set
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
