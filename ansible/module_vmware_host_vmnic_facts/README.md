# Ansible module: ansible.module_vmware_host_vmnic_facts


Gathers facts about vmnics available on the given ESXi host

## Description

This module can be used to gather facts about vmnics available on the given ESXi host.
If C(cluster_name) is provided, then vmnic facts about all hosts from given cluster will be returned.
If C(esxi_hostname) is provided, then vmnic facts about given host system will be returned.
Additional details about vswitch and dvswitch with respective vmnic is also provided which is added in 2.7 version.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'Vmnic facts about each ESXi server will be returned for the given cluster.', 'If C(esxi_hostname) is not given, this parameter is required.']}",
    "esxi_hostname": "{'description': ['ESXi hostname.', 'Vmnic facts about this ESXi server will be returned.', 'If C(cluster_name) is not given, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Gather facts about vmnics of all ESXi Host in the given Cluster
  vmware_host_vmnic_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmnics

- name: Gather facts about vmnics of an ESXi Host
  vmware_host_vmnic_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmnics

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
