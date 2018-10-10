# Ansible module: ansible.module_vmware_guest_move


Moves virtual machines in vCenter

## Description

This module can be used to move virtual machines between folders.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Destination datacenter for the move operation'], 'required': True}",
    "dest_folder": "{'description': ['Absolute path to move an existing guest', "The dest_folder should include the datacenter. ESX's datacenter is ha-datacenter.", 'This parameter is case sensitive.', 'Examples:', '   dest_folder: /ha-datacenter/vm', '   dest_folder: ha-datacenter/vm', '   dest_folder: /datacenter1/vm', '   dest_folder: datacenter1/vm', '   dest_folder: /datacenter1/vm/folder1', '   dest_folder: datacenter1/vm/folder1', '   dest_folder: /folder1/datacenter1/vm', '   dest_folder: folder1/datacenter1/vm', '   dest_folder: /folder1/datacenter1/vm/folder2'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the existing virtual machine to move.', 'This is required if C(UUID) is not supplied.']}",
    "name_match": "{'description': ['If multiple virtual machines matching the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the virtual machine to manage if known, this is VMware's unique identifier.", 'This is required if C(name) is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Move Virtual Machine
  vmware_guest_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: datacenter
    validate_certs: no
    name: testvm-1
    dest_folder: /"{{ datacenter }}"/vm
  delegate_to: localhost

- name: Get VM UUID
  vmware_guest_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    datacenter: "{{ datacenter }}"
    folder: /"{{datacenter}}"/vm
    name: "{{ vm_name }}"
  delegate_to: localhost
  register: vm_facts

- name: Get UUID from previous task and pass it to this task
  vmware_guest_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    datacenter: "{{ datacenter }}"
    uuid: "{{ vm_facts.instance.hw_product_uuid }}"
    dest_folder: "/DataCenter/vm/path/to/new/folder/where/we/want"
  delegate_to: localhost
  register: facts

```

## License

TODO

## Author Information
  - ['Jose Angel Munoz (@imjoseangel)']
