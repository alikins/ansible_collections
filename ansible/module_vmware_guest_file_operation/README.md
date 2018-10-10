# Ansible module: ansible.module_vmware_guest_file_operation


Files operation in a VMware guest operating system without network

## Description

Module to copy a file to a VM, fetch a file from a VM and create or delete a directory in the guest OS.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['The cluster hosting the virtual machine.', 'If set, it will help to speed up virtual machine search.']}",
    "copy": "{'description': ['Copy file to vm without requiring network.', 'Valid attributes are:', '  src: file source absolute or relative', '  dest: file destination, path must be exist', '  overwrite: False or True (not required, default False)'], 'required': False}",
    "datacenter": "{'description': ['The datacenter hosting the virtual machine.', 'If set, it will help to speed up virtual machine search.']}",
    "directory": "{'description': ['Create or delete directory.', 'Valid attributes are:', '  path: directory path to create or remove', '  operation: Valid values are create, delete', '  recurse (boolean): Not required, default (false)'], 'required': False}",
    "fetch": "{'description': ['Get file from virtual machine without requiring network.', 'Valid attributes are:', '  src: The file on the remote system to fetch. This I(must) be a file, not a directory', '  dest: file destination on localhost, path must be exist'], 'required': False, 'version_added': 2.5}",
    "folder": "{'description': ['Destination folder, absolute path to find an existing guest or create the new guest.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter", 'Used only if C(vm_id_type) is C(inventory_path).', 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2', '   folder: vm/folder2', '   folder: folder2']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vm_id": "{'description': ['Name of the virtual machine to work with.'], 'required': True}",
    "vm_id_type": "{'description': ['The VMware identification method by which the virtual machine will be identified.'], 'default': 'vm_name', 'choices': ['uuid', 'dns_name', 'inventory_path', 'vm_name']}",
    "vm_password": "{'description': ['The password used to login-in to the virtual machine.'], 'required': True}",
    "vm_username": "{'description': ['The user to login in to the virtual machine.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create directory inside a vm
  vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: no
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    directory:
      path: "/test"
      operation: create
      recurse: no
  delegate_to: localhost

- name: copy file to vm
  vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    copy:
        src: "files/test.zip"
        dest: "/root/test.zip"
        overwrite: False
  delegate_to: localhost

- name: fetch file from vm
  vmware_guest_file_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    vm_id: "{{ guest_name }}"
    vm_username: "{{ guest_username }}"
    vm_password: "{{ guest_userpassword }}"
    fetch:
        src: "/root/test.zip"
        dest: "files/test.zip"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Stéphane Travassac (@stravassac)']
