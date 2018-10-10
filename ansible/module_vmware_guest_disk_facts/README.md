# Ansible module: ansible.module_vmware_guest_disk_facts


Gather facts about disks of given virtual machine

## Description

This module can be used to gather facts about disks belonging to given virtual machine.
All parameters and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['The datacenter name to which virtual machine belongs to.'], 'required': True}",
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest.', 'This is required parameter, only if multiple VMs are found with same name.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2', '   folder: vm/folder2', '   folder: folder2']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the virtual machine.', 'This is required parameter, if parameter C(uuid) is not supplied.']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to gather facts if known, this is VMware's unique identifier.", 'This is required parameter, if parameter C(name) is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Gather disk facts from virtual machine using UUID
  vmware_guest_disk_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    validate_certs: no
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
  delegate_to: localhost
  register: disk_facts

- name: Gather disk facts from virtual machine using name
  vmware_guest_disk_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    validate_certs: no
    name: VM_225
  delegate_to: localhost
  register: disk_facts

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
