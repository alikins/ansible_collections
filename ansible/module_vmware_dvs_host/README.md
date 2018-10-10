# Ansible module: ansible.module_vmware_dvs_host


Add or remove a host from distributed virtual switch

## Description

Manage a host system from distributed virtual switch.

## Requirements

TODO

## Arguments

``` json
{
    "esxi_hostname": "{'description': ['The ESXi hostname.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['If the host should be present or absent attached to the vSwitch.'], 'choices': ['present', 'absent'], 'required': True, 'default': 'present'}",
    "switch_name": "{'description': ['The name of the Distributed vSwitch.'], 'required': True}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vmnics": "{'description': ['The ESXi hosts vmnics to use with the Distributed vSwitch.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Add Host to dVS
  vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    vmnics:
        - vmnic0
        - vmnic1
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
