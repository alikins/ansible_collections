# Ansible module: ansible.module_vmware_guest_find


Find the folder path(s) for a virtual machine by name or UUID

## Description

Find the folder path(s) for a virtual machine by name or UUID

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Destination datacenter for the find operation.', 'Deprecated in 2.5, will be removed in 2.9 release.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the VM to work with.', 'This is required if C(uuid) parameter is not supplied.']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this is VMware's BIOS UUID.", 'This is required if C(name) parameter is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Find Guest's Folder using name
  vmware_guest_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    name: testvm
  delegate_to: localhost
  register: vm_folder

- name: Find Guest's Folder using UUID
  vmware_guest_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 38c4c89c-b3d7-4ae6-ae4e-43c5118eae49
  delegate_to: localhost
  register: vm_folder

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde <akasurde@redhat.com>']
