# Ansible module: ansible.module_vmware_vmotion


Move a virtual machine using vMotion, and/or its vmdks using storage vMotion

## Description

Using VMware vCenter, move a virtual machine using vMotion to a different host, and/or its vmdks to another datastore using storage vMotion.

## Requirements

TODO

## Arguments

``` json
{
    "destination_datastore": "{'description': ["Name of the destination datastore the virtual machine's vmdk should be moved on."], 'aliases': ['datastore'], 'version_added': 2.7}",
    "destination_host": "{'description': ['Name of the destination host the virtual machine should be running on.', 'Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.'], 'aliases': ['destination']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vm_name": "{'description': ['Name of the VM to perform a vMotion on.', 'This is required parameter, if C(vm_uuid) is not set.', 'Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.'], 'aliases': ['vm']}",
    "vm_uuid": "{'description': ['UUID of the virtual machine to perform a vMotion operation on.', 'This is a required parameter, if C(vm_name) is not set.'], 'aliases': ['uuid'], 'version_added': 2.7}",
}
```

## Examples


``` yaml

- name: Perform vMotion of virtual machine
  vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    vm_name: 'vm_name_as_per_vcenter'
    destination_host: 'destination_host_as_per_vcenter'
  delegate_to: localhost

- name: Perform storage vMotion of of virtual machine
  vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    vm_name: 'vm_name_as_per_vcenter'
    destination_datastore: 'destination_datastore_as_per_vcenter'
  delegate_to: localhost

- name: Perform storage vMotion and host vMotion of virtual machine
  vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    vm_name: 'vm_name_as_per_vcenter'
    destination_host: 'destination_host_as_per_vcenter'
    destination_datastore: 'destination_datastore_as_per_vcenter'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Bede Carroll (@bedecarroll)', 'Olivier Boukili (@oboukili)']
  - ['Bede Carroll (@bedecarroll)', 'Olivier Boukili (@oboukili)']
