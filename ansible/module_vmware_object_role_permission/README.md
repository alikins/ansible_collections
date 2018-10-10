# Ansible module: ansible.module_vmware_object_role_permission


Manage local roles on an ESXi host

## Description

T
h
i
s
 
m
o
d
u
l
e
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
m
a
n
a
g
e
 
o
b
j
e
c
t
 
p
e
r
m
i
s
s
i
o
n
s
 
o
n
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
.

## Requirements

TODO

## Arguments

``` json
{
    "group": "{'description': ['The group to be assigned permission.', 'Required if C(principal) is not specified.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "object_name": "{'description': ['The object name to assigned permission.'], 'required': True}",
    "object_type": "{'description': ['The object type being targeted.'], 'default': 'Folder', 'choices': ['Folder', 'VirtualMachine', 'Datacenter', 'ResourcePool', 'Datastore', 'Network', 'HostSystem', 'ComputeResource', 'ClusterComputeResource', 'DistributedVirtualSwitch']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "principal": "{'description': ['The user to be assigned permission.', 'Required if C(group) is not specified.']}",
    "recursive": "{'description': ['Should the permissions be recursively applied.'], 'default': True, 'type': 'bool'}",
    "role": "{'description': ['The role to be assigned permission.'], 'required': True}",
    "state": "{'description': ["Indicate desired state of the object's permission.", "When C(state=present), the permission will be added if it doesn't already exist.", 'When C(state=absent), the permission is removed if it exists.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Assign user to VM folder
  vmware_object_role_permission:
    role: administrator
    principal: user_bob
    object_name: services
    state: present
  delegate_to: localhost

- name: Remove user from VM folder
  vmware_object_role_permission:
    role: administrator
    principal: user_bob
    object_name: services
    state: absent
  delegate_to: localhost

- name: Assign finance group to VM folder
  vmware_object_role_permission:
    role: Limited Users
    group: finance
    object_name: Accounts
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Derek Rushing (@kryptsi)']
