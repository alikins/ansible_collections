# Ansible module: ansible.module_vmware_guest_tools_wait


Wait for VMware tools to become available

## Description

This module can be used to wait for VMware tools to become available on the given VM and return facts.

## Requirements

TODO

## Arguments

``` json
{
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest.', 'This is required only, if multiple VMs with same C(name) is found.', "The folder should include the datacenter. ESX's datacenter is C(ha-datacenter).", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the VM for which to wait until the tools become available.', 'This is required if uuid is not supplied.']}",
    "name_match": "{'description': ['If multiple VMs match the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the VM  for which to wait until the tools become available, if known. This is VMware's unique identifier.", 'This is required, if C(name) is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Wait for VMware tools to become available by UUID
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
  vmware_guest_tools_wait:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    uuid: "{{ vm_facts.instance.hw_product_uuid }}"
  delegate_to: localhost
  register: facts


- name: Wait for VMware tools to become available by name
  vmware_guest_tools_wait:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    name: test-vm
    folder: /"{{datacenter}}"/vm
  delegate_to: localhost
  register: facts

```

## License

TODO

## Author Information
  - ['Philippe Dellaert (@pdellaert) <philippe@dellaert.org>']
