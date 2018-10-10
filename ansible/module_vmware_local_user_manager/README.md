# Ansible module: ansible.module_vmware_local_user_manager


Manage local users on an ESXi host

## Description

Manage local users on an ESXi host

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "local_user_description": "{'description': ['Description for the user.'], 'required': False}",
    "local_user_name": "{'description': ['The local user name to be changed.'], 'required': True}",
    "local_user_password": "{'description': ['The password to be set.'], 'required': False}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Indicate desired state of the user. If the user already exists when C(state=present), the user info is updated'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add local user to ESXi
  vmware_local_user_manager:
    hostname: esxi_hostname
    username: root
    password: vmware
    local_user_name: foo
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Andreas Nafpliotis (@nafpliot-ibm)']
