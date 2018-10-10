# Ansible module: ansible.module_vmware_cluster_facts


Gather facts about clusters available in given vCenter

## Description

This module can be used to gather facts about clusters in VMWare infrastructure.
All values and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'If set, facts of this cluster will be returned.', 'This parameter is required, if C(datacenter) is not supplied.'], 'required': False}",
    "datacenter": "{'description': ['Datacenter to search for cluster/s.', 'This parameter is required, if C(cluster_name) is not supplied.'], 'required': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Gather cluster facts from given datacenter
  vmware_cluster_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: ha-datacenter
    validate_certs: no
  delegate_to: localhost
  register: cluster_facts

- name: Gather facts from datacenter about specific cluster
  vmware_cluster_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
  delegate_to: localhost
  register: cluster_facts

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
