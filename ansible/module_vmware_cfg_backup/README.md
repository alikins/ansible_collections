# Ansible module: ansible.module_vmware_cfg_backup


Backup / Restore / Reset ESXi host configuration

## Description

This module can be used to perform various operations related to backup, restore and reset of ESXi host configuration.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['The destination where the ESXi configuration bundle will be saved. The I(dest) can be a folder or a file.', 'If I(dest) is a folder, the backup file will be saved in the folder with the default filename generated from the ESXi server.', 'If I(dest) is a file, the backup file will be saved with that filename. The file extension will always be .tgz.']}",
    "esxi_hostname": "{'description': ['Name of ESXi server. This is required only if authentication against a vCenter is done.'], 'required': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "src": "{'description': ['The file containing the ESXi configuration that will be restored.']}",
    "state": "{'description': ['If C(saved), the .tgz backup bundle will be saved in I(dest).', 'If C(absent), the host configuration will be reset to default values.', 'If C(loaded), the backup file in I(src) will be loaded to the ESXi host rewriting the hosts settings.'], 'choices': ['saved', 'absent', 'loaded']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Save the ESXi configuration locally by authenticating directly against the ESXi host
  vmware_cfg_backup:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    state: saved
    dest: /tmp/
  delegate_to: localhost

- name: Save the ESXi configuration locally by authenticating against the vCenter and selecting the ESXi host
  vmware_cfg_backup:
    hostname: '{{ vcenter_hostname }}'
    esxi_hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    state: saved
    dest: /tmp/
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Andreas Nafpliotis (@nafpliot-ibm)']
