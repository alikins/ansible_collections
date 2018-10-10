# Ansible module: ansible.module_vmware_host_lockdown


Manage administrator permission for the local administrative account for the ESXi host

## Description

This module can be used to manage administrator permission for the local administrative account for the host when ESXi hostname is given.
All parameters and VMware objects values are case sensitive.
This module is destructive as administrator permission are managed using APIs used, please read options carefully and proceed.
Please specify C(hostname) as vCenter IP or hostname only, as lockdown operations are not possible from standalone ESXi server.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of cluster.', 'All host systems from given cluster used to manage lockdown.', 'Required parameter, if C(esxi_hostname) is not set.']}",
    "esxi_hostname": "{'description': ['List of ESXi hostname to manage lockdown.', 'Required parameter, if C(cluster_name) is not set.', 'See examples for specifications.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['State of hosts system', 'If set to C(present), all host systems will be set in lockdown mode.', 'If host system is already in lockdown mode and set to C(present), no action will be taken.', 'If set to C(absent), all host systems will be removed from lockdown mode.', 'If host system is already out of lockdown mode and set to C(absent), no action will be taken.'], 'default': 'present', 'choices': ['present', 'absent'], 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Enter host system into lockdown mode
  vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: present
  delegate_to: localhost

- name: Exit host systems from lockdown mode
  vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: absent
  delegate_to: localhost

- name: Enter host systems into lockdown mode
  vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname:
        - '{{ esxi_hostname_1 }}'
        - '{{ esxi_hostname_2 }}'
    state: present
  delegate_to: localhost

- name: Exit host systems from lockdown mode
  vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname:
        - '{{ esxi_hostname_1 }}'
        - '{{ esxi_hostname_2 }}'
    state: absent
  delegate_to: localhost

- name: Enter all host system from cluster into lockdown mode
  vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
