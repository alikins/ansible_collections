# Ansible module: ansible.module_vmware_vswitch


Manage a VMware Standard Switch to an ESXi host

## Description

This module can be used to add, remove and update a VMware Standard Switch to an ESXi host.

## Requirements

TODO

## Arguments

``` json
{
    "esxi_hostname": "{'description': ['Manage the vSwitch using this ESXi host system.'], 'version_added': '2.5', 'aliases': ['host']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "mtu": "{'description': ['MTU to configure on vSwitch.'], 'default': 1500}",
    "nics": "{'description': ['A list of vmnic names or vmnic name to attach to vSwitch.', 'Alias C(nics) is added in version 2.4.'], 'aliases': ['nic_name'], 'default': []}",
    "number_of_ports": "{'description': ['Number of port to configure on vSwitch.'], 'default': 128}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Add or remove the switch.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "switch": "{'description': ['vSwitch name to add.', 'Alias C(switch) is added in version 2.4.'], 'required': True, 'aliases': ['switch_name']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add a VMware vSwitch
  vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vswitch_name
    nics: vmnic_name
    mtu: 9000
  delegate_to: localhost

- name: Add a VMWare vSwitch without any physical NIC attached
  vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vswitch_0001
    mtu: 9000
  delegate_to: localhost

- name: Add a VMWare vSwitch with multiple NICs
  vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vmware_vswitch_0004
    nics:
    - vmnic1
    - vmnic2
    mtu: 9000
  delegate_to: localhost

- name: Add a VMware vSwitch to a specific host system
  vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    nic_name: vmnic0
    mtu: 9000
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
