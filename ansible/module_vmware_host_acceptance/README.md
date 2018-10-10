# Ansible module: ansible.module_vmware_host_acceptance


Manage the host acceptance level of an ESXi host

## Description

This module can be used to manage the host acceptance level of an ESXi host.
The host acceptance level controls the acceptance level of each VIB on a ESXi host.

## Requirements

TODO

## Arguments

``` json
{
    "acceptance_level": "{'description': ['Name of acceptance level.', 'If set to C(partner), then accept only partner and VMware signed and certified VIBs.', 'If set to C(vmware_certified), then accept only VIBs that are signed and certified by VMware.', 'If set to C(vmware_accepted), then accept VIBs that have been accepted by VMware.', 'If set to C(community), then accept all VIBs, even those that are not signed.'], 'choices': ['community', 'partner', 'vmware_accepted', 'vmware_certified'], 'required': False}",
    "cluster_name": "{'description': ['Name of the cluster.', 'Acceptance level of all ESXi host system in the given cluster will be managed.', 'If C(esxi_hostname) is not given, this parameter is required.']}",
    "esxi_hostname": "{'description': ['ESXi hostname.', 'Acceptance level of this ESXi host system will be managed.', 'If C(cluster_name) is not given, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Set or list acceptance level of the given ESXi host.', 'If set to C(list), then will return current acceptance level of given host system/s.', 'If set to C(present), then will set given acceptance level.'], 'choices': ['list', 'present'], 'required': False, 'default': 'list'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Set acceptance level to community for all ESXi Host in given Cluster
  vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    acceptance_level: 'community'
    state: present
  delegate_to: localhost
  register: cluster_acceptance_level

- name: Set acceptance level to vmware_accepted for the given ESXi Host
  vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    acceptance_level: 'vmware_accepted'
    state: present
  delegate_to: localhost
  register: host_acceptance_level

- name: Get acceptance level from the given ESXi Host
  vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: list
  delegate_to: localhost
  register: host_acceptance_level

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
