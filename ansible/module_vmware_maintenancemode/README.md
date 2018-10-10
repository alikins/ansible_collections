# Ansible module: ansible.module_vmware_maintenancemode


Place a host into maintenance mode

## Description

This module can be used for placing a ESXi host into maintenance mode.
Support for VSAN compliant maintenance mode when selected.

## Requirements

TODO

## Arguments

``` json
{
    "esxi_hostname": "{'description': ['Name of the host as defined in vCenter.'], 'required': True}",
    "evacuate": "{'description': ['If set to C(True), evacuate all powered off VMs.'], 'default': False, 'required': False, 'type': 'bool'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Enter or exit maintenance mode.'], 'choices': ['present', 'absent'], 'default': 'present', 'required': False}",
    "timeout": "{'description': ['Specify a timeout for the operation.'], 'required': False, 'default': 0}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vsan": "{'description': ['Specify which VSAN compliant mode to enter.'], 'choices': ['ensureObjectAccessibility', 'evacuateAllData', 'noAction'], 'required': False, 'aliases': ['vsan_mode']}",
}
```

## Examples


``` yaml

- name: Enter VSAN-Compliant Maintenance Mode
  vmware_maintenancemode:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    vsan: ensureObjectAccessibility
    evacuate: yes
    timeout: 3600
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jay Jahns (@jjahns) <jjahns@vmware.com>', 'Abhijeet Kasurde (@Akasurde)']
  - ['Jay Jahns (@jjahns) <jjahns@vmware.com>', 'Abhijeet Kasurde (@Akasurde)']
