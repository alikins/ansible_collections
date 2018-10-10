# Ansible module: ansible.module_vmware_target_canonical_facts


Return canonical (NAA) from an ESXi host system

## Description

This module can be used to gather facts about canonical (NAA) from an ESXi host based on SCSI target ID.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'Facts about all SCSI devices for all host system in the given cluster is returned.', 'This parameter is required, if C(esxi_hostname) is not provided.'], 'version_added': 2.6}",
    "esxi_hostname": "{'description': ['Name of the ESXi host system.', 'Facts about all SCSI devices for the given ESXi host system is returned.', 'This parameter is required, if C(cluster_name) is not provided.'], 'version_added': 2.6}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "target_id": "{'description': ['The target id based on order of scsi device.', 'version 2.6 onwards, this parameter is optional.'], 'required': False}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Get Canonical name of particular target on particular ESXi host system
  vmware_target_canonical_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    target_id: 7
    esxi_hostname: esxi_hostname
  delegate_to: localhost

- name: Get Canonical name of all target on particular ESXi host system
  vmware_target_canonical_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost

- name: Get Canonical name of all ESXi hostname on particular Cluster
  vmware_target_canonical_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
