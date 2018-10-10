# Ansible module: ansible.module_vmware_guest_boot_manager


Manage boot options for the given virtual machine

## Description

This module can be used to manage boot options for the given virtual machine.

## Requirements

TODO

## Arguments

``` json
{
    "boot_delay": "{'description': ['Delay in milliseconds before starting the boot sequence.'], 'default': 0}",
    "boot_firmware": "{'description': ['Choose which firmware should be used to boot the virtual machine.'], 'choices': ['bios', 'efi']}",
    "boot_order": "{'description': ['List of the boot devices.'], 'default': []}",
    "boot_retry_delay": "{'description': ['Specify the time in milliseconds between virtual machine boot failure and subsequent attempt to boot again.', 'If set, will automatically set C(boot_retry_enabled) to C(True) as this parameter is required.'], 'default': 0}",
    "boot_retry_enabled": "{'description': ['If set to C(True), the virtual machine that fails to boot, will try to boot again after C(boot_retry_delay) is expired.', 'If set to C(False), the virtual machine waits indefinitely for user intervention.'], 'type': 'bool', 'default': False}",
    "enter_bios_setup": "{'description': ['If set to C(True), the virtual machine automatically enters BIOS setup the next time it boots.', 'The virtual machine resets this flag, so that the machine boots proceeds normally.'], 'type': 'bool', 'default': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the VM to work with.', 'This is required if C(uuid) parameter is not supplied.']}",
    "name_match": "{'description': ['If multiple virtual machines matching the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this is VMware's BIOS UUID.", 'This is required if C(name) parameter is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Change virtual machine's boot order and related parameters
  vmware_guest_boot_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: testvm
    boot_delay: 2000
    enter_bios_setup: True
    boot_retry_enabled: True
    boot_retry_delay: 22300
    boot_firmware: bios
    boot_order:
      - floppy
      - cdrom
      - ethernet
      - disk
  delegate_to: localhost
  register: vm_boot_order

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
